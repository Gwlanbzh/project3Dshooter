from render.sprites import SpriteStruct
from bodys import Body

class Barrel(Body):
    def __init__(self):
        super().__init__(game, r)
        self.sprite_data = SpriteStruct("barrel.png", 50, 40)
