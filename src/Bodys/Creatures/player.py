from ..creature import Creature, Config
import pygame as pg

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
            self.vorientation = min(self.vorientation + Config.PLAYER_VERT_ROT_SPEED, Config.PLAYER_MAX_VERT_ROT)
        if keys[pg.K_l]:
            self.vorientation = max(self.vorientation - Config.PLAYER_VERT_ROT_SPEED, -Config.PLAYER_MAX_VERT_ROT)
