from weapons import Weapon
from config import *
from math import pi
import pygame as pg

class Shotgun(Weapon):

    def __init__(self):
        super().__init__()
        self.delay = 400
        self.range = WALL_WIDTH * 5
        self.dmg = 20

    def shoot(self, entity):
        t = pg.time.get_ticks()
        if t - self.last_shot_time > self.delay: # 100 ms between shots 
            if entity.ammo > 2:
                self.last_shot_time = t

                entity.ammo = max(0, entity.ammo - 3)

                mob_list = entity.game.world.mobs
                orien = entity.orientation

                self.hit_scan(entity.game.world.map.map, entity.r, orien, mob_list)
                self.hit_scan(entity.game.world.map.map, entity.r, orien - pi/6, mob_list)
                self.hit_scan(entity.game.world.map.map, entity.r, orien + pi/6, mob_list)
                self.play_sound()
            
            else:
                self.play_sound(no_ammo=True)

    #def hit_scan(self, pos, orientation, mob_list):
    #    super().hit_scan(pos, orientation, mob_list)
    #    super().hit_scan(pos, orientation - pi/4, mob_list)
    #    super().hit_scan(pos, orientation + pi/4, mob_list)