import pygame as pg
import sys
from game_config import *
from world import *

class Game:
  def __init__(self):
    pg.init()
    self.window = pg.display.set_mode(GameConfig.WINDOW_SIZE)
    self.world = World()
    self.clock = pg.time.Clock()

  def check_event(self):
    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        sys.exit() # better quit

  def draw(self):
    self.window.fill('red') # Test
    # self.camera.draw()
    pass

  def update (self): # a deplacer dans world
    pg.display.flip()
    self.clock.tick(GameConfig.FRAME_RATE)

  def run(self):
    while True:
      self.update()
      self.check_event()
      self.update()






if __name__ == "__main__":
  game = Game()
  game.run()
