import pygame as pg
from math import pi
from config import Config
from render.vars import *


__all__ = ["skybox", "skybox_angle_per_stripe"]


tx = pg.image.load(SKYBOX)
w, h = tx.get_width(), tx.get_height()
k = (2*pi*RES_X)/(FOV_X*w)    # upscaling factor for the texture
W = (2*pi+FOV_X)*RES_X/FOV_X  # width of the final skybox
skybox_angle_per_stripe = 2*pi/(k*w)
sky_texture = pg.transform.scale(tx, (k*w,k*h))
skybox = pg.Surface((W, RES_Y))
skybox.blit(sky_texture, (0, 0))
skybox.blit(sky_texture, (k*w, 0))
