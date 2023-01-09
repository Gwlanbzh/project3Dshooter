from math import pi

WALL_WIDTH = 100
WINDOW_SIZE = RES_X, RES_Y = 1280 , 800 # value link to the size of the map before render is finished
PATH_ASSETS = "src/assets/"

class Config():
    """
    Contains constants for the game.
    TODO: init config from config file
    """
    WINDOW_SIZE = RES_X, RES_Y = 1280 , 800 # value link to the size of the map before render is finished
    FRAME_RATE = 120

    PLAYER_V = 0.065 # arbitraty value for good feeling
    PLAYER_FRICTION = 0.13
    PLAYER_ROT_SPEED = .004  # arbitrary value for good feeling. temporarily, waiting for mouse handling
    
    PLAYER_VERT_ROT_SPEED = 4
    PLAYER_MAX_VERT_ROT = RES_Y//2
    
    PLAYER_MOUSE_ROT_SPEED = .0005  # arbitrary value for good feeling. temporarily, waiting for mouse handling
    PLAYER_MOUSE_VERT_ROT_SPEED = 1
    
    WALL_HEIGHT = 200  # height of the wall that is above the player's point of view (e.g. for a height > VIEW_HEIGHT)
    FOV_X = 2*pi/3
    FOV_Y = FOV_X
    
    VIEW_HEIGHT = 85

    BOBBING_FREQUENCY = 10
    BOBBING_INTENSITY = 1


    TEXTURES_DIR = "src/assets/visual/textures/"
    SPRITES_DIR = "src/assets/visual/sprites/"
    SKYBOX_DIR = "src/assets/visual/env/"
    SOUNDS_FOLDER = "src/assets/sounds/"

    NO_SOUND = False
