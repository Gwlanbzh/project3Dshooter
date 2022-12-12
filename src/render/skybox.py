import pygame as pg
from math import pi
from config import Config
from render.vars import *


RES_Y = Config.RES_Y
RES_X = Config.RES_X
FOV_X = Config.FOV_X


__all__ = ["skybox"]


img = pg.image.load(SKYBOX)
w, h = img.get_width(), img.get_height()
k = (2*pi*RES_X)/(FOV_X*w)  # upscaling factor
W = (2*pi+FOV_X)*RES_X/FOV_X  # width of the final skybox
skybox_angle_per_stripe = 2*pi/(k*w)
sky_texture = pg.transform.scale(img, (k*w,k*h))
skybox = pg.Surface((W, RES_Y))
skybox.blit(sky_texture, (0, 0))
skybox.blit(sky_texture, (k*w, 0))
