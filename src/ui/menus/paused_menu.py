import pygame as pg;
from ui.ui_component import *;
from config import *

class PausedMenu():
    def __init__(self,game,position):
        self.game = game
        self.color_backbackground = (0,0,0)
        self.size = (RES_X*0.3,RES_Y*0.6)
        self.position = position
        self.background = pg.image.load(PATH_ASSETS+"visual/ui/Menu_Background.jpg")
        self.background = pg.transform.scale(self.background,self.size)

        self.description = CurrentGameDescriptionDisplay(game.window,self.position,self.game.description) 

        self.ui_elements_button = [  # Button not working properly we remove them. they stand here while fix not find
            GameToMainMenuButton(game.window,(position[0],position[1]-self.size[1]//2*0.7),game),
            ResumeButton(game.window,(position[0],self.size[1]//2+position[1]),game)
        ]

    def draw(self):
        #self.game.window.blit(self.background,((self.position[0]-self.size[0]//2,self.position[1]-self.size[1]//2)))
        self.description.draw()
        #for element in self.ui_elements_button:
            #element.draw()
        pass

    def hover(self):
        #for element in self.ui_elements_button:
            #element.hover()
        pass

    def click(self,event):
        #for element in self.ui_elements_button:
            #element.click(event)
        pass
    

class GameToMainMenuButton(Button):
    def __init__(self,window,position,game):
        super().__init__(window,position)
        self.game = game
        self.text = "Main Menu"
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
        self.game.is_esc_menu_active = False


class CurrentGameDescriptionDisplay(Display):
    """
    not use. need a way to get description of a Game without the game to be init
    """
    def __init__(self, window, position,description):
        super().__init__(window, (position[0],position[1]-0.4*RES_Y))
        self.font_size = 18
        self.is_center = True
        self.description = description
        self.update_content()
        self.update_surface()

    def update_content(self):
        self.content = self.description
        self.update_surface()