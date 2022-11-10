import pygame as pg
from config import *
from map import *
from bodies import *

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
    self.players = [Player((2,2),10)]
    self.map = Map(game)

  def update (self,game):
    """
    Makes the bodies evolve from 1 state to the next.
    """
    self.players[0].update()
    pg.display.flip()
    game.clock.tick(Config.FRAME_RATE)

  def draw(self,game):
    game.window.fill('red') # Test
    # self.camera.draw()
    self.map.draw(self)
    self.players[0].draw()
    # self.world.players.draw(self)
    pass