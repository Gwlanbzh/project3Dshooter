
import pygame as pg
import sys
from menu import MainMenu
from game import Game
from config import Config

class Main():
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode(Config.WINDOW_SIZE)
        self.main_menu = MainMenu(self)
        self.delta_time = 1 # utiliser dans le world.update et pour les vitesses
        self.clock = pg.time.Clock() # help managing time
        self.draw2d = True
        self.game = None
        self.game = Game("src/assets/maps/map_dest.bin", self.draw2d,self.window,self.delta_time,self.clock)

    def loop(self):
        while True :
            game = self.game
            if game != None:
                game.run()
                if game.is_game_over():
                    game = None
            else :
                self.main_menu.run()

            fps = self.clock.get_fps()
            pg.display.update()
            self.delta_time =  self.clock.tick(Config.FRAME_RATE)
            pg.display.set_caption(f"{fps:.2f}")

    def check_event(self):
        """
        Check if Client ask to quit
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()

            if self.game != None:
                self.main_menu.click(event)
                self.main_menu.over()
            else:
                self.game.hud.click(event)
                self.game.hud.over()


    def load_game(self,map_file):
        self.game = Game("src/assets/maps/map_dest.bin", self.draw2d,self.window,self.delta_time,self.clock)

    def unload_game(self):
        self.game = None

    def quit(self):
        pg.quit()  # quit pygame
        sys.exit()  # better quit, remove some error when  quiting

if __name__ == "__main__":
    main = Main()
    main.loop()
