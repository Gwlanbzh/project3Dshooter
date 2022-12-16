from render.sprites import SpriteStruct, static_sprites
from bodys.pickables.pickable import Pickable


class HealthPack25(Pickable):
    def __init__(self, game, r):
        super().__init__(game, r)
        self.heal_value = 25
        self.sprite_struct = SpriteStruct(static_sprites["health_25.png"], 25, 40)
    
    def update(self):
        picker = self.picker()
        if picker != None:
            picker.health += self.heal_value
            picker.health = min(picker.health, picker.max_health)
            return True
        return False
