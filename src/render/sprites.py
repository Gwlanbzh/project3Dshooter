from dataclasses import dataclass
import pygame as pg
from render.textures import load_texture
from render.vars import *
from os import listdir

static_sprites_names = [
    #"default.png",
    "putin.png",
    #"light.png",
    #"demon.png",
    "grunt.png",
    
    "health_5.png",
    "health_25.png",
    "ammo_10.png",
    "ammo_50.png",
    
    "shotgun.png",
    "rifle.png",
    "minigun.png",
    
    "street_light2.png",
    "tree.png",
    "dead_tree.png",
    "barrel.png",

    "grunt/static.png",
    "grunt/firing.png",
    "dead_mob.png",

]

mob_models_names = [
    "grunt",
    "heavy",
    "boss"
]

#static_sprites = {sprite: load_texture(SPRITES_DIR+sprite) for sprite in static_sprites_names}

def load_static_sprites():
    return {sprite: load_texture(SPRITES_DIR+sprite) for sprite in static_sprites_names}

def load_animated_sprites(model):
    textures = sorted(listdir(f"{SPRITES_DIR}{model}"))
    textures = [load_texture(f"{SPRITES_DIR}{model}/" + img_name) for img_name in textures]

    return textures


@dataclass
class SpriteStruct:
    data  : list
    height: float = 100.0
    width : float = 100.0

    
