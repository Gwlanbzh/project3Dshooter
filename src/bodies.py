import pygame as pg
import math
from pygame import Vector2 as v2
from weapons import *
from game import *
from config import *

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
        self.v = (0, 0) # FIXME not use for now
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
        super().__init__(r) 
        self.a = v2(0, 0) # FIXME not use
        self.orientation = 45 # arbitrary value for init
        self.game = game
        self
    
    def move(self, move: tuple, rotation):
        """
        TODO maybye refactoring get inputs and mouvement call
        Applies Newton's Second Principle then handles collisions
        with walls, props and mobs. FIXME text not right now
        
        Inputs:
            forces: list of pygame.Vector2 FIXME not use
            dt: strictly positive int FIXME not use
            move : tuple
            rotation : int -1 or 1
        
        Output:
            None
        """
        dt = self.game.delta_time
        speed = Config.PLAYER_V * dt
        V_sin = speed * math.sin(self.orientation) 
        V_cos = speed * math.cos(self.orientation) 
        x_move, y_move = move
        dx , dy = 0 , 0
        x , y = self.r
        dx += V_cos * y_move
        dy += V_sin * x_move

        self.orientation += rotation * Config.PLAYER_ROT_SPEED * dt

        self.r = x + dx, y + dy
        # collision stuff goes here

class Mob(Creature):
    def __init__(self, game,r):
        super().__init__(game,r)
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
        self.weapons = []
        self.heal_recovery_time = 10000 # valeur arbitraire
        self.weapons = []
        self.ammo = 0 # may change
        # TODO add ammo data structure

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
        TODO maybye refactoring get inputs and mouvement call
        """
        keys = pg.key.get_pressed()
        if keys[pg.K_z]:
            self.move((1, 1),0)
        if keys[pg.K_q]:
            self.move((1, -1), 0)
        if keys[pg.K_d]:
            self.move((-1, 1), 0)
        if keys[pg.K_s]:
            self.move((-1, -1), 0)
        if keys[pg.K_e]:
            self.move((0,0),-1)
        if keys[pg.K_a]:
            self.move((0,0),1)

        
