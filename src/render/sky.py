import pygame as pg
from math import pi
from config import Config
from render.vars import *


__all__ = ["skybox", "skybox_angle_per_stripe"]


def load_skybox(name: str):
    """
    Return a pygame surface representing a skybox. Used in the world class.
    """
    tx = pg.image.load(SKYBOX_DIR+name)
    w, h = tx.get_width(), tx.get_height()
    k = (2*pi*RES_X)/(FOV_X*w)    # upscaling factor for the texture
    W = (2*pi+FOV_X)*RES_X/FOV_X  # width of the final skybox
    skybox_angle_per_stripe = 2*pi/(k*w)
    sky_texture = pg.transform.scale(tx, (k*w,k*h))
    skybox = pg.Surface((W, RES_Y))
    skybox.blit(sky_texture, (0, 0))
    skybox.blit(sky_texture, (k*w, 0))
    
    return skybox, skybox_angle_per_stripe
