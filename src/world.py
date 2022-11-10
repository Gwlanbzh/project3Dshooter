import pygame as pg
from bodies import *

class World():
    """
    World containing a map, props, mobs and players evolving in it,
    and updating them.
    """
    def __init__(self):
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
        
        # add map data structure
    
    def update(self):
        """
        Makes the bodies evolve from 1 state to the next.
        """
        pass
