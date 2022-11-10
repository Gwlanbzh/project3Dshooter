import pygame as pg
import math
from pygame import Vector2 as v2
from weapons import *
from game import *

class Body():
    """
    Static body with a position and animated sprites.
    """
    def __init__(self,r: tuple):
        """
        Spanws a Body.
        
        Input:
            r: tuple (x,y)
        
        Outputs:
            Body
        """
        self.r = r
        self.v = (0, 0)
        # self.game = game
        ## add sprites data structure
    
    def get_sprite(self):
        """
        Returns a Surface representing the current sprite to display.
        
        Inputs:
            <none>
        
        Outputs:
            Surface
        """
        pass

class Creature(Body):
    """
    Body with implemented physics, life etc.
    """
    def __init__(self, r : tuple, mass: int):
        """
        Spawns a Creature.
        
        Inputs:
            mass: int
        
        Output:
            Creature
        """
        super().__init__(r) 
        self.a = v2(0, 0)
        self.m = mass
        self.orientation = 0
    
    def move(self, move: tuple):
        """
        Applies Newton's Second Principle then handles collisions
        with walls, props and mobs.
        
        Inputs:
            forces: list of pygame.Vector2
            dt: strictly positive int
        
        Output:
            None
        """
        v = Config.V
        x_move, y_move = move
        x, y = self.r
        self.r = x + x_move*v, y + y_move * v
        
        # collision stuff goes here

class Mob(Creature):
    def __init__(self,r,mass):
        super().__init__(r,mass)
        """
        Spawns a Mob.
        
        Inputs:
            <none>
        
        Outputs:
            Mob
        """
        pass
    
    def ia_command(self):
        """
        Returns a force vector based on the move the IA choses.
        """
        pass

class Player(Creature):
    """
    Controllable Creature with weapons.
    """
    def __init__(self,game ,r,mass):
        """
        Spawns a Player.
        
        Inputs:
            <none>
        
        Outputs:
            Player
        """
        super().__init__(r,mass)
        self.weapons = []
        self.heal_recovery_time = 10000 # valeur arbitraire
        self.weapons = []
        self.ammo = 0 # may change
        self.game = game
        # add ammo data structure

    def update(self):
        self.get_inputs()

    def draw(self,game):
        pg.draw.line(game.window,'yellow', (self.r),
                     (self.r[0]+ 1600* math.cos(self.orientation),
                      self.r[1] + 1600 * math.sin(self.orientation)),2) 
        pg.draw.circle(game.window, 'blue', self.r,15)
    
    def get_inputs(self):
        """
        Returns a force_vector based on the physical player's inputs.
        """
        keys = pg.key.get_pressed()
        if keys[pg.K_z]:
            self.move((0, -1))
        if keys[pg.K_q]:
            self.move((-1, 0))
        if keys[pg.K_d]:
            self.move((1, 0))
        if keys[pg.K_s]:
            self.move((0, 1))

        
