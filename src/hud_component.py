
import pygame as pg
from math import pi

BLACK = pg.Color(0,0,0)
GRAY = pg.Color(170,170,170) 
WHITE = pg.Color(255,255,255) 

class Display:
    def __init__(self,game,position,size=(20,20)):
        self.game = game
        self.size = size
        self.position = position
        self.myfont = pg.font.SysFont("monospace", 30)
        self.background = BLACK
        self.foreground = WHITE
        self.text = "text not set"
        self.label = self.myfont.render(self.text, 1, self.foreground)

    def draw(self):
        label = self.myfont.render(self.label+self.content, 1, self.foreground ,self.background)
        self.game.window.blit(label, self.position)
        pass

    def update():
        pass

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
    def __init__(self,game,position,size=(20,20)):
        super().__init__(game,position)
        self.update_size()
        self.surface = pg.Surface(self.size)
        self.surface.fill(self.background)
        self.surface.blit(self.label,(0,0))
        self.rect = pg.Rect(self.position[0], self.position[1], 
                            self.size[0], self.size[1])
        self.lifetime = -1
    
    def draw(self):
        if self.lifetime > 0:
            self.lifetime -= 1
            if self.lifetime <= 0:
                self.background = pg.Color(0,55,255,255)
                self.surface.fill(self.background)
                self.surface.blit(self.label,(0,0))
        self.game.window.blit(self.surface, self.position)

    def click(self,event):
        pass

class TP_Spawn(Button):
    def __init__(self,game,position,player):
        self.text = "Spawn"
        super().__init__(game,position)

    def click(self,event):
        x, y = pg.mouse.get_pos()
        if event.type == pg.MOUSEBUTTONDOWN:
            if pg.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.background = pg.Color(255,55,255,255)
                    self.surface.fill(self.background)
                    self.surface.blit(self.label,(0,0))
                    self.lifetime = 120

class FPS_Display(Display):
    def __init__(self,game,position,size=(20,20)):
        super().__init__(game,position,size)
        self.label = "FPS: "
        pass

    def update(self):
        self.content = str(int(self.game.clock.get_fps()))


class Health_Bar_Display(Display):
    def __init__(self,game,position,player,size=(20,20)):
        super().__init__(game,position,size)
        self.label = "Health: "
        self.player = player
        pass

    def update(self):
        self.content = str(int(self.player.health))

class Ammo_Display(Display):
    def __init__(self,game,position,player,size=(20,20)):
        super().__init__(game,position,size)
        self.label = "Ammo: "
        self.player = player
        pass

    def update(self):
        self.content = str(int(self.player.ammo))

class V_Orientation_Display(Display):
    def __init__(self,game,position,player,size=(20,20)):
        super().__init__(game,position,size)
        self.label = "V_orientation: "
        self.player = player
        pass

    def update(self):
        self.content = str(int(self.player.vorientation))


class Weapon_Display(Display):
    def __init__(self,game,position,player,size=(20,20)):
        super().__init__(game,position,size)
        self.label = "Weapon: "
        self.player = player
        pass

    def update(self):
        self.content = self.player.current_weapon.name

class H_Orientation_Display(Display):
    def __init__(self,game,position,player,size=(20,20)):
        super().__init__(game,position,size)
        self.label = "H_Orientation: "
        self.player = player
        pass

    def update(self):
        self.content = str(int(self.player.orientation*180/pi))

class Position_Display(Display):
    def __init__(self,game,position,player,size=(20,20)):
        super().__init__(game,position,size)
        self.label = "position: "
        self.player = player
        pass

    def update(self):
        self.content = str((self.player.r.x))+","+str(self.player.r.y)