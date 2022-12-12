from render.sprites import SpriteStruct, static_sprites
from bodys import Body


class Light(Body):
    def __init__(self, game, r):
        super().__init__(game, r)
        self.spriteStruct = SpriteStruct(static_sprites["light.png"], 150, 75)
