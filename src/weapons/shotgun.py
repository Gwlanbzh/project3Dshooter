from weapons import Weapon
from config import *
import pygame as pg
from math import tau

class Shotgun(Weapon):
    def __init__(self):
        super().__init__()
        self.delay = 600
        self.range = WALL_WIDTH * 5
        self.dmg = 40

        self.dteta = 0.09 # 5 degrés en radians

        self.time_between_sprites = 75
        self.image_index = 0

        self.model = "shotgun"

    def shoot(self, entity, mob_list):
        t = pg.time.get_ticks()
        if t - self.last_shot_time > self.delay: # 100 ms between shots 
            if entity.ammo > 2:
                self.last_shot_time = t

                entity.ammo = max(0, entity.ammo - 3)
                orien = entity.orientation

                self.hit_scan(entity.game.world.map.grid, entity.r, orien, mob_list)
                self.hit_scan(entity.game.world.map.grid, entity.r, (orien - self.dteta) % tau, mob_list)
                self.hit_scan(entity.game.world.map.grid, entity.r, (orien + self.dteta) % tau, mob_list)
                self.play_sound(entity)
            
            else:
                self.play_sound(entity, no_ammo=True)

    def draw2d(self, window, r, teta):
        super().draw2d(window, r, teta)
        super().draw2d(window, r, (teta - self.dteta) % tau)
        super().draw2d(window, r, (teta + self.dteta) % tau)
