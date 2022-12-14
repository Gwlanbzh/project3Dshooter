import pygame as pg
from pygame import Vector2 as v2
import sys
from config import *
from world import *
from render import Camera
from bodys import *
from hud import Hud
from menu import MainMenu

class Game:
    def __init__(self):
        """
        Important init for the game main component
        """
        pg.init()
        self.window = pg.display.set_mode(Config.WINDOW_SIZE)
        #self.window = pg.display.set_mode(Config.WINDOW_SIZE, pg.FULLSCREEN)
        #pg.display.toggle_fullscreen()

        self.main_menu = MainMenu(self)
        self.delta_time = 1 # utiliser dans le world.update et pour les vitesses
        self.clock = pg.time.Clock() # help managing time

        self.world_loaded = False
        
    def load_world(self):
        self.world = World(self) 
        self.hud = Hud(self)
        self.camera = Camera(self.world.players[0])
        self.world_loaded = True

    def unload_world(self):
        self.world_loaded = False
    
    def check_event(self):
        """
        Check if Client ask to quit
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit() # quit pygame
                sys.exit() # better quit, remove somme error when  quiting

            if self.world_loaded:
                self.hud.click(event)
  
    def run(self):
        """
        Main Game Loop 
        """
        while True:
            self.check_event()

            if not self.world_loaded:
                self.main_menu.draw()

                pass

            if self.world_loaded:
                # self.world.draw2d(game)
                self.world.update(self)
                self.camera.draw_frame(self.window)
                self.hud.update()
                self.hud.draw()

            pg.display.update()
            self.delta_time =  self.clock.tick(Config.FRAME_RATE)
            fps = self.clock.get_fps()
            pg.display.set_caption(f"{fps:.2f}")
  
if __name__ == "__main__":
    game = Game()
    game.run()
