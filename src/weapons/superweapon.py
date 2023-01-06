import pygame as pg
from weapons.weapon import Weapon
from config import *
from render import load_superweapon

class SuperWeapon(Weapon):
    def __init__(self):
        super().__init__()

        self.range = WALL_WIDTH * 15
        self.dmg = 40
        self.delay = 100 # ms
        self.time_between_sprites = 50
        self.image_index = 0

        self.state = 0

        self.model = "superweapon"

        self.sprite = load_superweapon()

    def shoot(self, entity, mob_list):
        t = pg.time.get_ticks()
        if t - self.last_shot_time > self.delay: # 100 ms between shots 
            if entity.ammo > 0:
                self.last_shot_time = t
                entity.ammo = max(0, entity.ammo - 1)
                self.hit_scan(entity.game.world.map.grid, entity.r, entity.orientation, mob_list)
                self.play_sound(entity.game, entity.r)
            else:
                self.play_sound(entity.game, entity.r, no_ammo=True)
            self.state = int(not self.state)

    def draw(self, window):
        self.update_image()
        width, height = self.sprite[self.state][self.image_index].get_size()
        top_left = (
            (Config.RES_X / 2) - (width / 2),
            Config.RES_Y - height
        )
        window.blit(self.sprite[self.state][self.image_index], top_left)
    
    def update_image(self):
        i = int((pg.time.get_ticks() - self.last_shot_time) / self.time_between_sprites)
        self.image_index = i if i < len(self.sprite[0]) else 0