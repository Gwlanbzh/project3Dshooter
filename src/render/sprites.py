from dataclasses import dataclass
import pygame as pg
from render.textures import load_texture
from render.vars import *


__all__ = ["static_sprites", "SpriteStruct"]


static_sprites_names = [
    "default.png",
    "putin.png",
    "light.png",
    "tree.png",
    "dead_tree.png",
    "demon.png",
    "street_light.png",
    "street_light2.png",
    "health_25.png",
    "ammo_20.png",
]

static_sprites = {sprite:load_texture(SPRITES_DIR+sprite) for sprite in static_sprites_names}


@dataclass
class SpriteStruct:
    sprite: list
    height: float = 100.0
    width : float = 100.0
