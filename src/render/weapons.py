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
        pg.image.load(Config.SPRITES_DIR + f"weapons/shotgun/{i}.png").convert_alpha() for i in range(4)
    ]
    shotgun_images = [ pg.transform.scale(img, (500, 500)) for img in shotgun_images ]

    return shotgun_images