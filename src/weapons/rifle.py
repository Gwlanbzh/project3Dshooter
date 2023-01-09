from weapons import Weapon
import pygame as pg
from config import *

class Rifle(Weapon):
    def __init__(self):
        super().__init__()
        
        self.range = WALL_WIDTH * 15
        self.dmg = 75
        self.delay = 250  # ms
        self.time_between_sprites = 90

        self.model = "rifle"
