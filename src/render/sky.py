import pygame as pg
from math import pi
from config import Config
from render.vars import *


__all__ = ["load_skybox"]


def load_skybox(name: str):
    """
    Return a pygame surface representing a skybox. Used in the world class.
    """
    tx = pg.image.load(SKYBOX_DIR+name)
    w, h = tx.get_width(), tx.get_height()
    W = (2*pi*RES_X)/(FOV_X*w) * w    # upscaling factor for the texture
    H = (2*pi*RES_Y)/(FOV_Y*h) * h
    
    box_W = (2*pi+FOV_X)*RES_X/FOV_X  # width of the final skybox
    
    #print(h)
    #print(k*h)
    #print(RES_Y)
    
    skybox_angle_per_strip = 2*pi/(W)
    sky_texture = pg.transform.scale(tx, (W, RES_Y))
    skybox = pg.Surface((box_W, RES_Y))
    skybox.blit(sky_texture, (0, 0))
    skybox.blit(sky_texture, (W, 0))
    
    return skybox, skybox_angle_per_strip
