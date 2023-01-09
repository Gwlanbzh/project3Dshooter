import pygame as pg;
from ui.ui_component import *;
from config import *


GRAY = pg.Color(170,170,170) 

class MainMenu:
    def __init__(self,main):
        self.main = main
        self.ui_elements_display = [
        Menu_Title(main.window,(0.5*RES_X,0.2*RES_Y))
        ]
        self.ui_elements_button = [
            Play_Button(main.window,(0.5*RES_X,0.4*RES_Y),main),
            Quit_Game_Button(main.window,(0.5*RES_X,0.7*RES_Y),main.sound),
            Select_World_Selectioner(main.window,(0.5*RES_X,0.47*RES_Y),main),
            Draw2DCheckBox(main.window,(0.5*RES_X - 100,0.6*RES_Y),main.sound,main),
        ]
        self.set_background(PATH_ASSETS+"Menu_Background.jpg",(RES_X,RES_Y))

    def set_background(self,path,size):
        background = pg.image.load(PATH_ASSETS+"visual/ui/Menu_Background.jpg")
        background = pg.transform.scale(background,size)
        self.background = background

    def run(self):
        self.draw()

    def draw(self):       
        self.main.window.blit(self.background,(0,0))
        for element in self.ui_elements_display:
            element.draw()
        for element in self.ui_elements_button:
            element.draw()

    def click(self,event):
        for element in self.ui_elements_button:
            element.click(event)

    def hover(self):
        for element in self.ui_elements_button:
            element.hover()

class Menu_Title(Display):
    def __init__(self,window,position):
        super().__init__(window,position)
        self.text = "Bad Mood"
        self.font_size = 50
        self.is_center = True
        self.update_surface()

class Select_World_Selectioner:
    def __init__(self,window,position,main):
        self.window = window
        self.main = main
        self.position = position
        self.ui_elements_display = [
            DescriptionGameSelectorDisplay(window,position),
        ]
        self.buttonselectorleft = ButtonSelectLeft(self.window,(self.position[0]-0.15*RES_X,self.position[1]+0.05*RES_Y),self.main,self)
        self.buttonselectorright = ButtonSelectRight(self.window,(self.position[0]+0.15*RES_X,self.position[1]+0.05*RES_Y),self.main,self)
        self.currentGameNameDisplay = CurrentGameNameDisplay(self.window,(self.position[0],self.position[1]+0.05*RES_Y),self.main,self)
        self.update_selector()

    def update_selector(self):
        if self.main.current_level_index < 1:
            self.ui_elements_button = [
                self.currentGameNameDisplay,
                self.buttonselectorright,                
            ]
            self.buttonselectorleft.lifetime = 0

        elif self.main.current_level_index == self.main.max_level_index - 1:
            self.ui_elements_button = [
                self.buttonselectorleft,                
                self.currentGameNameDisplay,
            ]
            self.buttonselectorright.lifetime = 0
        else:
            self.ui_elements_button = [
                self.currentGameNameDisplay,
                self.buttonselectorleft,                
                self.buttonselectorright,                
            ]
        self.currentGameNameDisplay.update_content()

    def draw(self):       
        self.update_selector()
        for element in self.ui_elements_button:
            element.draw()
        for element in self.ui_elements_display:
            element.draw()

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
        self.text = "Current Level : "
        self.is_center = True
        self.update_surface()

class CurrentGameNameDisplay(Button):
    def __init__(self, window, position,main,selector):
        super().__init__(window, position,main.sound)
        self.selector = selector
        self.main = main
        self.font_size = 27
        self.is_center = True
        self.update_content()
        self.update_surface()

    def update_content(self):
        self.content = self.main.levels_list[self.main.current_level_index][0]
        self.update_surface()

    def action(self):
        print("TODO")
        pass

class ButtonSelectRight(Button):
    def __init__(self, window, position,main,selector):
        super().__init__(window, position,main.sound)
        self.main = main
        self.selector = selector
        self.text = ">>"
        self.font_size = 30
        self.is_center = True
        self.update_surface()

    def action(self):
        self.main.current_level_index += 1
        if self.main.current_level_index > self.main.max_level_index:
            self.main.current_level_index = self.main.max_level_index
        self.selector.update_selector()

class ButtonSelectLeft(Button):
    def __init__(self,window, position,main,selector):
        super().__init__(window, position,main.sound)
        self.main = main
        self.selector = selector
        self.text = "<<"
        self.font_size = 30
        self.is_center = True
        self.update_surface()

    def action(self):
        self.main.current_level_index -= 1
        if self.main.current_level_index < 0:
            self.main.current_level_index = 0
        self.selector.update_selector()

class Play_Button(Button):
    def __init__(self,window,position,main):
        super().__init__(window,position,main.sound)
        self.main = main
        self.text = "PLAY"
        self.font_size = 30
        self.is_center = True
        self.update_surface()

    def action(self):
        print("Good Game")
        level = self.main.levels[self.main.levels_list[self.main.current_level_index][0]]
        self.main.load_game(level)

class Quit_Game_Button(Button):
    def __init__(self,window,position,sound):
        super().__init__(window,position,sound)
        self.text = "QUIT"
        self.font_size = 30
        self.is_center = True
        self.update_surface()

    def action(self):
        print("Thank you for playing ")
        pg.quit()  # quit pygame
        sys.exit()  # better quit, remove some error when  quiting

class Draw2DCheckBox():
    def __init__(self,window,position,sound,main):
        self.ui_checkbox = self.CheckBox(window,position,sound,main)
        self.ui_display = self.Label(window,(position[0]+40,position[1]+12))
        pass

    def draw(self):
        self.ui_display.draw()
        self.ui_checkbox.draw()
    
    def click(self,event):
        self.ui_checkbox.click(event)

    def hover(self):
        self.ui_checkbox.hover()

    class Label(Display):
        def __init__(self, window, position,):
            super().__init__(window, position)
            self.text = ": Draw2D"
            self.update_surface()
    
    class CheckBox(CheckBox):
        def __init__(self, window, position, sound,main):
            super().__init__(window, position, sound)
            self.main = main
            self.update_surface()

        def action(self):
            self.main.draw2d = not self.main.draw2d
            self.update_surface()
            

