import pygame as pg

class Config():
    WINDOW_SIZE = WINDOW_W, WINDOW_H = 600 , 400 # valeur arbitraire
    FRAME_RATE = 60

    # Value to init
    PLAYER_POS = 2,2.3 # valeur arbitraire
    PLAYER_ANGLE = 0 

    def __init__(self):
        pass

    def init():
        Config.DR = 200 / Config.FRAME_RATE # nbre de pixels par seconde.
