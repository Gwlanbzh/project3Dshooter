
import pygame as pg
from math import pi
from config import *

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
        self.myfont = pg.font.SysFont("monospace", self.font_size)
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
    def __init__(self,game,position,size=(20,20)):
        super().__init__(game,position)
        self.lifetime = -1
        self.background_activate = RED
        self.background_idle = self.background

    def update_surface(self):
        self.update_size()
        self.surface = pg.Surface(self.size)
        self.surface.fill(self.background)
        self.surface.blit(self.label,(0,0))
        self.rect = pg.Rect(self.position[0], self.position[1], 
                            self.size[0], self.size[1])
    
    def draw(self):
        if self.lifetime > 0:
            self.lifetime -= 1
            if self.lifetime <= 0:
                # change the background back to idle
                self.background = self.background_idle
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
                    self.animate()
                    self.action()

    def action(self):
        """
        each button have one action, action define in 
        the specific button class since every button are unique
        always call by self.click()
        """
        pass

    def animate(self):
        self.background = self.background_activate
        self.surface.fill(self.background)
        self.surface.blit(self.label,(0,0))
        self.lifetime = 10
        pass

class Health_Bar():
    def __init__(self,game,position,player):
        self.player = player
        self.game = game
        self.position = position
        self.health_bar_length = 600
        self.health_ratio = player.max_health / self.health_bar_length
        self.health_change_speed = 5
        self.icon = pg.image.load(PATH_ASSETS+"heart_icon.png")
        self.icon = pg.transform.scale(self.icon,(70,70))
        self.myfont = pg.font.SysFont("creep", 17)

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
        self.game.window.blit(label, self.position)
        self.game.window.blit(self.icon,(self.position[0]-40,self.position[1]-30))
    pass

class Menu():
    pass

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
        self.content = self.player.current_weapon.name

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
        self.myfont = pg.font.SysFont("monospace", self.font_size)
        self.label = self.myfont.render(self.string, 1, self.foreground)
        self.update_size()

        self.position = self.get_position_centered_surface()

        pass

class Menu_Select_World(Menu):
    def __init__(self):
        pass

class menu_setting(Menu):
    def __init__(self):
        pass

class Play_Button(Button):
    def __init__(self):
        pass

class Quit_Game_Button(Button):
    def __init__(self):
        pass
