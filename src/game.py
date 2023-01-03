import pygame as pg
from pygame import Vector2 as v2
import sys
from config import *
from world import *
from render import Camera
from bodys import *
from hud import Hud
from menu import MainMenu
from bodys.creatures.path_finding import *

class Game:
    """
    Base class for a game, to be used to define new game types.
    """
    def __init__(self, map_file, draw2d):
        """
        Important init for the game main component
        """
        pg.init()
        
        if draw2d:
            self.window = pg.display.set_mode(Config.WINDOW_SIZE)
        else:
            self.window = pg.display.set_mode(Config.WINDOW_SIZE)

        self.main_menu = MainMenu(self)

        #self.world.init_bodys(self)

        self.delta_time = 1 # utiliser dans le world.update et pour les vitesses
        self.clock = pg.time.Clock() # help managing time
        self.map_file = map_file

        self.world_loaded = False

        # self.load_world()
        
    def load_world(self,map_file):
        self.world = World(self,map_file) 
        self.path_finding = PathFinding(self)
        self.draw2d = draw2d
        self.camera = Camera(self.world.players[0])
        self.hud = Hud(self)
        self.world_loaded = True
        self.is_paused = False

    def unload_world(self):
        self.world_loaded = False
    
    def check_event(self):
        """
        Check if Client ask to quit
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()

            if self.world_loaded:
                self.hud.click(event)
                self.hud.over()
            else:
                self.main_menu.click(event)
                self.main_menu.over()

    def quit(self):
        pg.quit()  # quit pygame
        sys.exit()  # better quit, remove some error when  quiting
    
    def is_game_over(self):
        return False
    
    def display_info(self, text: str):
        img = self.font.render(text, False, (255, 255, 255))
        self.window.blit(img, (10, 10))
   
    def run(self):
        """
        Main Game Loop 
        """
        while not self.is_game_over():
            self.check_event()

            if not self.world_loaded:
                self.main_menu.draw()

            if self.world_loaded:
                # self.world.draw2d(game)
                self.world.update(self)
                if self.draw2d:
                    self.world.draw2d(self)
                else:
                    self.camera.draw_frame(self.window)
                self.hud.update()
                self.hud.draw()


            fps = self.clock.get_fps()
            pg.display.update()
            self.delta_time =  self.clock.tick(Config.FRAME_RATE)
            pg.display.set_caption(f"{fps:.2f}")
  
if __name__ == "__main__":
    draw2d = False
    game = Game("src/assets/maps/map_dest.bin", draw2d)
    game.run()
