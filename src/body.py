import pygame as pg 
from pygame import Vector2 as v2

class Body():
    """
    Static body with a position and animated sprites.
    """
    def __init__(self, game, r: tuple):
        """
        Spanws a Body.
        
        Input:
            r: tuple (x,y)
        
        Outputs:
            Body
        """
        self.r = v2(r)
        self.v = (0, 0) # FIXME not use for now
        self.color = 'magenta'
        self.game = game # link to dt
        ## TODO add sprites data structure
    
    def get_sprite(self):
        """
        TODO Returns a Surface representing the current sprite to display.
        
        Inputs:
            <none>
        
        Outputs:
            Surface
        """
        pass

    def draw(self,game): # draw object
        traylenght = 100
        pg.draw.circle(game.window, self.color, tuple(self.r),15)
