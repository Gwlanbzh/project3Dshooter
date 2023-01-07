from render.sprites import SpriteStruct
from bodys.pickables.pickable import Pickable

class Mine(Pickable):
    def __init__(self, game, r):
        super().__init__(game, r)
        self.dmg = 45

        self.model = "mine.png"
        self.dims = 50,50

    def update(self):
        picker = self.picker()
        if picker != None:
            picker.hurt(self.dmg)
            self.game.sound.play_sound("mine", self.game.world.players[0].r, self.r)
            return True
        return False
