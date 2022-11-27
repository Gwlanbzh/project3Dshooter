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
        #self.window = pg.display.set_mode(Config.WINDOW_SIZE)
        self.window = pg.display.set_mode(Config.WINDOW_SIZE, pg.FULLSCREEN)
        #pg.display.toggle_fullscreen()
        self.world = World(self) 
        # self.camera = Camera()
        self.delta_time = 1 # utiliser dans le world.update et pour les vitesses
        self.clock = pg.time.Clock() # help managing time
        
        self.camera = Camera(self.world.players[0])
        
        #if view == "first person":
            #self.camera = Camera(self.world.players[0])
            #self.draw = self.camera.draw_frame(self.window)
        #else:
            #self.draw = self.world.draw(self)
        
    
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
            self.world.update(self)
            #self.world.draw(game)
            self.camera.draw_frame(self.window)
            #self.draw()
            pg.display.update()
            self.delta_time =  self.clock.tick(Config.FRAME_RATE)
            fps = self.clock.get_fps()
            pg.display.set_caption(f"{fps:.2f}")
            self.delta_time =  self.clock.tick(Config.FRAME_RATE)
  
if __name__ == "__main__":
    game = Game()
    game.run()
