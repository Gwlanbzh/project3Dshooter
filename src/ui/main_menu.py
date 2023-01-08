import pygame as pg;
from ui.ui_component import *;
from config import *


GRAY = pg.Color(170,170,170) 

class MainMenu:
    def __init__(self,main):
        self.main = main
        self.menu_title = Menu_Title(main,(0.5*RES_X,0.2*RES_Y))

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
        self.ui_elements_display = [
            #Display(main,position,"Current Level :"),
            DescriptionGameSelectorDisplay(main,position),
        ]
        self.update_selector()

    def update_selector(self):
        if self.main.current_level_index < 1:
            self.ui_elements_button = [
                CurrentGameNameDisplay(self.main,(self.position[0],self.position[1]+0.05*RES_Y),self),
                ButtonSelectRight(self.main,(self.position[0]+0.15*RES_X,self.position[1]+0.05*RES_Y),self),
            ]

        elif self.main.current_level_index == self.main.max_level_index - 1:
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
        self.text = self.selector.menu.main.levels_list[self.selector.menu.main.current_level_index][0]

    def hover(self):
        is_colliding = self.rect.collidepoint(pg.mouse.get_pos())
        if is_colliding and not self.mouse_was_hover:
            if self.is_activate:
                self.foreground = self.foreground_activate
            else:
                self.foreground = self.foreground_hover
            self.label = self.myfont.render(self.text, 1, self.foreground)
            self.update_surface()
            if not self.mouse_is_over: 
               self.game.sound.play_sound("hover")
            self.mouse_is_over = True
        elif self.mouse_is_over and not is_colliding:
            if self.is_activate:
                self.foreground = self.foreground_activate
            else:
                self.foreground = self.foreground_idle
            
            self.label = self.myfont.render(self.text, 1, self.foreground)
            self.update_surface()
            self.mouse_is_over = False


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
        self.update_surface()
        self.position = self.get_position_centered_surface()
        self.update_surface()

    def action(self):
        self.selector.menu.main.current_level_index += 1
        if self.selector.menu.main.current_level_index > self.selector.menu.main.max_level_index:
            self.selector.menu.main.current_level_index = self.selector.menu.main.max_level_index
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
        self.selector.menu.main.current_level_index -= 1
        if self.selector.menu.main.current_level_index < 0:
            self.selector.menu.main.current_level_index = 0
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
        level = self.main.levels[self.main.levels_list[self.main.current_level_index][0]]
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


