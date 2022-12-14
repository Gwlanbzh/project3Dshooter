from render.sprites import SpriteStruct, static_sprites
from bodys import Body


class Light(Body):
    def __init__(self, game, r):
        super().__init__(game, r)
        self.sprite_struct = SpriteStruct(static_sprites["street_light2.png"], 150, 40)
