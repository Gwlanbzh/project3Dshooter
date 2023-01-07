from bodys import *


##################
#
#  This file stores the character to class links, and 
#  a string used to determinate the array in which goes which class.
#  It is used by create_world in configlib.py.
#
##################

values = {
    "P": Player,
    "G": Grunt,
    "V": Heavy,
    "B": Boss,
    
    "h": HealthPack5,
    "H": HealthPack25,
    "a": AmmoPack10,
    "A": AmmoPack50,
    "m": Mine,
    
    "S": PickableShotgun,
    "R": PickableRifle,
    "M": PickableSuperWeapon,
    
    "l": Light,
    "T": Tree,
    "t": DeadTree,
    "b": Barrel,
    
    # characters linked to None are forbidden special characters
    "E": None,  # used for exit
    " ": None,  # used for void
    }

values_destination = {
    Player: "players",
    Mob: "mobs",
    Grunt: "mobs",
    Heavy: "mobs",
    Boss: "mobs",
    
    HealthPack25: "pickables",
    HealthPack5: "pickables",
    AmmoPack10: "pickables",
    AmmoPack50: "pickables",
    Mine: "pickables",
    
    PickableShotgun: "pickables",
    PickableRifle: "pickables",
    PickableSuperWeapon: "pickables",
    
    Light: "props",
    Tree: "props",
    DeadTree: "props",
    Barrel: "props",
}
