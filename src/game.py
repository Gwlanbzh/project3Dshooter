import pygame as pg
import sys
from config import *
from world import *
from map import *

class Game:
  def __init__(self):
    pg.init()
    self.window = pg.display.set_mode(Config.WINDOW_SIZE)
    self.world = World(Map)
    self.delta_time = 1
    self.clock = pg.time.Clock()
  
  def check_event(self):
    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        sys.exit() # better quit
  
  
  
  def run(self):
    while True:
      self.world.update(self)
      self.check_event()
      self.world.draw(game)






if __name__ == "__main__":
  game = Game()
  game.run()
