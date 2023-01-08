import pygame as pg;
from ui.ui_component import *;
from config import *

class PausedMenu():
    def __init__(self,game,position,return_string = None, return_action = None):
        self.game = game
        self.color_backbackground = (0,0,0)
        self.background = pg.image.load(PATH_ASSETS+"visual/ui/Menu_Background.jpg")
        self.size = (RES_X*0.3,RES_Y*0.6)
        self.position = (position[0]-self.size[0]//2,position[1]-self.size[1]//2)
        self.background = pg.transform.scale(self.background,self.size)

        self.ui_elements_button = [
            GameToMainMenuButton(game.window,(position[0],self.size[1]//2*0.90+position[1]),game),
            ResumeButton(game.window,(position[0],self.size[1]//2*0.1+position[1]),game)
        ]

    def draw(self):
        self.game.window.blit(self.background,(self.position[0],self.position[1]))
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
        self.foreground = BLUE
        self.is_center = True
        self.update_surface()


    def action(self):
        print("you're bad")
        self.game.is_abandon = True

class ResumeButton(Button):
    def __init__(self,window,position,game):
        super().__init__(window,position)
        self.game = game
        self.text = "Resume"
        self.is_center = True
        self.update_surface()


    def action(self):
        self.game.is_paused = False