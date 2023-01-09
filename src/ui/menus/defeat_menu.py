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
            GameToMainMenuButton(game.window,(RES_X*0.5,RES_Y*0.8),game)
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

class GameToMainMenuButton(Button):
    def __init__(self,window,position,game):
        super().__init__(window,position)
        self.game = game
        self.text = "Main Menu"
        self.foreground = WHITE
        self.is_center = True
        self.update_surface()

    def action(self):
        self.game.is_abandon = True