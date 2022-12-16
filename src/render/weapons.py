import pygame as pg

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