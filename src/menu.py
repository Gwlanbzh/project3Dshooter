import pygame as pg;
from ui_component import *;
from config import *


GRAY = pg.Color(170,170,170) 

class MainMenu:
    def __init__(self,game):
        self.game = game
        self.worlds = []
        self.menu_title = Menu_Title(game,(0.5*RES_X,0.2*RES_Y))
        self.ui_elements_button = [
            Play_Button(game,(0.5*RES_X,0.4*RES_Y)),
            Quit_Game_Button(game,(0.5*RES_X,0.7*RES_Y)),
            Menu_Select_World_Button(game,(0.5*RES_X,0.5*RES_Y))
        ]
        self.menu_setting = menu_setting()
        self.background = pg.image.load(PATH_ASSETS+"Menu_Background.jpg")
        self.background = pg.transform.scale(self.background,(RES_X,RES_Y))
        pass

    def draw_menu_background(self):
        self.game.window.blit(self.background,(0,0))

    def draw(self):       
        self.draw_menu_background()
        self.menu_title.draw_without_content()
        # self.menu_setting.draw()
        for element in self.ui_elements_button:
            element.draw()


    def click(self,event):
        for element in self.ui_elements_button:
            element.click(event)

class MenuOption:
    pass
