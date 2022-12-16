from render.sprites import SpriteStruct, static_sprites
from bodys.pickables.pickable import Pickable


class AmmoPack10(Pickable):
    def __init__(self, game, r):
        super().__init__(game, r)
        
        self.supply_value = 10
        self.sprite_struct = SpriteStruct(static_sprites["ammo_10.png"], 25, 25)
    
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
        self.sprite_struct = SpriteStruct(static_sprites["ammo_50.png"], 50, 80)
