import pygame as pg
from config import *


def load_weapon():
    weapon_images = [
        pg.image.load(f"src/assets/sprites/weapon_debug/{i}.png").convert_alpha() for i in range(4)
    ]
    return weapon_images

def load_pistol():
    pistol_images = [
        pg.image.load(f"src/assets/sprites/weapons/pistol/{i}.png").convert_alpha() for i in range(6)
    ]
    return pistol_images

def load_shotgun():
    shotgun_images = [
        pg.image.load(Config.SPRITES_DIR + f"weapons/shotgun/{i}.png").convert_alpha() for i in range(4)
    ]
    shotgun_images = [ pg.transform.scale(img, (500, 500)) for img in shotgun_images ]

    return shotgun_images