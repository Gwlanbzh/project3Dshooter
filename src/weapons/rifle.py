from weapons import Weapon
import pygame as pg
from config import *
from render import load_rifle

class Rifle(Weapon):

    def __init__(self):
        super().__init__()
        
        self.range = WALL_WIDTH * 15
        self.dmg = 50
        self.delay = 500 # ms
        self.time_between_sprites = 90

        self.ammo_sound = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + "weapons/rifle-firing.mp3"),
        ]

        self.no_ammo_sound = [ 
            pg.mixer.Sound(Config.SOUNDS_FOLDER + "weapons/dryfire_pistol.mp3"),
        ]

        self.sprite = load_rifle()
