import pygame as pg;
from math import pi

BLACK = pg.Color(0,0,0)
GRAY = pg.Color(170,170,170) 
WHITE = pg.Color(255,255,255) 

class Hud:
    def __init__(self,game):
        self.game = game
        self.player = game.world.players[0]
        self.toolkit = 0
        self.toolkit_prev = 1 # TODO change to 3 later 
        self.ui_element_display = []
        self.ui_element_button = []
        pass

    def draw(self):
        for element in self.ui_element_display:
            element.draw()
        for element in self.ui_element_button:
            element.draw()
        pass
    
    def update(self):
        for element in self.ui_element_display:
            element.update()
        pass

    def click(self,event):
        for element in self.ui_element_button:
            element.click(event)

    def toolkit_ui(self,value):
        """
        self.toolkit value
        0 : no hud
        1 : god mode hud
        2 : gameplay 3D hud
        3 : gameplay 2D hud
        """
        game = self.game
        print("b")
        if value == 1:
            self.toolkit = 1
            self.ui_element_display = [FPS_Display(game,(0,0)),
                                    Health_Bar_Display(game,(0,20),self.player),
                                    Ammo_Display(game,(0,40),self.player),
                                    Weapon_Display(game,(0,60),self.player),
                                    V_Orientation_Display(game,(0,80),self.player),
                                    H_Orientation_Display(game,(0,100),self.player), 
                                    Position_Display(game,(0,100),self.player)]
            self.ui_element_button = [TP_Spawn(game,(200,0),self.player)]

    def toolkit_toggle(self):
        if not self.toolkit:
            self.toolkit_ui(1)
        else:
            self.toolkit = 0
            self.ui_element_button = []
            self.ui_element_display = []


class Button:
    def __init__(self,game,position,player,size=(20,20)):
        self.game = game
        self.player = player
        self.position = position
        self.myfont = pg.font.SysFont("monospace", 30)
        self.background = BLACK
        self.foreground = WHITE
        self.label = self.myfont.render(self.text, 1, self.foreground)

        size_x,size_y = size
        size_label_x,size_label_y = self.label.get_size()

        if size_x < size_label_x:
            size_x = size_label_x
        if size_y < size_label_y:
            size_y = size_label_y
        self.size = size_x,size_y      

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


class display:
    def __init__(self,game,position,size=(20,20)):
        self.game = game
        self.position = position
        self.size = size
        self.background = pg.Color(0, 0, 0, 0)
        self.foreground = pg.Color(255, 255, 255, 255)
        self.myfont = pg.font.SysFont("monospace", 15)
        self.label = ""
        self.content = ""

    def draw(self):
        label = self.myfont.render(self.label+self.content, 1, self.foreground ,self.background)
        self.game.window.blit(label, self.position)
        pass

    def update():
        pass

class TP_Spawn(Button):
    def __init__(self,game,position,player):
        self.text = "Spawn"
        super().__init__(game,position,player)

    def click(self,event):
        x, y = pg.mouse.get_pos()
        if event.type == pg.MOUSEBUTTONDOWN:
            if pg.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.background = pg.Color(255,55,255,255)
                    self.surface.fill(self.background)
                    self.surface.blit(self.label,(0,0))
                    self.lifetime = 120



class FPS_Display(display):
    def __init__(self,game,position,size=(20,20)):
        super().__init__(game,position,size)
        self.label = "FPS: "
        pass

    def update(self):
        self.content = str(int(self.game.clock.get_fps()))


class Health_Bar_Display(display):
    def __init__(self,game,position,player,size=(20,20)):
        super().__init__(game,position,size)
        self.label = "Health: "
        self.player = player
        pass

    def update(self):
        self.content = str(int(self.player.health))

class Ammo_Display(display):
    def __init__(self,game,position,player,size=(20,20)):
        super().__init__(game,position,size)
        self.label = "Ammo: "
        self.player = player
        pass

    def update(self):
        self.content = str(int(self.player.ammo))

class V_Orientation_Display(display):
    def __init__(self,game,position,player,size=(20,20)):
        super().__init__(game,position,size)
        self.label = "V_orientation: "
        self.player = player
        pass

    def update(self):
        self.content = str(int(self.player.vorientation))


class Weapon_Display(display):
    def __init__(self,game,position,player,size=(20,20)):
        super().__init__(game,position,size)
        self.label = "Weapon: "
        self.player = player
        pass

    def update(self):
        self.content = self.player.current_weapon.name

class H_Orientation_Display(display):
    def __init__(self,game,position,player,size=(20,20)):
        super().__init__(game,position,size)
        self.label = "H_Orientation: "
        self.player = player
        pass

    def update(self):
        self.content = str(int(self.player.orientation*180/pi))

class Position_Display(display):
    def __init__(self,game,position,player,size=(20,20)):
        super().__init__(game,position,size)
        self.label = "position: "
        self.player = player
        pass

    def update(self):
        self.content = str((self.player.r.x))+","+str(self.player.r.y)


def get_surface_size():
    pass