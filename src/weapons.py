import pygame as pg
from pygame import Vector2 as v2

class Weapon():
    def __init__(self):
        self.dmg = 0
        self.freq = 1
        self.range = 0.
        # add sprite
    
    def fire_scan(self):
        pass

class Pistol(Weapon):
    def __init__(self):
        super().__init__(self)