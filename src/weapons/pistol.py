from weapons import Weapon
from render import load_pistol
from config import WALL_WIDTH

class Pistol(Weapon):
    def __init__(self):
        super().__init__()
        
        self.dmg = 30
        self.delay = 500 # en ms
        self.range = 10 * WALL_WIDTH

        self.last_shot_time = - self.delay # moment at which the last shot was fired
                                           # - self.delay to avoid animation at init of the game
        
        self.time_between_sprites = 50
        self.sprite = load_pistol() # from render.weapons
        self.image_index = 0