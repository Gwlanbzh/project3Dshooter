import pygame as pg 
from pygame import Vector2 as v2
from render.sprites import SpriteStruct, static_sprites

class Body():
    """
    Static body with a position and animated sprites.
    """
    def __init__(self, game, r: tuple):
        """
        Spanws a Body.
        
        Input:
            r: pygame.Vector2(x,y)
        
        Outputs:
            Body
        """
        self.r = v2(r)
        self.v = (0, 0) # FIXME not use for now
        self.size = 20
        
        self.color = 'magenta'
        self.game = game # link to dt

        self.health = 1

        ## TODO add sprites data structure
        self.sprite_struct = SpriteStruct(static_sprites["default.png"])
    
    def get_sprite(self):
        """
        TODO Returns a Surface representing the current sprite to display.
        
        Inputs:
            <none>
        
        Outputs:
            Surface
        """
        #return self.sprite()
        return self.sprite_struct

    def draw(self,game): # draw object
        pg.draw.circle(game.window, self.color, self.r, 15)
