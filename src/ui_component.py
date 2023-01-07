
import pygame as pg
from math import pi
from config import *
import sys

BLACK = pg.Color(0,0,0)
GRAY = pg.Color(170,170,170) 
BLUE = pg.Color(0,0,170) 
RED = pg.Color(255,0,0) 
WHITE = pg.Color(255,255,255) 

class Display:
    """
    display something and can have a content's update
    can be use outside a world
    """
    def __init__(self,game,position,size=(20,20)):
        self.game = game
        self.size = size
        self.position = position
        self.font_size = 20
        self.myfont = pg.font.Font(PATH_ASSETS+"fonts/PressStart2P-Regular.ttf",self.font_size)
        self.background = BLACK
        self.foreground = WHITE
        self.label = "text not set"

    def draw_with_content(self):
        label = self.myfont.render(self.label+self.content, 1, self.foreground ,self.background)
        self.game.window.blit(label, self.position)
        pass

    def draw_without_content(self):
        label = self.myfont.render(self.string, 1, self.foreground)
        self.game.window.blit(label, self.position)
        pass

    def update():
        pass

    def get_position_centered_surface(self):
        pos_x,pos_y = self.position
        size_x,size_y = self.size
        return (pos_x-(size_x/2),pos_y-(size_y/2))


    def update_size(self):
        size_x,size_y = self.size
        size_label_x,size_label_y = self.label.get_size()
    
        if size_x < size_label_x:
            size_x = size_label_x
        if size_y < size_label_y:
            size_y = size_label_y
        self.size = size_x,size_y      
        pass

class Button(Display):
    """
    can be click and have an animation when click
    can be use outside a world
    """
    def __init__(self,game,position,foreground = WHITE):
        super().__init__(game,position)
        self.lifetime = -1
        self.foreground = foreground
        self.foreground_activate = RED
        self.foreground_idle = self.foreground
        self.foreground_hover = GRAY
        self.mouse_is_over = False
        self.mouse_was_hover = False
        self.is_activate = False

    def update_surface(self):
        self.update_size()
        self.surface = pg.Surface(self.size,pg.SRCALPHA)
        if self.background != None:
            self.surface.fill(self.background)
        self.surface.blit(self.label,(0,0))
        self.rect = pg.Rect(self.position[0], self.position[1], 
                            self.size[0], self.size[1])
    
    def draw(self):
        if self.lifetime > 0:
            self.lifetime -= 1
            if self.lifetime <= 0:
                # change the background back to idle
                self.foreground = self.foreground_idle
                self.is_activate = False
                self.label = self.myfont.render(self.text, 1, self.foreground)
                self.update_surface()
        self.game.window.blit(self.surface, self.position)

    def click(self,event):
        """
        each button have one action, action define in 
        the specific button class since every button are unique
        pass
        self.action() must be call inside self.click()
        """
        x, y = pg.mouse.get_pos()
        if event.type == pg.MOUSEBUTTONDOWN:
            if pg.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.lifetime = 10
                    self.is_activate = True
                    self.game.sound.play_sound("click")
                    self.action()

    def action(self):
        """
        each button have one action, action define in 
        the specific button class since every button are unique
        always call by self.click()
        """
        pass

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


