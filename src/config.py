from math import pi
import pygame as pg
from pygame import Vector2 as v2, Vector3 as v3

class Config():
    """
    Contains constants for the game.
    TODO: init config from config file
    """
    WINDOW_SIZE = 1200 , 800 # value link to the size of the map before render is finished
    RES_X, RES_Y = WINDOW_SIZE
    FRAME_RATE = 60

    PLAYER_V = 1 # arbitraty value for good feeling
    PLAYER_ROT_SPEED = 0.004  # arbitrary value for good feeling. temporarily, waiting for mouse handling
    
    PLAYER_VERT_ROT_SPEED = 10
    PLAYER_MAX_VERT_ROT = 100
    
    # rendering-related constants
    WALL_HEIGHT = 150
    MAX_RENDER_DISTANCE = 1000
    RAY_STEP = 5
    FOV = pi/2
    
    DISTANCE_FADING = 1.001
    
    TEXTURES_FOLDER = "assets/textures/"
