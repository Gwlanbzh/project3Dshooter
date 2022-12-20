from render.sprites import SpriteStruct
from bodys.pickables.pickable import Pickable


class AmmoPack10(Pickable):
    def __init__(self, game, r):
        super().__init__(game, r)
        
        self.supply_value = 10
        self.sprite_data = SpriteStruct("ammo_10.png", 25, 20)
    
    def update(self):
        picker = self.picker()
        if picker != None:
            picker.ammo += self.supply_value
            picker.ammo = min(picker.ammo, picker.max_ammo)
            return True
        return False

class AmmoPack50(AmmoPack10):
    def __init__(self, game, r):
        super().__init__(game, r)
        
        self.supply_value = 50
        self.sprite_data = SpriteStruct("ammo_50.png", 50, 80)
