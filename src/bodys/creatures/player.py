import pygame as pg
from pygame import Vector2 as v2
from math import cos, sin, hypot
from config import Config
from bodys import Creature
from weapons import *
from math import tau


class Player(Creature):
    """
    Controllable Creature with weapons.
    """
    def __init__(self, game, r):
        """
        Spawns a Player.
        
        Inputs:
            game : Game
            r : tuple
        
        Outputs:
            Player
        """
        super().__init__(game, r)
        
        self.v = v2(0, 0)
        
        self.size = 40
        self.color = 'blue'
        self.model = "player"

        self.orientation = -tau/4
        self.vorientation = 0
        self.spawn_pos = r
        # self.health
        self.visual_health = self.health

        # weapons attributes
        self.current_weapon = Pistol()
        self.weapons = [Punch, Pistol]
        self.ammo = 20  # may change to dict ?
        
        self.max_ammo = 100

        pg.event.set_grab(True)
        pg.mouse.set_visible(False)


    def update(self):  # might be move into Creature or Body
        # heal
        # status, maybe buff / debuff
        pass
    
    
    def get_inputs(self,event):
        """
        """
        keys = pg.key.get_pressed()


        if not self.game.is_paused:
            moves = set()
            if keys[pg.K_z]:
                moves.add(2)
            if keys[pg.K_s]:
                moves.add(3)
            if keys[pg.K_q]:
                moves.add(1)
            if keys[pg.K_d]:
                moves.add(4)
        
            # sera géré par la souris plus tard
            if keys[pg.K_e]:
                self.rotate(-1)
            if keys[pg.K_a]:
                self.rotate(1)

            if keys[pg.K_o]:
                self.vorientation = min(self.vorientation + Config.PLAYER_VERT_ROT_SPEED, Config.PLAYER_MAX_VERT_ROT)
            if keys[pg.K_k]:
                self.vorientation = max(self.vorientation - Config.PLAYER_VERT_ROT_SPEED, -Config.PLAYER_MAX_VERT_ROT)

            for event in event:
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_g:
                        self.health -= 10
                    if event.key == pg.K_h:
                        self.health += 10
                    if event.key == pg.K_p:
                        self.game.hud.toggle()
                    if event.key == pg.K_ESCAPE:
                        self.game.hud.menu_esc_is_toggle = True
                        self.game.is_paused = True

                    if event.key == pg.K_1 and Punch in self.weapons:
                        self.current_weapon = Punch()
                    if event.key == pg.K_2 and Pistol in self.weapons:
                        self.current_weapon = Pistol()
                    if event.key == pg.K_3 and Shotgun in self.weapons:
                        self.current_weapon = Shotgun()
                    if event.key == pg.K_4 and Rifle in self.weapons:
                        self.current_weapon = Rifle()
                    if event.key == pg.K_LEFTPAREN and SuperWeapon in self.weapons:
                        self.current_weapon = SuperWeapon()
            
            # Mouse events
            left_click, _, _ = pg.mouse.get_pressed()
            if left_click:
                mob_list = self.game.world.mobs + self.game.world.props
                self.current_weapon.shoot(self, mob_list)
        
            mouse_delta_pos = pg.mouse.get_rel()
            x, y = mouse_delta_pos
            self.vorientation = self.vorientation - y * Config.PLAYER_VERT_ROT_SPEED
            self.vorientation = max(min(self.vorientation, Config.PLAYER_MAX_VERT_ROT), -Config.PLAYER_MAX_VERT_ROT)
            self.rotate(-x, sensitivity=Config.PLAYER_MOUSE_ROT_SPEED)
        
        # Weapon selection
        
            self.move(moves) 
        else:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.game.hud.menu_esc_is_toggle = False
                        self.game.is_paused = False

    
    def move(self,moves):
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
        V_sin = sin(self.orientation) 
        V_cos = cos(self.orientation) 

        fx = 0
        fy = 0
        if 1 in moves:
            # gauche
            fx += V_sin 
            fy += -V_cos 
        if 2 in moves:
            # devant
            fx += V_cos 
            fy += V_sin 
        if 3 in moves:
            # derrière
            fx += -V_cos 
            fy += -V_sin 
        if 4 in moves:
            # droite
            fx += -V_sin 
            fy += V_cos
        
        if fx != 0 or fy != 0:
            k = speed * (1/hypot(fx, fy))
            fx = k * fx
            fy = k * fy
        ## collision stuff goes here
        # world = self.game.world.map.map
        # if world[int((y + dy)//100)][int((x + dx)//100)] == 0:
        #     self.r = x + dx, y + dy
        
        forces = [
            v2(fx, fy),     # movement force
            - Config.PLAYER_FRICTION * self.v  # friction force
        ]
        
        a = sum(forces, start=v2(0, 0))
        self.v += a

        x_permission, y_permission = self.not_colliding(self.v.x, self.v.y)
        if x_permission:
            self.r.x += self.v.x
        if y_permission:
            self.r.y += self.v.y


    def rotate(self, direction, sensitivity=Config.PLAYER_ROT_SPEED):
        dt = self.game.delta_time # may be change to a const but there might be a use for it in future when framerate will be unsure
        self.orientation -= direction * sensitivity * dt
        self.orientation %= tau

