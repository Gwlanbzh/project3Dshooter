import pygame as pg;
from ui.ui_component import *;
from ui.menus.paused_menu import PausedMenu
from config import *

from os import listdir

class Hud:
    def __init__(self,game):
        self.game = game
        self.player = game.world.players[0]
        self.toolkit = 0
        self.toolkit_prev = 1 # TODO change to 3 later 
        self.ui_elements_display = []
        self.ui_elements_button = []
        self.ui_bar = []
        self.menu_esc = PausedMenu(game,(RES_X*0.5,RES_Y*0.5))
        self.toggle()

    def draw(self):
        for element in self.ui_elements_display:
            element.draw()
        for element in self.ui_elements_button:
            element.draw()
        for element in self.ui_bar:
            element.draw()
        if self.game.is_paused:
            self.menu_esc.draw()
    
    def update(self):
        self.update_content()

    def update_content(self):
        for element in self.ui_elements_display:
            element.content_update()


    def switch(self,value):
        """
        self.toolkit value
        0 : no hud
        1 : god mode hud
        2 : gameplay 3D hud
        3 : gameplay 2D hud
        """
        game = self.game
        window = self.game.window
        if value == 1:
            self.toolkit = 1
            self.ui_elements_display = [
                                        FPS_Display(window,(0,0),game),
                                        Health_Bar_Display(window,(0,20),self.player),
                                        Ammo_Display(window,(0,40),self.player),
                                        Weapon_Display(window,(0,60),self.player),
                                        V_Orientation_Display(window,(0,80),self.player),
                                        H_Orientation_Display(window,(0,100),self.player), 
                                        Position_Display(window,(0,120),self.player)
                                        ]
            self.ui_elements_button = [TP_Spawn_Button(window,(300,0),self.player)]
            self.ui_bar = [Health_Bar(window,(RES_X*0.03,RES_Y*0.95),self.player)]

        if value == 2:
            self.toolkit = 1
            self.ui_elements_display = [
                                        Ammo_Display(window,(0,40),self.player),
                                        FPS_Display(window,(0,0),game),
                                        WeaponInventory(window,(RES_X-70,-60),self.player)
                                        # VictoryStatus((RES_X*0.5,RES_Y*0.5)(window)
                                        ]
            self.ui_elements_button = []
            self.ui_bar = [Health_Bar(window,(RES_X*0.03,RES_Y*0.96),self.player)]

    def toggle(self):
        """
        toggle god mode hud
        """
        if not self.toolkit:
            self.switch(2)
        else:
            self.toolkit = 0
            self.ui_elements_button = []
            self.ui_elements_display = []
            self.ui_bar = []

    def hover(self):
        if self.game.is_paused:
            self.menu_esc.hover()

    def click(self,event):
        for element in self.ui_elements_button:
            element.click(event)
        if self.game.is_paused:
            self.menu_esc.click(event)
class TP_Spawn_Button(Button):
    def __init__(self,window,position,player):
        super().__init__(window,position)
        self.player = player
        self.text = "Spawn"
        self.update_surface()

    def action(self):
        self.player.r.x = 150 
        self.player.r.y = 150 
        self.player.orientation = 0

class FPS_Display(Display):
    """
    TODO
    """
    def __init__(self,window,position,main):
        super().__init__(window,position)
        self.main = main
        self.text = "FPS: "
        self.update_surface()

    def content_update(self):
        self.content = str(int(self.main.clock.get_fps()))
        self.update_surface()


class Health_Bar_Display(Display):
    def __init__(self,window,position,player):
        super().__init__(window,position)
        self.text = "Health: "
        self.player = player
        self.update_surface()

    def content_update(self):
        self.content = str(int(self.player.health))
        self.update_surface()

class Ammo_Display(Display):
    def __init__(self,window,position,player,):
        super().__init__(window,position,)
        self.text = "Ammo: "
        self.player = player
        self.update_surface()

    def content_update(self):
        self.content = str(int(self.player.ammo))
        self.update_surface()

class V_Orientation_Display(Display):
    def __init__(self,window,position,player,):
        super().__init__(window,position,)
        self.text = "V_orientation: "
        self.player = player
        self.update_surface()

    def content_update(self):
        self.content = str(int(self.player.vorientation))
        self.update_surface()


class Weapon_Display(Display):
    def __init__(self,window,position,player,):
        super().__init__(window,position,)
        self.text = "Weapon: "
        self.player = player
        self.update_surface()

    def content_update(self):
        self.content = self.player.current_weapon.model
        self.update_surface()

class H_Orientation_Display(Display):
    def __init__(self,window,position,player,):
        super().__init__(window,position,)
        self.text = "H_Orientation: "
        self.player = player
        self.update_surface()

    def content_update(self):
        self.content = str(int(self.player.orientation*180/pi))
        self.update_surface()

class Position_Display(Display):
    def __init__(self,window,position,player,):
        super().__init__(window,position)
        self.text = "position: "
        self.player = player
        self.update_surface()

    def content_update(self):
        self.content = str(self.player.r.x)+","+str(self.player.r.y)
        self.update_surface()

class WeaponInventory():
    def __init__(self,window,position,player):
        self.player = player
        self.window = window
        self.position = position
        self.size_icon = 70,70
        self.ui_component_display = [WeaponInventorySlot(self.window,(self.position[0],self.position[1]+70*weapon().key),weapon().model,self.size_icon,weapon().key) for index,weapon in enumerate(self.player.weapons)]

    def draw(self):
        for element in self.ui_component_display:
            element.draw()

    def content_update(self):
        self.ui_component_display = [WeaponInventorySlot(self.window,(self.position[0],self.position[1]+70*weapon().key),weapon().model,self.size_icon,weapon().key) for index,weapon in enumerate(self.player.weapons)]
        pass

class WeaponInventorySlot():
    def __init__(self,window,position,model,size_icon,number):
        self.ui_component_display = [
            WeaponInventorySlotImage(window,position,model,size_icon),
            WeaponInventorySlotNumber(window,position,size_icon,number)
        ]

    def draw(self):
        for element in self.ui_component_display:
            element.draw()
class WeaponInventorySlotImage(Display):
    def __init__(self,window,position,model,size_icon):
        super().__init__(window,position,)
        path = Config.SPRITES_DIR+"weapons/"
        file = listdir(path + model)[0]
        self.icon = pg.image.load(path+model+"/"+file )
        self.icon = pg.transform.scale(self.icon,size_icon)
        self.update_surface()

    def content_update(self):
        pass

class WeaponInventorySlotNumber(Display):
    def __init__(self, window, position,size_icon,number):
        super().__init__(window, (position[0],position[1]+size_icon[0]-20))
        self.text = str(number)
        self.update_surface()