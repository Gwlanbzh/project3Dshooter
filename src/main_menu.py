import pygame as pg;
from ui_component import *;
from config import *


GRAY = pg.Color(170,170,170) 

class MainMenu:
    def __init__(self,main):
        self.main = main
        self.worlds = []
        self.menu_title = Menu_Title(main,(0.5*RES_X,0.2*RES_Y))
        self.ui_elements_button = [
            Play_Button(main,(0.5*RES_X,0.4*RES_Y)),
            Quit_Game_Button(main,(0.5*RES_X,0.7*RES_Y)),
            Select_World_Selectioner(main,(0.5*RES_X,0.5*RES_Y),self.main.GameList)
        ]
        self.background = pg.image.load(PATH_ASSETS+"Menu_Background.jpg")
        self.background = pg.transform.scale(self.background,(RES_X,RES_Y))
        pass

    def run(self):
        self.draw()


    def draw_menu_background(self):
        self.main.window.blit(self.background,(0,0))

    def draw(self):       
        self.draw_menu_background()
        self.menu_title.draw_without_content()
        for element in self.ui_elements_button:
            element.draw()

    def click(self,event):
        for element in self.ui_elements_button:
            element.click(event)

    def over(self):
        for element in self.ui_elements_button:
            element.over()

class Select_World_Selectioner:
    def __init__(self,main,position,GameList):
        self.main = main
        self.position = position
        self.GameList = GameList
        self.ui_elements_display = [
            DescriptionGameSelectorDisplay(main,position),

        ]
        self.ui_elements_button = [
            #CurrentGameNameDisplay(main,position,GameList),
        ]


    def draw(self):       
        for element in self.ui_elements_button:
            element.draw()
        for element in self.ui_elements_display:
            element.draw_without_content()

    def click(self,event):
        for element in self.ui_elements_button:
            element.click(event)

    def over(self):
        for element in self.ui_elements_button:
            element.over()
        pass

class DescriptionGameSelectorDisplay(Display):
    def __init__(self, main, position):
        super().__init__(main, position)
        self.font_size = 20
        self.string = "Current Level : "
        self.myfont = pg.font.Font(PATH_ASSETS+"fonts/PressStart2P-Regular.ttf",self.font_size)
        self.label = self.myfont.render(self.string, 1, self.foreground)
        self.update_size()
        self.position = self.get_position_centered_surface()
        self.position = self.position[0]-0*RES_X,self.position[1]

class CurrentGameNameDisplay(Button):
    def __init__(self, game, position,GameList):
        super().__init__(game, position)
        self.text = "play"
        self.background = (0,0,255,0)
        self.background_activate = RED
        self.background_idle = self.background
        self.myfont = pg.font.Font(PATH_ASSETS+"fonts/PressStart2P-Regular.ttf", 30)
        self.label = self.myfont.render(self.text, 1, self.foreground)
        self.Game_index_Selector = 0
        self.update_surface()
        self.position = self.get_position_centered_surface()
        self.update_surface()


