from render.sprites import SpriteStruct
from bodys.creatures.creature import Creature
from math import pi, cos, sin, atan2,hypot, tau, atan
from pygame import Vector2 as v2
from render.ray import Ray
from weapons import *
import random
import pygame as pg
from config import *

class Mob(Creature):
    def __init__(self, game, r):
        """
        Spawns a Mob.

        color : color of the mob when draw2d is 1
        has_seen_player : bool : trigger the folow player
        fov : angle : fov of the mob for player_in_fov()
        can_move_delay : int : delay for the mob to move after a shot
        frequence : flaot : frequence where the mob will shoot the ayer when in range. the lower the fewer. 
        current_weapon : Weapon : weapon use by the mob
        range : int : range of the mob. 
        ammo : int : default ammo capacity of the mob  
        
        Inputs:
            r : positon du mob
        
        Outputs:
            Mob
        """
        super().__init__(game, r)
        self.color = 'red' 
        self.speed = 0.06 # small value because of the * dt
        self.has_seen_player = False
        self.fov = pi/2
        self.can_move_delay = 0
        self.frequence = 0.004 
        self.current_weapon = Pistol()
        self.range = self.current_weapon.range
        self.ammo = 10000
        self.newt_pos = None
        self.time_from_last_path_finding = None
        self.next_pos = None

    def update(self):
        self.ia_command()
        if self.is_dead():
            self.color = "black"
    
    def ia_command(self):
        """
        Behavior of the mob
        do nothing if dead
        do nothing if he has never seen the player
        do random attack when at range
        do not approch the player more than 0.2*range of is range 
        loose trigger when too far from player
        """
        player = self.game.world.players[0]
        mob_view_player = self.mob_view_player()
        dist_with_player = self.dist_with_player()
        if not self.is_dead() :
            if not self.has_seen_player and mob_view_player and dist_with_player < 20 * self.range:
                self.has_seen_player = True
            if self.has_seen_player:
                if not mob_view_player and dist_with_player > 15*WALL_WIDTH:
                    self.has_seen_player = False
                    self.walking = False
                elif 0.3 * self.range < dist_with_player < 0.8 * self.range and mob_view_player:
                    rand = random.random()
                    if rand < self.frequence:
                        self.walking = False 
                        self.can_move_delay = 30
                        direction = v2(player.r - self.r)
                        self.orientation = atan2(direction.y,direction.x)
                        self.current_weapon.shoot(self, self.game.world.players)
                    elif self.can_move_delay < 1 and dist_with_player > 0.2 * self.range or not mob_view_player:
                            self.movement()
                            self.walking = True
                    else:
                        self.walking = False
                        direction = v2(player.r - self.r)
                        self.orientation = atan2(direction.y,direction.x)
                        self.current_weapon.shoot(self, self.game.world.players)
                elif self.can_move_delay < 1 and dist_with_player > 0.2 * self.range or not mob_view_player:
                        self.movement()
                        self.walking = True
                else:
                    self.walking = False
                    direction = v2(player.r - self.r)
                    self.orientation = atan2(direction.y,direction.x)
                    self.current_weapon.shoot(self, self.game.world.players)
            self.can_move_delay -= 1


    def movement(self):
        """
        move the mob toward the player
        """
        # Get player and self position
        x,y = self.r
        target_pos = self.game.world.players[0].r

        mob_map_pos = self.map_pos
        player_map_pos = self.game.world.players[0].map_pos
        current_time = pg.time.get_ticks()

        if self.time_from_last_path_finding == None or self.next_pos == None:
            self.next_pos = self.game.path_finding.Astar(mob_map_pos, player_map_pos)
            self.time_from_last_path_finding = pg.time.get_ticks()
        if current_time - self.time_from_last_path_finding > 4000 or self.next_pos == self.map_pos:
            self.next_pos = self.game.path_finding.Astar(mob_map_pos, player_map_pos)
            self.time_from_last_path_finding = pg.time.get_ticks()

        if self.next_pos != None and self.next_pos not in self.game.world.mobs_position:
            next_pos_x, next_pos_y = self.next_pos
            next_pos_x += 0.5
            next_pos_y += 0.5
            next_pos_y *= 100
            next_pos_x *= 100

            # compute nex postion
            angle = atan2(next_pos_y - y, next_pos_x - x)
            dx = cos(angle) * self.speed * self.game.delta_time
            dy = sin(angle) * self.speed * self.game.delta_time
            self.orientation = angle % tau

            # check colision with not_colliding's Creature methode
            x_permission, y_permission = self.not_colliding(dx, dy)
            if x_permission:
                x += dx
            if y_permission:
                y += dy 
            self.r = v2(x, y)


    def mob_view_player(self):
        """
        Check if the player is visible from the mob
        """
        player = self.game.world.players[0]

        # test mur
        direction = v2(player.r - self.r)
        rayon = Ray(self.r, direction, self.game.world.map.grid)

        if rayon.distance > self.dist_with_player() < self.range * 15:
            # if self.player_in_fov():
            return True

    def player_in_fov(self): 
        """
        Deprecated
        """
        # Info Player
        player = self.game.world.players[0]
        x_player,y_player = player.r.x, player.r.y

        # Info Mob
        mob_x,mob_y = self.r.x,self.r.y

        # if player in FOV of mob
        angle_mob_player = atan2(y_player - mob_y,x_player - mob_x)
        if self.orientation - pi/4 < angle_mob_player < self.orientation + pi/4:
            self.has_seen_player = True


    def dist_with_player(self):
        player = self.game.world.players[0]
        diff = player.r - self.r
        dist = hypot(diff.x, diff.y)
        return dist


class Grunt(Mob):
    def __init__(self, game, r):
        super().__init__(game,r)
        
        self.size = 27
        self.health = 100
        self.current_weapon = Pistol()        # TODO add pistol
        # TODO implement dynamic sprites

        self.model = "grunt"
        self.dims = 70, 130

class Heavy(Mob):
    def __init__(self, game, r):
        super().__init__(game,r)
        
        self.size = 30
        self.health = 400
        self.current_weapon = Rifle()        # TODO add pistol
        # TODO implement dynamic sprites

        self.model = "heavy"
        self.dims = 70, 130

class Boss(Mob):
    def __init__(self, game, r):
        super().__init__(game,r)
        
        self.size = 35
        self.health = 2000
        self.current_weapon = SuperWeapon()        # TODO add pistol
        # TODO implement dynamic sprites

        self.model = "boss"
        self.dims = 90, 175
