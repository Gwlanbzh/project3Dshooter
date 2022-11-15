from math import pi
import pygame as pg
from pygame import Vector2 as v2, Vector3 as v3

class Config():
    WINDOW_SIZE = RES_X, RES_Y = 1200 , 800 # value link to the size of the map befor render is finished
    FRAME_RATE = 60

    PLAYER_V = 0.5 # arbitraty value for good feeling
    PLAYER_ROT_SPEED = 0.004  # arbitraty value for good feeling. temporaty, waitting for mouse handling
    
    # rendering-related constants
    WALL_HEIGHT = 30
    MAX_RENDER_DISTANCE = 1000
    RAY_STEP = 5
    FOV = pi/2
    
    DISTANCE_FADING = 1.001

    def init():
        Config.DR = 200 / Config.FRAME_RATE # nbre de pixels par seconde.
