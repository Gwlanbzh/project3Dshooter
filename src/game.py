import pygame as pg
from pygame import Vector2 as v2
import sys
from config import *
from world import *
from render import Camera
from bodys import *

class Game:
    def __init__(self):
        """
        Important init for the game main component
        """
        pg.init()
        self.window = pg.display.set_mode(Config.WINDOW_SIZE)
        #self.window = pg.display.set_mode(Config.WINDOW_SIZE, pg.FULLSCREEN)
        #pg.display.toggle_fullscreen()
        self.world = World(self) 
        self.delta_time = 1 # utiliser dans le world.update et pour les vitesses
        self.clock = pg.time.Clock() # help managing time
        self.camera = Camera(self.world.players[0])
        
        
    
    def check_event(self):
        """
        Check if Client ask to quit
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit() # quit pygame
                sys.exit() # better quit, remove somme error when  quiting
  
    def run(self):
        """
        Main Game Loop 
        """
        while True:
            self.check_event()
            # self.world.draw2d(game)
            self.world.update(self)
            self.camera.draw_frame(self.window)
            pg.display.update()
            self.delta_time =  self.clock.tick(Config.FRAME_RATE)
            fps = self.clock.get_fps()
            pg.display.set_caption(f"{fps:.2f}")
  
if __name__ == "__main__":
    game = Game()
    game.run()
