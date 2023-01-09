from math import pi

WALL_WIDTH = 100
WINDOW_SIZE = RES_X, RES_Y = 1280 , 800 # value link to the size of the map before render is finished
PATH_ASSETS = "src/assets/"

class Config():
    """
    Contains constants for the game.
    TODO: init config from config file
    """
    WINDOW_SIZE = RES_X, RES_Y = 1280, 800
    FULLSCREEN = False
    FRAME_RATE = 120

    PLAYER_V = 0.05
    PLAYER_FRICTION = 0.13
    PLAYER_ROT_SPEED = .004
    PLAYER_MOUSE_ROT_SPEED = .0005
    
    
    PLAYER_VERT_ROT_SPEED = 4
    PLAYER_MAX_VERT_ROT = RES_Y//2
    PLAYER_MOUSE_VERT_ROT_SPEED = 1
    
    WALL_HEIGHT = 200  # height of the wall that is above the player's point of view (e.g. for a height > VIEW_HEIGHT)
    FOV_X = pi
    FOV_Y = FOV_X * RES_Y / RES_X
    
    VIEW_HEIGHT = 75


    BOBBING_FREQUENCY = 12
    BOBBING_INTENSITY = 2.30


    TEXTURES_DIR = "src/assets/visual/textures/"
    SPRITES_DIR = "src/assets/visual/sprites/"
    SKYBOX_DIR = "src/assets/visual/env/"
    SOUNDS_FOLDER = "src/assets/sounds/"

    NO_SOUND = False
