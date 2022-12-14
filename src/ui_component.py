
import pygame as pg
from math import pi

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
        self.font_size = 15
        self.myfont = pg.font.SysFont("monospace", self.font_size)
        self.background = BLACK
        self.foreground = WHITE
        self.text = "text not set"
        self.label = self.myfont.render(self.text, 1, self.foreground)

    def draw_with_content(self):
        label = self.myfont.render(self.label+self.content, 1, self.foreground ,self.background)
        self.game.window.blit(label, self.position)
        pass

    def draw_without_content(self):
        label = self.myfont.render(self.label, 1, self.foreground ,self.background)
        self.game.window.blit(label, self.position)
        pass

    def update():
        pass

    def get_position_centered_surface(self):
        pos_x,pos_y = self.position
        size_x,size_y = self.size
        return (pos_x+(size_x/2),pos_y+(size_y/2))


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
        self.background_idle = BLACK

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
        pass

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
        self.label = "H_Orientation: "
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
        self.label = "position: "
        self.player = player
        pass


class Menu_Title(Display):
    def __init__(self,game,position,size=(20,20)):
        super().__init__(game,position,size)
        self.label = "An Awesome Name"
        self.font_size = 50
        self.myfont = pg.font.SysFont("monospace", self.font_size)
        print(self.position)
        self.position = self.get_position_centered_surface()
        print(self.position)

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
