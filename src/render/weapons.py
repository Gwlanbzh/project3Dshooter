import pygame as pg
from os import listdir
from config import *

# liste des noms des models, tuple (nom, scaling)
models = [
    ("weapon", 1),
    ("punch", 3),
    ("pistol", 4),
    ("rifle", 4),
    ("shotgun", 3),
    # superweapon = special case, see load_weaon function
]

def scale(img, ratio):
    size_x, size_y = img.get_size()
    scaled_img = pg.transform.scale(img, (size_x * ratio, size_y * ratio))
    return scaled_img

def load_model(model, scaling):
    path = Config.SPRITES_DIR + "weapons/"
    path_list = sorted([ path + model + "/" + name for name in listdir(path + model) ])
    return [scale(pg.image.load(p).convert_alpha(), scaling) for p in path_list]


def load_weapon():
    ids = dict()
    for model, scaling in models:
        ids[model] = load_model(model, scaling)    
    
    # specific case
    super_weapon_scaling = 4
    superweapons_images = {
        0 : [
                scale(pg.image.load(Config.SPRITES_DIR + f"weapons/superweapon/0.png").convert_alpha(), super_weapon_scaling),
                scale(pg.image.load(Config.SPRITES_DIR + f"weapons/superweapon/state1_firing.png").convert_alpha(), super_weapon_scaling)
            ],
        1 : [
                scale(pg.image.load(Config.SPRITES_DIR + f"weapons/superweapon/1.png").convert_alpha(), super_weapon_scaling),
                scale(pg.image.load(Config.SPRITES_DIR + f"weapons/superweapon/state2_firing.png").convert_alpha(), super_weapon_scaling)
            ]
    }
    
    # scalings images
    ids["superweapon"] = superweapons_images
    
    return ids
