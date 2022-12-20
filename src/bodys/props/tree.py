from render.sprites import SpriteStruct
from bodys import Body


class Tree(Body):
    def __init__(self, game, r):
        super().__init__(game, r)
        self.sprite_data = SpriteStruct("tree.png", 200, 200)

class DeadTree(Body):
    def __init__(self, game, r):
        super().__init__(game, r)
        self.sprite_data = SpriteStruct("dead_tree.png", 150, 100)
