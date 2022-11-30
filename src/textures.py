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

NO_W0 = 0  # no wall
W_DEF = 1  # wall with default texture nb1
W_TX1 = 2  # wall with default texture nb 2
W_TX2 = 3  # wall with texture mc_wall
W_TX3 = 4  # wall with texture xon_concrete_plates
W_TX4 = 5  # wall with texture wall
W_TX5 = 6  # wall with texture concrete

textures_map = {W_DEF: "quake_texture_5.png",
                W_TX1: "quake_texture_17.png",
                W_TX2: "quake_texture_25.png",
                W_TX3: "quake_texture_11.png",
                W_TX4: "quake_texture_4.png",
                W_TX5: "concrete.png"
               }

textures_units_per_strip = {t:100/len(textures[textures_map[t]]) for t in textures_map}
