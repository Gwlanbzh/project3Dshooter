from weapons import Weapon
import pygame as pg
from config import *

class Punch(Weapon):
    def __init__(self):
        super().__init__()
        
        self.dmg = 40
        self.range = 1 * WALL_WIDTH
        
        self.state = 0
        self.time_between_sprites = 80
        
        self.model = "punch"
        self.key = 1 

    def draw(self, Ressources, window):
        self.update_image(Ressources)

        sprites = Ressources.weapon_sprites[self.model]

        width, height = sprites[self.image_index].get_size()
        top_left = (
            (Config.RES_X) - (width),
            Config.RES_Y - height
        )
        window.blit(sprites[self.image_index], top_left)
    
    def shoot(self, entity, mob_list):
        """
        check if a mob is touch on click and act in consequence.
        """
        t = pg.time.get_ticks()
        if t - self.last_shot_time > self.delay:  # 100 ms between shots 
            self.last_shot_time = t
            self.hit_scan(entity.game.world.map.grid, entity.r, entity.orientation, mob_list)
            self.play_sound(entity)
