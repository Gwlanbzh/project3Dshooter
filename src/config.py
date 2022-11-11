import pygame as pg

class Config():
    WINDOW_SIZE = WINDOW_W, WINDOW_H = 1200 , 800 # value link to the size of the map befor render is finished
    FRAME_RATE = 60

    PLAYER_V = 0.5 # arbitraty value for good feeling
    PLAYER_ROT_SPEED = 0.004  # arbitraty value for good feeling. temporaty, waitting for mouse handling

    def init():
        Config.DR = 200 / Config.FRAME_RATE # nbre de pixels par seconde.
