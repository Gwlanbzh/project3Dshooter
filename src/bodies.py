import pygame as pg
import math
from pygame import Vector2 as v2
from weapons import *
from game import *
from config import *

# TODO : create differents files for Player, Mob, and Body

class Body():
    """
    Static body with a position and animated sprites.
    """
    def __init__(self,game,r: tuple):
        """
        Spanws a Body.
        
        Input:
            r: tuple (x,y)
        
        Outputs:
            Body
        """
        self.r = r
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
        pg.draw.circle(game.window, self.color, self.r,15)


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

    def move(self,direction):
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

        x, y= self.r
        ## collision stuff goes here
        # world = self.game.world.map.map
        # if world[int((y + dy)//100)][int((x + dx)//100)] == 0:
        #     self.r = x + dx, y + dy
        
        x_permission, y_permission = self.not_colliding(dx, dy)
        if x_permission:
            x += dx
        if y_permission:
            y += dy 
        
        self.r = x, y

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
        pg.draw.circle(game.window, self.color, self.r,15)

class Mob(Creature):
    def __init__(self,game,r):
        """
        Spawns a Mob.
        
        Inputs:
            <none>
        
        Outputs:
            Mob
        """
        super().__init__(game,r)
        self.color = 'red' 

    def update(self):
        self.ia_command()
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
        self.heal_recovery_time = 10000 # valeur arbitraire
        self.weapons = []
        self.ammo = 0 # may change
        self.color = 'blue'
        # TODO add ammo data structure

    def update(self): # might be move into Creature or Body
        self.get_inputs()
        # heal
        # status, maybe buff / debuff
        # TODO : not logical to call self.get_inputs, call self.move() instead would be better
    
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

        
