from weapons import Weapon
from config import *
from math import pi
import pygame as pg
from render import load_shotgun
from math import tau

class Shotgun(Weapon):

    def __init__(self):
        super().__init__()
        self.delay = 400
        self.range = WALL_WIDTH * 5
        self.dmg = 30

        self.dteta = 0.09 # 5 degrés en radians

        self.time_between_sprites = 100
        self.sprite = load_shotgun() # from render.weapons
        self.image_index = 0

        self.ammo_sound = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + "weapons/fire_shotgun.mp3"),
        ]
        
        self.no_ammo_sound = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + "weapons/dryfire_pistol.mp3"),
        ]

    def shoot(self, entity, mob_list):
        t = pg.time.get_ticks()
        if t - self.last_shot_time > self.delay: # 100 ms between shots 
            if entity.ammo > 2:
                self.last_shot_time = t

                entity.ammo = max(0, entity.ammo - 3)
                orien = entity.orientation

                self.hit_scan(entity.game.world.map.map, entity.r, orien, mob_list)
                self.hit_scan(entity.game.world.map.map, entity.r, (orien - self.dteta) % tau, mob_list)
                self.hit_scan(entity.game.world.map.map, entity.r, (orien + self.dteta) % tau, mob_list)
                self.play_sound()
            
            else:
                self.play_sound(no_ammo=True)

    def draw2d(self, window, r, teta):
        super().draw2d(window, r, teta)
        super().draw2d(window, r, (teta - self.dteta) % tau)
        super().draw2d(window, r, (teta + self.dteta) % tau)