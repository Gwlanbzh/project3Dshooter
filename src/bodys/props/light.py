from render.sprites import static_sprites
from bodys import Body

class Light(Body):
    def __init__(self, game, r):
        super().__init__(game, r)
        self.sprite = static_sprites["light.png"]
