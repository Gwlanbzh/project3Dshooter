import pygame as pg

def load_weapon():
    weapon_images = [
        pg.image.load(f"assets/sprites/weapon_debug/{i}.png").convert_alpha() for i in range(4)
    ]
    return weapon_images