class Health_Bar():
    def __init__(self,game,position,player):
        self.player = player
        self.game = game
        self.position = position
        self.health_bar_length = 400
        self.health_ratio = player.max_health / self.health_bar_length
        self.health_change_speed = 5
        self.icon = pg.image.load(PATH_ASSETS+"heart_icon.png")
        self.icon = pg.transform.scale(self.icon,(70,70))
        self.myfont = pg.font.Font(PATH_ASSETS+"fonts/PressStart2P-Regular.ttf", 16)

    def draw(self):
        transition_width = 0
        transition_color = (0,0,0)

        if self.player.health < self.player.target_health:
            self.player.health += self.health_change_speed
            transition_width = int((self.player.target_health - self.player.health) / self.health_ratio)
            transition_color = (75,141,57)

        if self.player.health > self.player.target_health:
            self.player.health -= self.health_change_speed 
            transition_width = -int((self.player.target_health - self.player.health) / self.health_ratio)
            transition_color = (210,122,49)

        health_bar_width = int(self.player.health / self.health_ratio)
        health_bar = pg.Rect(self.position[0],self.position[1],health_bar_width,25)
        transition_bar = pg.Rect(health_bar.right,self.position[1],transition_width,25)

        pg.draw.rect(self.game.window,(31,32,49),(self.position[0],self.position[1],self.health_bar_length,25))	
        pg.draw.rect(self.game.window,(141,7,35),health_bar)
        pg.draw.rect(self.game.window,transition_color,transition_bar)	
        pg.draw.rect(self.game.window,(73,54,43),(self.position[0],self.position[1],self.health_bar_length,25),3)	
        label = self.myfont.render(str(self.player.health)+"/"+str(self.player.max_health), 4, (255,255,255,0))
        self.game.window.blit(label,(self.position[0]+30,self.position[1]+5))
        self.game.window.blit(self.icon,(self.position[0]-40,self.position[1]-30))
    pass

