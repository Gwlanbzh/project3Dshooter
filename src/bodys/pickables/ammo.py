from render.sprites import SpriteStruct, static_sprites
from bodys.pickables.pickable import Pickable


class AmmoPack20(Pickable):
    def __init__(self, game, r):
        super().__init__(game, r)
        
        self.supply_value = 20
        self.sprite_struct = SpriteStruct(static_sprites["ammo_20.png"], 25, 40)
    
    def update(self):
        picker = self.picker()
        if picker != None:
            print(picker.ammo)
            print("Supply!")
            picker.ammo += self.supply_value
            picker.ammo = min(picker.ammo, picker.max_ammo)
            print(picker.ammo)
            return True
        return False
