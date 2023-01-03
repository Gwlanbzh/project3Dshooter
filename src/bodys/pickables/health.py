from render.sprites import SpriteStruct
from bodys.pickables.pickable import Pickable


class HealthPack5(Pickable):
    def __init__(self, game, r):
        super().__init__(game, r)
        self.heal_value = 5
        self.sprite_data = SpriteStruct("health_5.png", 30, 30)
    
    def update(self):
        picker = self.picker()
        if picker != None:
            picker.health += self.heal_value
            picker.health = min(picker.health, picker.max_health)
            return True
        return False

class HealthPack25(HealthPack5):
    def __init__(self, game, r):
        super().__init__(game, r)
        self.heal_value = 25
        self.sprite_data = SpriteStruct("health_25.png", 50, 80)
