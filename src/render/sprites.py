from dataclasses import dataclass
import pygame as pg
from render.textures import load_texture
from render.vars import *


__all__ = ["load_static_sprites", "load_animated_sprites", "SpriteStruct"]


static_sprites_names = [
    "default.png",
    "putin.png",
    "light.png",
    "tree.png",
    "dead_tree.png",
    "demon.png",
    "grunt.png",
    "street_light2.png",
    "health_5.png",
    "health_25.png",
    "ammo_10.png",
    "ammo_50.png",
]

#static_sprites = {sprite: load_texture(SPRITES_DIR+sprite) for sprite in static_sprites_names}

def load_static_sprites():
    return {sprite: load_texture(SPRITES_DIR+sprite) for sprite in static_sprites_names}

def load_animated_sprites(model: str, animations: list):
    directory = f"{TEXTURES_DIR}/{model}"
    sprites_dict = {}
    for anim in animations:
        anim_key = anim.replace("{}", "")
        sprites_dict[anim_key] = []
        try:
            i = 1
            if anim.endswith("{}"):
                while True:
                    sprites_dict[anim_key].append(load_texture(pg.image.load(f"{directory}/{anim.format(i)}.png")))
                    i += 1
            else:
                sprites_dict[anim_key].append(load_texture(pg.image.load(f"{directory}/{anim}.png")))
        except FileNotFoundError:
            continue
    return sprites_dict


@dataclass
class SpriteStruct:
    name  : str
    height: float = 100.0
    width : float = 100.0
