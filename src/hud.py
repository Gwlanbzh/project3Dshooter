import pygame as pg;
from ui_component import *;
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
        self.menu_esc = Menu(game,(RES_X*0.5,RES_Y*0.5),"exit_test")
        self.menu_esc_is_toggle = False
        self.toggle()
        pass

    def draw(self):
        for element in self.ui_elements_display:
            element.draw_with_content()
        for element in self.ui_elements_button:
            element.draw()
        for element in self.ui_bar:
            element.draw()
        if self.menu_esc_is_toggle:
            self.menu_esc.draw()
    
    def update(self):
        self.update_content()
        pass

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
        if value == 1:
            self.toolkit = 1
            self.ui_elements_display = [FPS_Display(game,(0,0)),
                                        Health_Bar_Display(game,(0,20),self.player),
                                        Ammo_Display(game,(0,40),self.player),
                                        Weapon_Display(game,(0,60),self.player),
                                        V_Orientation_Display(game,(0,80),self.player),
                                        H_Orientation_Display(game,(0,100),self.player), 
                                        Position_Display(game,(0,120),self.player)
                                        ]
            self.ui_elements_button = [TP_Spawn_Button(game,(300,0),self.player)]
            self.ui_bar = [Health_Bar(game,(RES_X*0.03,RES_Y*0.95),self.player)]

        if value == 2:
            self.toolkit = 1
            self.ui_elements_display = [Ammo_Display(game,(0,40),self.player),
                                        Weapon_Display(game,(0,60),self.player),
                                        ]
            self.ui_elements_button = []
            self.ui_bar = [Health_Bar(game,(RES_X*0.03,RES_Y*0.96),self.player)]

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






