from weapons import Weapon
from config import *
from math import pi

class Shotgun(Weapon):

    def __init__(self):
        super().__init__()
        self.delay = 400
        self.range = WALL_WIDTH * 5
        self.dmg = 10

    def hit_scan(self, pos, orientation, mob_list):
        super().hit_scan(pos, orientation, mob_list)
        super().hit_scan(pos, orientation - pi/4, mob_list)
        super().hit_scan(pos, orientation + pi/4, mob_list)

    