import pygame as pg
from config import *

def scale(image_list, ratio):
    scaled_images = []
    for img in image_list:
        size_x, size_y = img.get_size()
        new = pg.transform.scale(img, (size_x * ratio, size_y * ratio))
        scaled_images.append(new)
    return scaled_images

def load_weapon():
    weapon_images = [
        pg.image.load(f"src/assets/visual/sprites/weapon_debug/{i}.png").convert_alpha() for i in range(4)
    ]
    return weapon_images

def load_pistol():
    pistol_images = [
        pg.image.load(Config.SPRITES_DIR + f"weapons/pis/pis{i}.png").convert_alpha() for i in range(5)
    ]
    return scale(pistol_images, 4)
    

def load_shotgun():
    shotgun_images = [
        pg.image.load(Config.SPRITES_DIR + f"weapons/sht/sht{i}.png").convert_alpha() for i in range(8)
    ]
    return scale(shotgun_images, 2)

def load_rifle():
    rifle_images = [
        pg.image.load(Config.SPRITES_DIR + f"weapons/rifle/rifle{i}.png").convert_alpha() for i in range(4)
    ]

    return scale(rifle_images, 4)

def load_superweapon():
    superweapons_images = {
        0 : scale([pg.image.load(Config.SPRITES_DIR + f"weapons/superweapon/0.png").convert_alpha(), pg.image.load(Config.SPRITES_DIR + f"weapons/superweapon/state1_firing.png").convert_alpha() ], 2),
        1 : scale([pg.image.load(Config.SPRITES_DIR + f"weapons/superweapon/1.png").convert_alpha(), pg.image.load(Config.SPRITES_DIR + f"weapons/superweapon/state2_firing.png").convert_alpha()], 2)
    }

    return superweapons_images
