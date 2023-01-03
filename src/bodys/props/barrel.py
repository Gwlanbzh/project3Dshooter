from render.sprites import SpriteStruct
from bodys import Body

class Barrel(Body):
    def __init__(self, game, r):
        super().__init__(game, r)
        self.sprite_data = SpriteStruct("barrel.png", 80, 60)
