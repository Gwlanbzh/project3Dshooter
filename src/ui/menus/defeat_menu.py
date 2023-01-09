import pygame as pg;
from ui.ui_component import *;
from config import *

class DefeatMenu():
    def __init__(self,game,position):
        self.game = game
        self.size = (RES_X*0.65,RES_Y*0.5)
        self.position = position

        self.background = pg.image.load(PATH_ASSETS+"visual/ui/defeat.png")
        self.background = pg.transform.scale(self.background,self.size)

        self.ui_elements_button = [
        ]

    def draw(self):
        self.game.window.blit(self.background,((self.position[0]-self.size[0]//2,self.position[1]-self.size[1]//2)))
        for element in self.ui_elements_button:
            element.draw()

    def hover(self):
        for element in self.ui_elements_button:
            element.hover()

    def click(self,event):
        for element in self.ui_elements_button:
            element.click(event)

class to_main_menu(): # TODO
    pass