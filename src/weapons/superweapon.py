import pygame as pg
from weapons.weapon import Weapon
from config import *
from render import load_superweapon

class SuperWeapon(Weapon):
    def __init__(self):
        super().__init__(self)

        self.range = WALL_WIDTH * 15
        self.dmg = 40
        self.delay = 100 # ms
        self.time_between_sprites = 50
        self.image_index = 0

        self.ammo_sound = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + "weapons/fire_pistol.mp3"),
        ]

        self.no_ammo_sound = [ 
            pg.mixer.Sound(Config.SOUNDS_FOLDER + "weapons/dryfire_rifle.mp3"),
        ]

        self.sprite = load_superweapon()