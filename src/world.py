import pygame as pg
from config import *
from map import Map
from body import Body
from Bodys.Creatures.mob import Mob 
from Bodys.Creatures.player import Player 
from pygame import Vector2 as v2

class World:
    """
    World containing a map, props, mobs and players evolving in it,
    and updating them.
    """ 
    def __init__(self,game):
        """
        Spawns a Body.
         # For now Body are purple
         #         Mob are red
         #         Player are blue
         # Creature have a tray for orientation
        
        Input:
            game : Game
        
        Outputs:
            World
        """
        self.props = [Body(game,v2(350,150)),
                      Body(game,v2(950,450)),
                      Body(game,v2(550,550)),
                      Body(game,v2(850,650))]
        self.mobs = [Mob(game,v2(450,150)),
                     Mob(game,v2(450,450)),
                     Mob(game,v2(550,650)),
                     Mob(game,v2(750,450))]
        self.players = [Player(game,v2(150,150))]
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
        for mob in self.mobs:
            mob.update()
            pass
  
    def draw(self,game):
        """
        Draw world
  
        temporary way to display world may change by camera
        """
        game.window.fill('grey')
        # self.camera.draw()
        for prop in self.props:
            prop.draw(game)
        self.map.draw(game)
        for mob in self.mobs:
            mob.draw(game)
        self.players[0].draw(game)
        pass