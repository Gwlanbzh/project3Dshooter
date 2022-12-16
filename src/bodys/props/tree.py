from render.sprites import SpriteStruct, static_sprites
from bodys import Body


class Tree(Body):
    def __init__(self, game, r):
        super().__init__(game, r)
        self.sprite_struct = SpriteStruct(static_sprites["tree.png"], 200, 200)

class DeadTree(Body):
    def __init__(self, game, r):
        super().__init__(game, r)
        self.sprite_struct = SpriteStruct(static_sprites["dead_tree.png"], 150, 100)
