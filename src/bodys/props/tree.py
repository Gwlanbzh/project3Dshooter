from render.sprites import static_sprites
from bodys import Body

class Tree(Body):
    def __init__(self, game, r):
        super().__init__(game, r)
        self.sprite = static_sprites["tree.png"]
