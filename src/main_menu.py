import pygame as pg;
from ui_component import *;
from config import *


GRAY = pg.Color(170,170,170) 

class MainMenu:
    def __init__(self,main):
        self.main = main
        self.menu_title = Menu_Title(main,(0.5*RES_X,0.2*RES_Y))

        self.levels = main.levels
        self.levels_list = [ (level_name , False) if i == 0 else (level_name,True) for i , level_name in enumerate(self.levels)] 
        self.current_level_index = 0
        self.ui_elements_button = [
            Play_Button(main,(0.5*RES_X,0.4*RES_Y),self),
            Quit_Game_Button(main,(0.5*RES_X,0.7*RES_Y)),
            Select_World_Selectioner(main,(0.5*RES_X,0.5*RES_Y),self)
        ]

        self.background = pg.image.load(PATH_ASSETS+"Menu_Background.jpg")
        self.background = pg.transform.scale(self.background,(RES_X,RES_Y))

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

    def hover(self):
        for element in self.ui_elements_button:
            element.hover()

class Select_World_Selectioner:
    def __init__(self,main,position,menu):
        self.main = main
        self.menu = menu
        self.position = position
        self.max_level_index = len(self.main.levels)
        self.ui_elements_display = [
            #Display(main,position,"Current Level :"),
            DescriptionGameSelectorDisplay(main,position),
        ]
        self.update_selector()

    def update_selector(self):
        if self.menu.current_level_index < 1:
            self.ui_elements_button = [
                CurrentGameNameDisplay(self.main,(self.position[0],self.position[1]+0.05*RES_Y),self),
                ButtonSelectRight(self.main,(self.position[0]+0.15*RES_X,self.position[1]+0.05*RES_Y),self),
            ]

        elif self.menu.current_level_index == self.max_level_index - 1:
            self.ui_elements_button = [
                ButtonSelectLeft(self.main,(self.position[0]-0.15*RES_X,self.position[1]+0.05*RES_Y),self),
                CurrentGameNameDisplay(self.main,(self.position[0],self.position[1]+0.05*RES_Y),self),
            ]
        else:
            self.ui_elements_button = [
                CurrentGameNameDisplay(self.main,(self.position[0],self.position[1]+0.05*RES_Y),self),
                ButtonSelectLeft(self.main,(self.position[0]-0.15*RES_X,self.position[1]+0.05*RES_Y),self),
                ButtonSelectRight(self.main,(self.position[0]+0.15*RES_X,self.position[1]+0.05*RES_Y),self),
            ]

    def draw(self):       
        for element in self.ui_elements_button:
            element.draw()
        for element in self.ui_elements_display:
            element.draw_without_content()

    def click(self,event):
        for element in self.ui_elements_button:
            element.click(event)

    def hover(self):
        for element in self.ui_elements_button:
            element.hover()

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
    def __init__(self, main, position,selector):
        super().__init__(main, position)
        self.selector = selector
        self.update_content()
        self.background = (0,0,255,0)
        self.background_activate = RED
        self.background_idle = self.background
        self.myfont = pg.font.Font(PATH_ASSETS+"fonts/PressStart2P-Regular.ttf", 30)
        self.label = self.myfont.render(self.text, 1, self.foreground)
        self.update_surface()
        self.position = self.get_position_centered_surface()
        self.update_surface()

    def update_content(self):
        self.text = self.selector.menu.levels_list[self.selector.menu.current_level_index][0]


class ButtonSelectRight(Button):
    def __init__(self, main, position,selector):
        super().__init__(main, position,)
        self.selector = selector
        self.text = ">>"
        self.background = (0,0,255,0)
        self.background_activate = RED
        self.background_idle = self.background
        self.myfont = pg.font.Font(PATH_ASSETS+"fonts/PressStart2P-Regular.ttf", 30)
        self.label = self.myfont.render(self.text, 1, self.foreground)
        self.Game_index_Selector = 0
        self.update_surface()
        self.position = self.get_position_centered_surface()
        self.update_surface()

    def action(self):
        self.selector.menu.current_level_index += 1
        if self.selector.menu.current_level_index > self.selector.max_level_index:
            self.selector.menu.current_level_index = self.selector.max_level_index
        self.selector.update_selector()

class ButtonSelectLeft(Button):
    def __init__(self, main, position,selector):
        super().__init__(main, position,)
        self.text = "<<"
        self.selector = selector
        self.background = (0,0,255,0)
        self.background_activate = RED
        self.background_idle = self.background
        self.myfont = pg.font.Font(PATH_ASSETS+"fonts/PressStart2P-Regular.ttf", 30)
        self.label = self.myfont.render(self.text, 1, self.foreground)
        self.update_surface()
        self.position = self.get_position_centered_surface()
        self.update_surface()

    def action(self):
        self.selector.menu.current_level_index -= 1
        if self.selector.menu.current_level_index < 0:
            self.selector.menu.current_level_index = 0
        self.selector.update_selector()

class Play_Button(Button):
    def __init__(self,main,position,menu):
        super().__init__(main,position)
        self.text = "PLAY"
        self.main = main
        self.menu = menu
        self.background = (0,0,255,0)
        self.background_activate = RED
        self.background_idle = self.background
        self.myfont = pg.font.Font(PATH_ASSETS+"fonts/PressStart2P-Regular.ttf", 30)
        self.label = self.myfont.render(self.text, 1, self.foreground)
        self.update_surface()
        self.position = self.get_position_centered_surface()
        self.update_surface()

    def action(self):
        print("Good Game")
        level = self.menu.levels[self.menu.levels_list[self.menu.current_level_index][0]]
        self.main.load_game(level)

class Quit_Game_Button(Button):
    def __init__(self,main,position):
        super().__init__(main,position)
        self.main = main
        self.text = "QUIT"
        self.police_size = 30
        self.background = (0,0,255,0)
        self.background_activate = RED
        self.background_idle = self.background

        self.myfont = pg.font.Font(PATH_ASSETS+"fonts/PressStart2P-Regular.ttf", self.police_size)
        self.label = self.myfont.render(self.text, 1, self.foreground)
        self.update_surface()
        self.position = self.get_position_centered_surface()
        self.update_surface()

    def action(self):
        print("Thank you for playing ")
        pg.quit()  # quit pygame
        sys.exit()  # better quit, remove some error when  quiting
        pass


