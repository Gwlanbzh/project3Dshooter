from storage import *
from bodys import *

world = StorableWorld(
    props=[
        (Light, (150, 150)),
        (Light, (1150, 150)),
        (Light, (150, 850)),
        (Light, (1150, 850)),
        (Tree, (650, 650)),
        ],
    
    pickables=[
        (HealthPack25, (450, 950)),
        (HealthPack25, (550, 950)),
        (HealthPack25, (650, 950)),
        (HealthPack25, (750, 950)),
        (HealthPack25, (850, 950)),
        (AmmoPack20, (450, 150)),
        (AmmoPack20, (550, 150)),
        (AmmoPack20, (650, 150)),
        (AmmoPack20, (750, 150)),
        (AmmoPack20, (850, 150)),
        ],
    
    mobs=[
        (Mob, (650, 350)),
        (Mob, (650, 750)),
        (Mob, (1150, 550)),
        ],
    
    players=[
        (Player, (150, 550)),
        ],
    
    grid=[
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
        [1, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 1, ],
        [1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, ],
        [1, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 1, ],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
        ],
    )

print(world.write("assets/maps/test_map.bin"))

print(load("assets/maps/test_map.bin")) #as f:
    #print(load(f.read()))
