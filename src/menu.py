import pygame as pg;
from ui_component import *;
from config import *


GRAY = pg.Color(170,170,170) 

class MainMenu:
    def __init__(self,game):
        self.game = game
        self.worlds = []
        self.menu_title = Menu_Title(game,(0.5*RES_X,0.2*RES_Y))
        self.menu_select_world = Menu_Select_World()
        self.menu_setting = menu_setting()
        self.play_button = Play_Button()
        self.quit_game_button = Quit_Game_Button()
        pass

    def draw_menu_background(self):
        menu_background = 'gray'
        self.game.window.fill(menu_background)

    def draw(self):       
        self.draw_menu_background()
        self.menu_title.draw_without_content()
        # self.menu_select_world.draw()
        # self.menu_setting.draw()
        # self.play_button.draw()
        # self.quit_game_button.draw()

    def draw_quit():

        pass

    def draw_title(self):
        pass

    def load_world(self,game):
        pass

class MenuOption:
