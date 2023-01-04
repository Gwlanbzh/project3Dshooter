from render.sprites import SpriteStruct
from bodys import Body


class Tree(Body):
    def __init__(self, game, r):
        super().__init__(game, r)
        self.model = "tree.png"
        self.dims = 200, 200
class DeadTree(Body):
    def __init__(self, game, r):
        super().__init__(game, r)
        self.model = "dead_tree.png"
        self.dims = 100, 150
