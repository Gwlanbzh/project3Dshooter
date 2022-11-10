import pygame as pg
from config import *
from map import *

class World:
  """
  World containing a map, props, mobs and players evolving in it,
  and updating them.
  """ 
  def __init__(self,game):
    """
    Spawns a Body.
    
    Input:
        <none>
    
    Outputs:
        World
    """
    self.props = []
    self.mobs = []
    self.players = []
    self.map = Map(game)

  def update (self,game):
    """
    Makes the bodies evolve from 1 state to the next.
    """
    pg.display.flip()
    game.clock.tick(Config.FRAME_RATE)