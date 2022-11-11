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
            game : Game
        
        Outputs:
            World
        """
        self.props = []
        self.mobs = []
        self.players = [Player(game,(2,2))]
        self.map = Map(game)
  
    def update (self,game):
        """
        call upadate for every Body(or more) in the world
        and
  
        Input:
            game : Game
        
        Outputs:
            <none>
        """
        self.players[0].update()
  
    def draw(self,game):
        """
        Draw world
  
        temporary way to display world may change by camera
        """
        game.window.fill('grey')
        # self.camera.draw()
        self.map.draw(game)
        self.players[0].draw(game)
        pass