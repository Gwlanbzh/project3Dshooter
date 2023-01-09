from dataclasses import dataclass
import pygame as pg
from render.textures import load_texture
from render.vars import *
from os import listdir


mob_models_names = [
    "grunt",
    "heavy",
    "boss"
]

static_sprites_names = [
    #"default.png",
    "putin.png",
    #"light.png",
    #"demon.png",
    "grunt.png",
    
    "health_mini.png",
    "health_mega.png",
    "ammo_mini.png",
    "ammo_mega.png",
    "mine.png",
    
    "shotgun.png",
    "rifle.png",
    "minigun.png",
    
    "street_light2.png",
    "tree.png",
    "dead_tree.png",
    "barrel.png",

    "dead_mob.png",

]

animated_sprites_name = []

for mob_name in mob_models_names:
    static_sprites_names.append(mob_name + "/shooted.png")
    static_sprites_names.append(mob_name + "/firing.png")
    static_sprites_names.append(mob_name + "/static.png")
    static_sprites_names.append(mob_name + "/dead.png")
    animated_sprites_name.append(mob_name + "/walking")

def load_static_sprites():
    return {sprite: load_texture(SPRITES_DIR+sprite) for sprite in static_sprites_names}

def load_animated_sprites():
    textures = dict()
    for dir in animated_sprites_name:
        temp = sorted(listdir(f"{SPRITES_DIR}{dir}"))
        temp = [load_texture(f"{SPRITES_DIR}{dir}/" + img_name) for img_name in temp]
        textures[dir] = temp

    return textures


@dataclass
class SpriteStruct:
    data  : list
    height: float = 100.0
    width : float = 100.0

    
