import pygame as pg
import sys
from config import *
from world import *

class Game:
    def __init__(self):
        """
        Important init for the game main component
        """
        pg.init()
        Config.init()
        self.window = pg.display.set_mode(Config.WINDOW_SIZE)
        self.world = World(self) 
        # self.camera = Camera()
        self.delta_time = 1 # utiliser dans le world.update et pour les vittesse
        self.clock = pg.time.Clock() # help managing time
    
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
            self.world.draw(game)
            pg.display.update()
            self.delta_time =  self.clock.tick(Config.FRAME_RATE)
  
if __name__ == "__main__":
    game = Game()
    game.run()
