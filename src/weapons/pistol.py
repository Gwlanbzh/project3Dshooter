from weapons import Weapon
from config import WALL_WIDTH

class Pistol(Weapon):
    def __init__(self):
        super().__init__()
        self.range = WALL_WIDTH * 10
        self.delay = 200
        self.dmg = 10