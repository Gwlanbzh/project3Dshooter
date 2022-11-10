import pygame as pg
from pygame import Vector2 as v2
from weapons import *

class Body():
    """
    Static body with a position and animated sprites.
    """
    def __init__(self, r: tuple):
        """
        Spanws a Body.
        
        Input:
            r: tuple
        
        Outputs:
            Body
        """
        self.r = v2(r)
        self.v = v2(0, 0)
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
    def __init__(self, mass: int):
        """
        Spawns a Creature.
        
        Inputs:
            mass: int
        
        Output:
            Creature
        """
        super().__init__(self)
        self.a = v2(0, 0)
        self.m = mass
        self.orientation = 0
    
    def _move(self, forces: list, dt: int):
        """
        Applies Newton's Second Principle then handles collisions
        with walls, props and mobs.
        
        Inputs:
            forces: list of pygame.Vector2
            dt: strictly positive int
        
        Output:
            None
        """
        self.a  = sum(forces, start=v2(0, 0)) / self.m
        self.v += self.a * dt
        self.r += self.v * dt
        
        # collision stuff goes here

class Mob(Creature):
    def __init__(self):
        super().__init__(self)
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
    def __init__(self):
        """
        Spawns a Player.
        
        Inputs:
            <none>
        
        Outputs:
            Player
        """
        super().__init__(self)
        weapons = []
        self.heal_recovery_time = 10000 # valeur arbitraire
        self.weapons = []
        self.ammo = 0 # may change
        # add ammo data structure
    
    def get_inputs(self):
        """
        Returns a force vector based on the physical player's inputs.
        """
        pass
        
