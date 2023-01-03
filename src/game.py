import pygame as pg
from pygame import Vector2 as v2
import sys
from config import *
from world import *
from render import Camera
from bodys import *
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
            self.window = pg.display.set_mode(Config.WINDOW_SIZE, pg.FULLSCREEN)
        
        self.world = World(self, map_file) 
        self.path_finding = PathFinding(self)

        #self.world.init_bodys(self)

        self.delta_time = 1 # utiliser dans le world.update et pour les vitesses
        self.clock = pg.time.Clock() # help managing time
        self.camera = Camera(self.world.players[0])
        self.draw2d = draw2d

        self.font = pg.font.Font(pg.font.get_default_font(), 24)
    
    def check_event(self):
        """
        Check if Client ask to quit
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit() # quit pygame
                sys.exit() # better quit, remove some error when  quiting
    
    def is_game_over(self):
        return ""
    
    def display_info(self, text: str):
        img = self.font.render(text, False, (255, 255, 255))
        self.window.blit(img, (10, 10))
  
    def run(self):
        """
        Main Game Loop 
        """
        while not self.is_game_over():
            self.check_event()
            self.world.update(self)
            
            if self.draw2d:
                self.world.draw2d(self)
            else:
                self.camera.draw_frame(self.window)

            fps = self.clock.get_fps()
            self.display_info(f"FPS: {fps:.2f} ; Health: {self.world.players[0].health} ; Ammo: {self.world.players[0].ammo}")
            pg.display.update()
            self.delta_time =  self.clock.tick(Config.FRAME_RATE)
            pg.display.set_caption(f"{fps:.2f}")
  
if __name__ == "__main__":
    draw2d = 0
    game = Game("src/assets/maps/map_dest.bin", draw2d)
    game.run()
