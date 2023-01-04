import pygame as pg 
from pygame import Vector2 as v2
from render.sprites import SpriteStruct
from config import Config

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
        self.model = "putin.png"
        self.dims = 100, 100

        self.sprite_data = {
            "alive" : [SpriteStruct("default.png")],
            }
    
    def get_sprite(self):
        """
        TODO Returns a Surface representing the current sprite to display.
        
        Inputs:
            <none>
        
        Outputs:
            Surface
        """
        #return self.sprite()
        # si mort : en fonction de la date de mort retourner une sprite spécifique
        # sinon : afficher en fonction du dernier tir qui a touché

        # state = 
        # frame = 0

        # data = self.game.world.ressources.animated_sprites[self.model][state][frame]
        data = self.game.world.ressources.static_sprites[self.model]
        w, h = self.dims

        return SpriteStruct(data, h, w)

    def draw(self, game): # might be move into Creature or Body
        p_pos = self.game.world.players[0].r
        x0, y0 = Config.WINDOW_SIZE
        x0, y0 = x0/2, y0/2

        render_pos = self.r - p_pos
        render_pos.x += x0
        render_pos.y += y0
        
        # rond
        pg.draw.circle(game.window, self.color, render_pos, self.size)
        
        # retour pour les classes qui héritent de body
        return render_pos

    @property
    def map_pos(self):
        return int(self.r.x//100), int(self.r.y//100)
    
    def hurt(self, damages):
        pass
