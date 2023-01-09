
import pygame as pg
import sys
from ui.menus.main_menu import MainMenu
from levels import *
from config import Config
from sound import Sound

class Main():
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode(Config.WINDOW_SIZE)
        self.levels = levels
        self.levels_list = [ (level_name , False) if i == 0 else (level_name,True) for i , level_name in enumerate(self.levels)] 
        self.current_level_index = 0
        self.max_level_index = len(self.levels)
        self.sound = Sound()
        self.main_menu = MainMenu(self)
        self.delta_time = 1 # utiliser dans le world.update et pour les vitesses
        self.clock = pg.time.Clock() # help managing time
        self.draw2d = False
        self.game = None

        self.music = pg.mixer.Sound(Config.SOUNDS_FOLDER + "menu/RideOfTheValkyries.mp3")
        self.music.play()
        self.sound.shut_music()

        # self.load_game(map_file)

    def loop(self):
        while True :
            game = self.game
            events = self.check_event()
            if game != None: # if game is initialize
                game.run()
                self.game.delta_time = self.delta_time
                self.game.world.players[0].get_inputs(events)
                if self.game.is_paused:
                    for event in pg.event.get():
                        if event.type == pg.KEYDOWN:
                            if event.key == pg.K_ESCAPE:
                                self.game.is_paused = False
                if game.is_game_over() == "defeat":
                    # self.unload_game()
                    pass
                elif game.is_game_over() == "victory":
                    # self.hud.victory() 
                    self.current_level_index += 1
                    if self.current_level_index > self.max_level_index:
                        self.current_level_index = self.main_level_index 
                    level = self.levels[self.levels_list[self.current_level_index][0]]
                    self.load_game(level)
                elif game.is_abandon:
                    self.unload_game()
            else : # else run menu
                self.main_menu.run()

            fps = self.clock.get_fps()
            pg.display.update()
            self.delta_time = self.clock.tick(Config.FRAME_RATE)
            pg.display.set_caption(f"{fps:.2f}")
            pg.event.pump()

    def check_event(self):
        """
        Check if Client ask to quit
        """
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                self.quit()

            if self.game == None:
                self.main_menu.click(event)
                self.main_menu.hover()
            else:
                self.game.hud.click(event)
                self.game.hud.hover()
        
        self.cursor_visibility()
        return events

    def load_game(self,level):
        self.game = level["type"](level["map_file"], self.draw2d,self.window,self.delta_time,self.clock,self.sound)
        pg.mixer.stop()

    def unload_game(self):
        self.game = None
        self.music.play()

    def quit(self):
        pg.quit()  # quit pygame
        sys.exit()  # better quit, remove some error when  quiting

    def cursor_visibility(self):
        if self.game == None or self.game.is_paused:
            pg.event.set_grab(True)
            pg.mouse.set_visible(True)
        else:
            pg.event.set_grab(True)
            pg.mouse.set_visible(False)

if __name__ == "__main__":
    main = Main()
    main.loop()
