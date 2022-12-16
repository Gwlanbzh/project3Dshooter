from bodys import *

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
