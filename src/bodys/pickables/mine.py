from render.sprites import SpriteStruct
from bodys.pickables.pickable import Pickable

class Mine(Pickable):
    def __init__(self, game, r):
        super().__init__(game, r)
        self.damage = 45

        self.model = "mine.png"
        self.dims = 50,50

    def update(self):
        picker = self.picker()
        if picker != None:
            picker.health -= self.damage
            picker.health = min(picker.health, picker.max_health)
            return True
        return False
