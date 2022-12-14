import pygame as pg
from math import pi
from config import Config

TEXTURES_FOLDER = Config.TEXTURES_FOLDER
RES_Y = Config.RES_Y
RES_X = Config.RES_X
FOV_X = Config.FOV_X


# Create a dict to map a number (the values in the map array) to a texture

NO_WALL = 0  # no wall
W_TX0 = 1  # wall with default texture nb1
W_TX1 = 2  # wall with default texture nb 2
W_TX2 = 3  # wall with texture mc_wall
W_TX3 = 4  # wall with texture xon_concrete_plates
W_TX4 = 5  # wall with texture wall
W_TX5 = 6  # wall with texture concrete
W_TX6 = 7  # wall with texture concret

textures_map = {W_TX0: "quake_texture_5.png",
                W_TX1: "quake_texture_17.png",
                W_TX2: "quake_texture_25.png",
                W_TX3: "quake_texture_27.png",
                W_TX4: "quake_texture_4.png",
                W_TX5: "quake_texture_9.png",
                W_TX6: "quake_texture_24_double.png",
               }

# height map for each texture

height_map = {W_TX0: 75,
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

textures = {id:load_texture(TEXTURES_FOLDER+textures_map[id]) for id in textures_map}

textures_units_per_strip = {t:100/len(textures[t]) for t in textures_map}


#skybox = [pg.transform.scale(column, (1, RES_Y)) for column in load_texture("assets/env/green-half.png")]

img = pg.image.load("src/assets/env/green.png")
w, h = img.get_width(), img.get_height()
k = (2*pi*RES_X)/(FOV_X*w)  # upscaling factor
W = (2*pi+FOV_X)*RES_X/FOV_X  # width of the final skybox
skybox_angle_per_stripe = 2*pi/(k*w)
sky_texture = pg.transform.scale(img, (k*w,k*h))
skybox = pg.Surface((W, RES_Y))
skybox.blit(sky_texture, (0, 0))
skybox.blit(sky_texture, (k*w, 0))

if __name__ =="__main__":
    pg.init()
    window = pg.display.set_mode((1920, 500))
    window.blit(pg.transform.scale(skybox, (skybox.get_width()/4, skybox.get_height()/4)), (0, 50))
    pg.display.update()
    while True:
        for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()

textures_map = {
                1: "default.png",
                2: "default2.png",
                3: "mc_wall.png",
                4: "xon_concrete_plates.png"
            }
