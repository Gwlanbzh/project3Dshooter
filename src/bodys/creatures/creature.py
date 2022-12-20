from pygame import Vector2 as v2
import pygame as pg
from math import *
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
        super().__init__(game, r) 
        self.a = v2(0, 0) # FIXME not use
        self.orientation = 0 # arbitrary value for init
        self.health = 100
        self.max_health = 200
    
    def in_wall(self, pos):
        x , y = pos
        world = self.game.world.map.grid
        return world[int((y)//100)][int((x)//100)] != 0

    def not_colliding(self, dx, dy):
        """
        return a tuple :
            first element is x_permission for moving
            second element is y_permission for moving
        """
        x, y = self.r
        # respectivly signe of dx and dy 
        sdx = (copysign(1,dx))
        sdy = (copysign(1,dy))
        sqrt2 = 0.80
        #     2
        #   1   3
        # 4       6
        #   7   9
        #     8
        posx13  = (x + sqrt2*(sdx*self.size) , y + sqrt2*(sdx*self.size))
        posx79  = (x + sqrt2*(sdx*self.size) , y - sqrt2*(sdx*self.size))
        posy13  = (x + sqrt2*(sdy*self.size) , y + sqrt2*(sdy*self.size))
        posy79  = (x - sqrt2*(sdy*self.size) , y + sqrt2*(sdy*self.size))
        posx46 = (x + sdx*(self.size+5) , y) 
        posy28 = (x , y + sdy*(self.size+5))


        # print (dy,dx,sdy,sdx)
        pg.draw.line(self.game.window,'purple', (self.r),(posx46),10) 
        pg.draw.line(self.game.window,'purple', (self.r),(posy28),10) 
        pg.draw.line(self.game.window,'orange', (self.r),(posx13),5) 
        pg.draw.line(self.game.window,'pink', (self.r),(posx79),5) 
        pg.draw.line(self.game.window,'brown', (self.r),(posy13),5) 
        pg.draw.line(self.game.window,'cyan', (self.r),(posx79),5) 


        return (
            not (self.in_wall(posx46) 
                or self.in_wall(posx13) 
                or self.in_wall(posx79)
                ),
            not (self.in_wall(posy28) 
                or self.in_wall(posy13) 
                or self.in_wall(posy79)
                )
        )

    def rotate(self, direction, sensitivity=Config.PLAYER_ROT_SPEED):
        dt = self.game.delta_time # may be change to a const but there might be a use for it in future when framerate will be unsure
        self.orientation -= direction * sensitivity * dt
        self.orientation %= tau


    def draw(self, game): # might be move into Creature or Body
        traylenght = 100
        pg.draw.line(game.window,'yellow', (self.r),
                     (self.r[0]+ traylenght * cos(self.orientation),
                      self.r[1] + traylenght * sin(self.orientation)),2) 
        pg.draw.circle(game.window, self.color, self.r,15)
