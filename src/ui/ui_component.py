
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
    Abstract Class
    Display text or icon
    if display text it can have a dynamic content value
    """
    def __init__(self,window,position):
        self.window = window
        self.position_original = position
        self.font_size = 20
        self.font = pg.font.Font(PATH_ASSETS+"fonts/PressStart2P-Regular.ttf",self.font_size)
        self.background = None
        self.foreground = WHITE
        self.text = "" # should not be updated
        self.content = None # content can be updated
        self.icon = None
        self.is_center = False
        self.is_init = False

    def draw(self):
        self.window.blit(self.surface, self.position)
        pass

    def update_surface(self):
        """
        update the surface display, use for button and dynamic content
        surface can be center with is_center it will center the text around the position
        call when: init,hover,click,content updated
        """
        if self.icon == None:
            if not self.is_init: # use to refresh the font when using different font
                self.font = pg.font.Font(PATH_ASSETS+"fonts/PressStart2P-Regular.ttf",self.font_size)
            self.position = self.position_original 
            self.update_label() # update display text
            self.update_surface_size() # uptade display size after new content update
            if self.is_center: # center text/icon if is_center == true
                self.center_surface()
            self.surface = pg.Surface(self.size,pg.SRCALPHA) # allow suface to use alpha
            if self.background != None: # draw a background if set
                self.surface.fill(self.background)
            self.surface.blit(self.label,(0,0)) # draw text and content on surface
            self.rect = pg.Rect(self.position[0], self.position[1], 
                                self.size[0], self.size[1]) # create a rect that fit the surface. use by Button for colision
        else:
            self.position = self.position_original 
            self.update_surface_size() # uddate icon size useful if icon are dynamic change 
            if self.is_center: # center text/icon if is_center == true
                self.center_surface()
            self.surface = pg.Surface(self.size,pg.SRCALPHA) # allow surface to use alpha
            if self.background != None: # draw a background if set
                self.surface.fill(self.background)
            self.surface.blit(self.icon,(0,0)) # draw icon on surface
            self.rect = pg.Rect(self.position[0], self.position[1], 
                                self.size[0], self.size[1])


    def center_surface(self):
        """
        center an suface. can be icon or text
        """
        pos_x,pos_y = self.position_original
        size_x,size_y = self.size
        self.position = (pos_x-(size_x/2),pos_y-(size_y/2))

    def update_label(self):
        """
        update label only if no icon or set
        """
        if self.content == None:
            self.label = self.font.render(self.text, 1, self.foreground , self.background)
        else:
            self.label = self.font.render(self.text+self.content, 1, self.foreground ,self.background)

    def update_surface_size(self):
        """
        update surface size. can be icon or text
        """
        if self.icon == None:
            self.size = self.label.get_size()
        else: 
            self.size = self.icon.get_size()
    

class Button(Display):
    """
    sound on a button is optional
    button can be hover and click
    it can be an icon or a text
    icon don't have hover and click animation
    """
    def __init__(self,window,position,sound = None):
        super().__init__(window,position)
        self.sound = sound
        self.lifetime = -1
        self.foreground_activate = RED
        self.foreground_idle = self.foreground
        self.foreground_hover = GRAY
        self.mouse_is_over = False
        self.is_click = False
    
    def draw(self):
        if self.is_click:
            if self.lifetime <= 0:
                # change the background back to idle from activate
                self.foreground = self.foreground_idle
                self.label = self.font.render(self.text, 1, self.foreground)
                self.update_surface()
            else:
                self.lifetime -= 1
        self.window.blit(self.surface, self.position)

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
                    self.is_click = True
                    self.lifetime = 10 # time period might use pg.time.get_tick()
                    if self.sound != None:
                        self.sound.play_sound("click")
                    self.update_surface()
                    self.action()

    def action(self):
        """
        each button have one action, action define in 
        the specific button class since every button are unique
        always call by self.click()
        """
        raise Exception("A Button didn't have any action defind")
        pass

    def hover(self):
        is_colliding = self.rect.collidepoint(pg.mouse.get_pos())
        if is_colliding: #Only on the first time hover
            if not self.mouse_is_over: # play sound only once
                if self.sound != None:
                    self.sound.play_sound("hover")

            if self.is_click:
                self.foreground = self.foreground_activate
            else:
                self.foreground = self.foreground_hover

            self.update_surface()
            self.mouse_is_over = True

        elif self.mouse_is_over:

            if self.is_click:
                self.foreground = self.foreground_activate
            else:
                self.foreground = self.foreground_idle

            self.update_surface()
            self.mouse_is_over = False


class Health_Bar():
    def __init__(self,window,position,player):
        self.player = player
        self.window = window
        self.position = position
        self.health_bar_length = 400
        self.health_ratio = player.max_health / self.health_bar_length
        self.health_change_speed = 1
        self.icon = pg.image.load(PATH_ASSETS+"visual/ui/cross.png")
        self.icon = pg.transform.scale(self.icon,(70,70))
        self.myfont = pg.font.Font(PATH_ASSETS+"fonts/PressStart2P-Regular.ttf", 16)

    def draw(self):
        transition_width = 0
        transition_color = (0,0,0)

        if self.player.visual_health < self.player.health:
            self.player.visual_health += self.health_change_speed
            transition_width = int((self.player.health - self.player.visual_health) / self.health_ratio)
            transition_color = (75,141,57)

        if self.player.visual_health > self.player.health:
            self.player.visual_health -= self.health_change_speed 
            transition_width = -int((self.player.health - self.player.visual_health) / self.health_ratio)
            transition_color = (210,122,49)

        health_bar_width = int(self.player.health / self.health_ratio)
        health_bar = pg.Rect(self.position[0],self.position[1],health_bar_width,25)
        if self.player.visual_health < self.player.health:
            transition_bar = pg.Rect(health_bar.right - transition_width,self.position[1],transition_width,25)
        else:
            transition_bar = pg.Rect(health_bar.right,self.position[1],transition_width,25)


        pg.draw.rect(self.window,(31,32,49),(self.position[0],self.position[1],self.health_bar_length,25))	
        pg.draw.rect(self.window,(141,7,35),health_bar)
        pg.draw.rect(self.window,transition_color,transition_bar)	
        pg.draw.rect(self.window,(73,54,43),(self.position[0],self.position[1],self.health_bar_length,25),3)	
        label = self.myfont.render(str(self.player.health)+"/"+str(self.player.max_health), 4, (255,255,255,0))
        self.window.blit(label,(self.position[0]+30,self.position[1]+5))
        self.window.blit(self.icon,(self.position[0]-50,self.position[1]-45))

class CheckBox(Button):
    def __init__(self,window,position,sound = None):
        super().__init__(window,position)
        self.sound = sound
        self.lifetime = -1
        self.foreground_activate = RED
        self.foreground_idle = self.foreground
        self.foreground_hover = GRAY
        self.checkbox_size = 40,40
        self.icon_True = pg.image.load(PATH_ASSETS+"visual/ui/check_checkbox.png")
        self.icon_True = pg.transform.scale(self.icon_True,self.checkbox_size)
        self.icon_False = pg.image.load(PATH_ASSETS+"visual/ui/empty_checkbox.png")
        self.icon_False = pg.transform.scale(self.icon_False,self.checkbox_size)
        self.checkbox_status = False
        self.mouse_is_over = False
        self.is_click = False

    def update_surface(self):
        if self.checkbox_status:
            self.icon = self.icon_True
        else:
            self.icon = self.icon_False
        self.position = self.position_original
        self.update_surface_size()
        if self.is_center:
            self.center_surface()
        self.surface = pg.Surface(self.size,pg.SRCALPHA)
        if self.background != None:
            self.surface.fill(self.background)
        self.surface.blit(self.icon,(0,0))
        self.rect = pg.Rect(self.position[0], self.position[1], 
                            self.size[0], self.size[1])

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
                    if self.sound != None:
                        self.sound.play_sound("click")
                    self.checkbox_status = not self.checkbox_status
                    self.update_surface()
                    self.action()

        