class Menu():
    def __init__(self,game,position,return_string = None, return_action = None):
        self.game = game
        self.color_backbackground = (0,0,0)
        self.background = pg.image.load(PATH_ASSETS+"Menu_Background.jpg")
        self.size = (RES_X*0.3,RES_Y*0.6)
        self.position = (position[0]-self.size[0]//2,position[1]-self.size[1]//2)
        self.background = pg.transform.scale(self.background,self.size)
        self.ui_elements_button = [
            WorldToMainMenuButton(game,(position[0],self.size[1]//2*0.90+position[1])),
        ]

    def draw(self):
        self.game.window.blit(self.background,(self.position[0],self.position[1]))
        for element in self.ui_elements_button:
            element.draw()

class WorldToMainMenuButton(Button):
    def __init__(self,game,position):
        super().__init__(game,position)
        self.text = "Main Menu"
        self.background = None
        self.foreground = BLUE
        self.myfont = pg.font.Font(PATH_ASSETS+"fonts/PressStart2P-Regular.ttf", 20)
        self.label = self.myfont.render(self.text, 1, self.foreground)
        self.update_surface()
        self.position = self.get_position_centered_surface()
        self.update_surface()
        pass


    def action(self):
        print("you're bad")
        self.game.is_abandon = True

class ResumeButton(Button):
    def __init__(self,game,position):
        super().__init__(game,position)
        self.text = "Resume"
        self.background = None
        self.foreground = BLUE
        self.myfont = pg.font.Font(PATH_ASSETS+"fonts/PressStart2P-Regular.ttf", 20)
        self.label = self.myfont.render(self.text, 1, self.foreground)
        self.update_surface()
        self.position = self.get_position_centered_surface()
        self.update_surface()
        pass


    def action(self):
        self.game.is_paused = False

class TP_Spawn_Button(Button):
    """
    can only be use inside a world
    """
    def __init__(self,game,position,player):
        super().__init__(game,position)
        self.player = player
        self.text = "Spawn"
        self.label = self.myfont.render(self.text, 1, self.foreground)
        self.update_surface()

    def action(self):
        self.player.r.x = 150 
        self.player.r.y = 150 
        self.player.orientation = 0

class FPS_Display(Display):
    """
    can be use outside a world
    """
    def __init__(self,game,position,size=(20,20)):
        super().__init__(game,position,size)
        self.label = "FPS: "
        pass

    def content_update(self):
        self.content = str(int(self.game.clock.get_fps()))


class Health_Bar_Display(Display):
    """
    can only be use inside a world
    """
    def __init__(self,game,position,player,size=(20,20)):
        super().__init__(game,position,size)
        self.label = "Health: "
        self.player = player
        pass

    def content_update(self):
        self.content = str(int(self.player.health))

class Ammo_Display(Display):
    """
    can only be use inside a world
    """
    def __init__(self,game,position,player,size=(20,20)):
        super().__init__(game,position,size)
        self.label = "Ammo: "
        self.player = player
        pass

    def content_update(self):
        self.content = str(int(self.player.ammo))

class V_Orientation_Display(Display):
    """
    can only be use inside a world
    """
    def __init__(self,game,position,player,size=(20,20)):
        super().__init__(game,position,size)
        self.label = "V_orientation: "
        self.player = player
        pass

    def content_update(self):
        self.content = str(int(self.player.vorientation))


class Weapon_Display(Display):
    """
    can only be use inside a world
    """
    def __init__(self,game,position,player,size=(20,20)):
        super().__init__(game,position,size)
        self.label = "Weapon: "
        self.player = player
        pass

    def content_update(self):
        self.content = self.player.current_weapon.model

class H_Orientation_Display(Display):
    """
    can only be use inside a world
    """
    def __init__(self,game,position,player,size=(20,20)):
        super().__init__(game,position,size)
        self.string = "H_Orientation: "
        self.player = player
        pass

    def content_update(self):
        self.content = str(int(self.player.orientation*180/pi))

class Position_Display(Display):
    """
    can only be use inside a world
    """
    def __init__(self,game,position,player,size=(20,20)):
        super().__init__(game,position,size)
        self.string = "position: "
        self.player = player

    def content_update(self):
        self.content = str(self.player.r.x)+","+str(self.player.r.y)



#### Menu UI Compoenent ####

class Menu_Title(Display):
    def __init__(self,game,position,size=(20,20)):
        super().__init__(game,position,size)
        self.string = "An_Awesome_Name"
        self.font_size = 50
        self.background = (0,0,0,0)

        # TODO find a way to remove the 3 line below 
        self.myfont = pg.font.Font(PATH_ASSETS+"fonts/PressStart2P-Regular.ttf", 42)
        self.label = self.myfont.render(self.string, 1, self.foreground)
        self.update_size()

        self.position = self.get_position_centered_surface()

        pass

class Menu_Select_World_Button(Button):
    def __init__(self,game,position):
        self.game = game
        self.position = position
        self.ui_elements_button = [
            self.right_button(game,(60,50))
        ]

    def draw(self):
        for element in self.ui_elements_button:
            element.draw()
        for element in self.ui_elements_display:
            element.draw_without_content()

    class menu_name(Display):
        def __init__(self,game,position):
            super().__init__(game,position)
            self.string = "WORLD"
            self.myfont = pg.font.Font(PATH_ASSETS+"fonts/PressStart2P-Regular.ttf", 30)

    class right_button(Button):
        def __init__(self,game,position):
            super().__init__(game,position)
            self.text = "play"
            self.background = (0,0,255,0)
            self.background_activate = RED
            self.background_idle = self.background
            self.myfont = pg.font.Font(PATH_ASSETS+"fonts/PressStart2P-Regular.ttf", 30)
            self.label = self.myfont.render(self.text, 1, self.foreground)
            self.update_surface()
            self.position = self.get_position_centered_surface()
            self.update_surface()

        def action(self):
            print("good game")
            self.game.load_world()
            pass
    class right_button(Button):
        def __init__(self,game,position):
            super().__init__(game,position)
            self.text = "play"
            self.background = (0,0,255,0)
            self.background_activate = RED
            self.background_idle = self.background
            self.myfont = pg.font.Font(PATH_ASSETS+"fonts/PressStart2P-Regular.ttf", 30)
            self.label = self.myfont.render(self.text, 1, self.foreground)
            self.update_surface()
            self.position = self.get_position_centered_surface()
            self.update_surface()

        def action(self):
            print("good game")
            self.game.load_world()
            pass

class menu_setting(Menu):
    def __init__(self):
        pass

