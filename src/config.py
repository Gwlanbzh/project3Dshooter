from math import pi

WALL_WIDTH = 100
WINDOW_SIZE = RES_X, RES_Y = 1280 , 800 # value link to the size of the map before render is finished
PATH_ASSETS = "src/assets/"

class Config():
    """
    Contains constants for the game.
    """
    WINDOW_SIZE = RES_X, RES_Y = 1280 , 800 # value link to the size of the map before render is finished
    FRAME_RATE = 120

    PLAYER_V = 0.065 # arbitraty value for good feeling
    PLAYER_FRICTION = 0.13
    PLAYER_ROT_SPEED = .004
    PLAYER_MOUSE_ROT_SPEED = .0005
    
    # Vertical rotation
    PLAYER_MAX_VERT_ROT = RES_Y//2
    PLAYER_VERT_ROT_SPEED = 4
    PLAYER_MOUSE_VERT_ROT_SPEED = 1
    
    # Rendering
    FOV_X = 2*pi/3
    FOV_Y = FOV_X
    
    VIEW_HEIGHT = 85 # The height from which the camera will render the scene.

    BOBBING_FREQUENCY = 10
    BOBBING_INTENSITY = 1

    # Directories
    TEXTURES_DIR = "src/assets/visual/textures/"
    SPRITES_DIR = "src/assets/visual/sprites/"
    SKYBOX_DIR = "src/assets/visual/env/"
    SOUNDS_FOLDER = "src/assets/sounds/"

    # Sound
    NO_SOUND = False
