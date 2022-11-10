import pygame as pg
from game_config import *

class World: 
  def __init__(self):
    self.props = []
    self.mobs = []
    self.players = []

  # def update (self):
  #   pg.display.flip()
  #   self.clock.tick(GameConfig.FrameRate)