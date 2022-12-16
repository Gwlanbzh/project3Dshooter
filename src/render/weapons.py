import pygame as pg
from config import *


def load_weapon():
    weapon_images = [
        pg.image.load(Config.SPRITES_DIR + f"weapon_debug/{i}.png").convert_alpha() for i in range(4)
    ]
    return weapon_images

def load_pistol():
    pistol_images = [
        pg.image.load(Config.SPRITES_DIR + f"weapons/pistol/{i}.png").convert_alpha() for i in range(6)
    ]
    return pistol_images