import pygame as pg;
from ui.ui_component import *;
from ui.menus.paused_menu import PausedMenu
from config import *

class Hud:
    def __init__(self,game):
        self.game = game
        self.player = game.world.players[0]
        self.toolkit = 0
        self.toolkit_prev = 1 # TODO change to 3 later 
        self.ui_elements_display = []
        self.ui_elements_button = []
        self.ui_bar = []
        self.menu_esc = PausedMenu(game,(RES_X*0.5,RES_Y*0.5),"exit_test")
        self.menu_esc_is_toggle = False
        self.toggle()

    def draw(self):
        for element in self.ui_elements_display:
            element.draw()
        for element in self.ui_elements_button:
            element.draw()
        for element in self.ui_bar:
            element.draw()
        if self.menu_esc_is_toggle:
            self.menu_esc.draw()
    
    def update(self):
        self.update_content()

    def update_content(self):
        for element in self.ui_elements_display:
            element.content_update()

    def click(self,event):
        for element in self.ui_elements_button:
            element.click(event)
        if self.menu_esc_is_toggle:
            for element in self.menu_esc.ui_elements_button:
                element.click(event)

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
            self.ui_elements_display = [Ammo_Display(window,(0,40),self.player),
                                        Weapon_Display(window,(0,60),self.player),
                                        FPS_Display(window,(0,0),game),
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
        if self.menu_esc_is_toggle:
            for element in self.menu_esc.ui_elements_button:
                element.hover()

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