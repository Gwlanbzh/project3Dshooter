from math import pi

WALL_WIDTH = 100
WINDOW_SIZE = RES_X, RES_Y = 1280 , 800 # value link to the size of the map before render is finished
PATH_ASSETS = "src/assets/"

class Config():
    """
    Contains constants for the game.
    """
    # Display
    WINDOW_SIZE = RES_X, RES_Y = 1280, 800
    FULLSCREEN = False
    FRAME_RATE = 120

    # Player movement and horizontal rotation
    PLAYER_V = 0.05
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
    VIEW_HEIGHT = 75  # The height from which the camera will render the scene.

    # Bobbing
    BOBBING_FREQUENCY = 12
    BOBBING_INTENSITY = 3

    # Directories
    TEXTURES_DIR = "src/assets/visual/textures/"
    SPRITES_DIR = "src/assets/visual/sprites/"
    SKYBOX_DIR = "src/assets/visual/env/"
    SOUNDS_FOLDER = "src/assets/sounds/"

    # Sound
    NO_SOUND = False
