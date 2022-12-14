from weapons import Weapon
from config import *

class Punch(Weapon):

    def __init__(self):
        self.dmg = 10
        self.range = 0.5 * WALL_WIDTH
