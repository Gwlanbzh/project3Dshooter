from pygame import Vector2 as v2
import pygame as pg
import math
from bodys import Body
from config import *

class Creature(Body):
    """
    Body with implemented physics, life etc.
    """
    def __init__(self, game, r : tuple):
        """
        Spawns a Creature.
        
        Inputs:
            game: Game
            r : tuple
        
        Output:
            Creature
        """
        super().__init__(game,r) 
        self.a = v2(0, 0) # FIXME not use
        self.orientation = 0 # arbitrary value for init
        self.health = "int" # TODO
        self.size = 15


    def in_wall(self, x, y):
        world = self.game.world.map.map
        return world[int((y)//100)][int((x)//100)][0] != 0

    def not_colliding(self, dx, dy):
        """
        return a tuple :
            first element is x_permission for moving
            second element is y_permission for moving
        """
        x, y = self.r
        return (
            not (self.in_wall(x + 5 + dx, y) or self.in_wall(x - 5 + dx, y)),
            not (self.in_wall(x, y + 5 + dy) or self.in_wall(x, y - 5 + dy))
        )

    def rotate(self,direction):
        dt = self.game.delta_time # may be change to a const but there might be a use for it in future when framerate will be unsure
        self.orientation -= direction * Config.PLAYER_ROT_SPEED * dt
        self.orientation %= math.tau


    def draw(self,game): # might be move into Creature or Body
        traylenght = 100
        pg.draw.line(game.window,'yellow', (self.r),
                     (self.r[0]+ traylenght* math.cos(self.orientation),
                      self.r[1] + traylenght* math.sin(self.orientation)),2) 
        pg.draw.circle(game.window, self.color, self.r, self.size)