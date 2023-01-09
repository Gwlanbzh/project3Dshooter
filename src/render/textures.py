import pygame as pg
from math import pi
from config import Config
from render.vars import *


__all__ = ["load_texture", "load_texture_set", "height_map", "NO_WALL"]


NO_WALL = 0

# height map for each texture, that is above the player's point of view (e.g. the total height is this value *plus* VIEW_HEIGHT).
height_map = {
    1: 75,
    2: 75,
    3: 75,
    4: 75,
    5: 110,
    6: 300,
    7: 75,
    8: 75,
    9: 75
}

# Load the textures as arrays of colum surfaces.

def load_texture(path: str):
    """
    Return an array of the columns of a given image as pygame Surfaces.
    """
    return [column.transpose().make_surface() for column in pg.PixelArray(pg.image.load(path).convert_alpha())]

def load_texture_set(texture_set: str):
    """
    Return a dictionary of textures using load_textures.
    """
    texture_dict = {}
    try:
        for i in range(1, 11):
            texture_path = TEXTURES_DIR + texture_set + "/" + str(i) + ".png"
            texture_dict[i] = load_texture(texture_path)
    except FileNotFoundError:  # end of set reached
        return texture_dict
