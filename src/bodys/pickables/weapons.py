from weapons import Shotgun, Rifle, SuperWeapon
from render.sprites import SpriteStruct
from bodys.pickables.pickable import Pickable


class PickableShotgun(Pickable):
    def __init__(self, game, r):
        super().__init__(game, r)
        self.sprite_data = SpriteStruct("shotgun.png", 40, 150)
    
    def update(self):
        picker = self.picker()
        if picker != None:
            picker.weapons.append(Shotgun)
            return True
        return False

class PickableRifle(Pickable):
    def __init__(self, game, r):
        super().__init__(game, r)
        self.sprite_data = SpriteStruct("rifle.png", 40, 150)
    
    def update(self):
        picker = self.picker()
        if picker != None:
            picker.weapons.append(Rifle)
            return True
        return False
    

class PickableSuperWeapon(Pickable):
    def __init__(self, game, r):
        super().__init__(game, r)
        self.sprite_data = SpriteStruct("minigun.png", 40, 150)
    
    def update(self):
        picker = self.picker()
        if picker != None:
            picker.weapons.append(SuperWeapon)
            return True
        return False
