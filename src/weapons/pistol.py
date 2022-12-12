from weapons import Weapon

class Pistol(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Pistol"