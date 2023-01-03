from render.sprites import SpriteStruct
from bodys import Body


class Light(Body):
    def __init__(self, game, r):
        super().__init__(game, r)
        self.sprite_data = SpriteStruct("street_light2.png", 150, 40)
