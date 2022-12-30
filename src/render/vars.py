from config import *
from math import tan, atan


TEXTURES_FOLDER = Config.TEXTURES_FOLDER
SPRITES_DIR = Config.SPRITES_DIR
SKYBOX = Config.SKYBOX
GROUND_COLOR = Config.GROUND_COLOR

VIEW_HEIGHT = Config.VIEW_HEIGHT
RES_X = Config.RES_X
RES_Y = Config.RES_Y
FOV_X = Config.FOV_X
FOV_Y = Config.FOV_Y


# function for computing the ray 's direction vector
atanfov = atan(FOV_X/2)
theta = lambda n : atan(atanfov * ( 1-(2*n) / RES_X))

theta_inv = lambda theta : (1 - (RES_X*tan(theta))/atanfov) * 1/2


# function for computing the on-screen height of a wall segment
resfovratio = RES_Y / FOV_Y
scr_h = lambda h, d : resfovratio * (h/d)


sign = lambda x : 1 if x >= 0 else -1
