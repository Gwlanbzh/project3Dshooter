from weapons import Pistol, Shotgun, Rifle, SuperWeapon
from render.sprites import SpriteStruct
from bodys.pickables.pickable import Pickable


class PickableWeapon(Pickable):
    def __init__(self, game, r):
        super().__init__(game, r)
        
        self.provided_weapon = Pistol()
    
    def update(self):
        picker = self.picker()
        if picker != None:
            picker.weapons.append(self.provided_weapon)
            return True
        return False


class PickableShotgun(PickableWeapon):
    def __init__(self, game, r):
        super().__init__(game, r)
        
        self.provided_weapon = Shotgun()
        self.sprite_data = SpriteStruct("shotgun.png", 40, 150)
    

class PickableRifle(PickableWeapon):
    def __init__(self, game, r):
        super().__init__(game, r)
        
        self.provided_weapon = Rifle()
        self.sprite_data = SpriteStruct("rifle.png", 40, 150)
    

class PickableSuperWeapon(PickableWeapon):
    def __init__(self, game, r):
        super().__init__(game, r)
        
        self.provided_weapon = SuperWeapon()
        self.sprite_data = SpriteStruct("minigun.png", 40, 150)
