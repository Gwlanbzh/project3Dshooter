import pygame as pg
from math import pi
from config import Config
from render.vars import *


__all__ = ["global_textures", "load_texture", "height_map", "textures_units_per_strip", "NO_WALL"]


NO_WALL = 0  # no wall
W_TX0 = 1  # wall with default texture nb1
W_TX1 = 2  # wall with default texture nb 2
W_TX2 = 3  # wall with texture mc_wall
W_TX3 = 4  # wall with texture xon_concrete_plates
W_TX4 = 5  # wall with texture wall
W_TX5 = 6  # wall with texture concrete
W_TX6 = 7  # wall with texture concret

textures_map = {
    W_TX0: "cyberpunk1.png",
    W_TX1: "quake_texture_17.png",
    W_TX2: "quake_texture_25.png",
    W_TX3: "quake_texture_27.png",
    W_TX4: "quake_texture_4.png",
    W_TX5: "quake_texture_9.png",
    W_TX6: "quake_texture_24_double.png",
}

# height map for each texture

height_map = {
    W_TX0: 75,
    W_TX1: 75,
    W_TX2: 200,
    W_TX3: 300,
    W_TX4: 110,
    W_TX5: 112.5,
    W_TX6: 250,
}

# Load the textures as arrays of colum surfaces.

def load_texture(path:str):
    """
    Return an array of the columns of a given image, as surfaces if surface is True, else as PixelArrays.
    """
    return [column.transpose().make_surface() for column in pg.PixelArray(pg.image.load(path))]

global_textures = {id:load_texture(TEXTURES_DIR+textures_map[id]) for id in textures_map}

textures_units_per_strip = {t:100/len(global_textures[t]) for t in textures_map}

