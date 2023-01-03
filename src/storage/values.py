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
    "M": Mob,
    "h": HealthPack5,
    "H": HealthPack25,
    "a": AmmoPack10,
    "A": AmmoPack50,
    "l": Light,
    "T": Tree,
    "t": DeadTree,
    
    # characters linked to None are forbidden special characters
    "E": None,  # used for exit
    " ": None,  # used for void
    }

values_destination = {
    Player: "players",
    Mob: "mobs",
    HealthPack25: "pickables",
    HealthPack5: "pickables",
    AmmoPack10: "pickables",
    AmmoPack50: "pickables",
    Light: "props",
    Tree: "props",
    DeadTree: "props",
}
