from render.sprites import SpriteStruct
from bodys import Body


class Light(Body):
    def __init__(self, game, r):
        super().__init__(game, r)

        self.model = "street_light2.png"
        self.dims = 40, 150
