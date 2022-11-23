from pygame import Vector2 as v2
import pygame as pg
import math
from body import Body
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

    def move(self, direction):
        """
        TODO maybye refactoring get inputs and mouvement call
        Applies Newton's Second Principle then handles collisions
        with walls, props and mobs. FIXME text not true now
        direction meaning
          2
        1 + 4
          3
        
        Inputs:
            direction
        
        Output:
            Alter Creature position
        """

        dt = self.game.delta_time # may be change to a const but there might be a use for it in future when framerate will be unsure
        speed = Config.PLAYER_V * dt 
        V_sin = speed * math.sin(self.orientation) 
        V_cos = speed * math.cos(self.orientation) 
        if direction == 1:
            dx = V_sin 
            dy = -V_cos 
        if direction == 2:
            dx = V_cos 
            dy = V_sin 
        if direction == 3:
            dx = -V_cos 
            dy = -V_sin 
        if direction == 4:
            dx = -V_sin 
            dy = V_cos

        x, y = self.r
        ## collision stuff goes here
        # world = self.game.world.map.map
        # if world[int((y + dy)//100)][int((x + dx)//100)] == 0:
        #     self.r = x + dx, y + dy
        
        x_permission, y_permission = self.not_colliding(dx, dy)
        if x_permission:
            x += dx
        if y_permission:
            y += dy 
        
        self.r = v2(x, y)

    def in_wall(self, x, y):
        world = self.game.world.map.map
        return world[int((y)//100)][int((x)//100)] != 0

    def not_colliding(self, dx, dy):
        """
        return a tuple :
            first element is x_permission for moving
            second element is y_permission for moving
        """
        x, y = self.r
        return (
            not (self.in_wall(x + self.size + dx, y) or self.in_wall(x - self.size + dx, y)),
            not (self.in_wall(x, y + self.size + dy) or self.in_wall(x, y - self.size + dy))
        )

    def rotate(self, direction):
        dt = self.game.delta_time # may be change to a const but there might be a use for it in future when framerate will be unsure
        self.orientation -= direction * Config.PLAYER_ROT_SPEED * dt
        self.orientation %= math.tau


    def draw(self, game): # might be move into Creature or Body
        traylenght = 100
        pg.draw.line(game.window,'yellow', (self.r),
                     (self.r[0]+ traylenght* math.cos(self.orientation),
                      self.r[1] + traylenght* math.sin(self.orientation)),2) 
        pg.draw.circle(game.window, self.color, self.r,15)
