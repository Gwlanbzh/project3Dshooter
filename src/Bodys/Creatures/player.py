from ..creature import Creature, Config
import pygame as pg
from pygame import Vector2 as v2
from math import cos, sin

class Player(Creature):
    """
    Controllable Creature with weapons.
    """
    def __init__(self,game ,r):
        """
        Spawns a Player.
        
        Inputs:
            game : Game
            r : tuple
        
        Outputs:
            Player
        """
        super().__init__(game,r)
        self.heal_recovery_time = 10000 # valeur arbitraire
        self.weapons = []
        self.ammo = 0 # may change
        self.color = 'blue'
        
        self.vorientation = 0  # used for looking up and down. positive => looking up
        # TODO add ammo data structure

    def update(self): # might be move into Creature or Body
        self.get_inputs()
        # heal
        # status, maybe buff / debuff
        # TODO : not logical to call self.get_inputs, call self.move() instead would be better
    
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
        V_sin = speed * sin(self.orientation) 
        V_cos = speed * cos(self.orientation) 
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
    
    def get_inputs(self):
        """
        Returns a force_vector based on the physical player's inputs.
        TODO maybye refactoring get inputs and mouvement call
        """
        keys = pg.key.get_pressed()
        if keys[pg.K_z]:
            self.move(2)
        if keys[pg.K_s]:
            self.move(3)
        if keys[pg.K_q]:
            self.move(1)
        if keys[pg.K_d]:
            self.move(4)
        if keys[pg.K_e]:
            self.rotate(-1)
        if keys[pg.K_a]:
            self.rotate(1)
        
        if keys[pg.K_o]:
            self.vorientation = max(self.vorientation + Config.PLAYER_VERT_ROT_SPEED, -Config.PLAYER_MAX_VERT_ROT)
        if keys[pg.K_k]:
            self.vorientation = min(self.vorientation - Config.PLAYER_VERT_ROT_SPEED, Config.PLAYER_MAX_VERT_ROT)
