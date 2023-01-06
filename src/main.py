
import pygame as pg
import sys
from main_menu import MainMenu
from game import Game
from config import Config

class Main():
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode(Config.WINDOW_SIZE)
        self.GameList = None
        self.main_menu = MainMenu(self)
        self.delta_time = 1 # utiliser dans le world.update et pour les vitesses
        self.clock = pg.time.Clock() # help managing time
        self.draw2d = False
        self.game = None

        self.music = pg.mixer.Sound(Config.SOUNDS_FOLDER + "menu/RideOfTheValkyries.mp3")
        self.music.play()


        map_file = "src/assets/maps/map_dest.bin"
        # self.load_game(map_file)

    def loop(self):
        while True :
            game = self.game
            events = self.check_event()
            if game != None:
                game.run()
                self.game.delta_time = self.delta_time
                self.game.world.players[0].get_inputs(events)
                if game.is_game_over():
                    game = None

                if game.is_abandon:
                    self.unload_game()
            else :
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
                self.main_menu.over()
            else:
                self.game.hud.click(event)
                self.game.hud.over()
        return events

    def load_game(self,map_file):
        self.game = Game(map_file, self.draw2d,self.window,self.delta_time,self.clock)
        pg.mixer.stop()

    def unload_game(self):
        self.game = None

        self.music.play()

    def quit(self):
        pg.quit()  # quit pygame
        sys.exit()  # better quit, remove some error when  quiting

if __name__ == "__main__":
    main = Main()
    main.loop()
