from os import listdir
import pygame as pg
from config import Config

TEXTURES_FOLDER = Config.TEXTURES_FOLDER


# Load the textures as arrays of colum surfaces.

texturefiles = [f for f in listdir(TEXTURES_FOLDER) if f.endswith(".png")]

texture_surfaces = {f:pg.image.load(TEXTURES_FOLDER+f) for f in texturefiles}

textures = {}

for f in texture_surfaces:
    column_surfaces_array = []
    for column in pg.PixelArray(texture_surfaces[f]):
        column_surfaces_array.append(column.transpose().make_surface())
    textures[f] = column_surfaces_array

# Create a dict to map a number (the values in the map array) to a texture

textures_map = {
                1: "default.png",
                2: "default2.png",
                3: "mc_wall.png",
                4: "xon_concrete_plates.png"
            }
