import pygame as pg
from game_config import *
from map import *

class World: 
  def __init__(self,game):
    self.props = []
    self.mobs = []
    self.players = []
    self.map = Map(game)

  def update (self,game):
    pg.display.flip()
    game.clock.tick(GameConfig.FRAME_RATE)