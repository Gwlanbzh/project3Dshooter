from pygame import Vector2 as v2
from config import *
from world import *
from render import Camera
from bodys import *
from hud import Hud
from bodys.creatures.path_finding import *

class Game:
    """
    Base class for a game, to be used to define new game types.
    """
    def __init__(self, map_file, draw2d, window, delta_time, clock, sound):
        """
        Important init for the game main component
        """
        self.window = window
        self.delta_time = delta_time
        self.clock = clock
        self.map_file = map_file
        self.draw2d = draw2d
        self.world = World(self,map_file) 
        self.path_finding = PathFinding(self)
        self.camera = Camera(self.world.players[0])
        self.hud = Hud(self)
        self.sound = sound
        self.is_paused = False
        self.is_abandon = False
    
    def is_game_over(self):
        return ""
    
    def run(self):
        """
        Main Game Loop 
        """

        self.world.update(self)
        self.sound.update_music()
        if self.draw2d:
            self.world.draw2d(self)
        else:
            self.camera.draw_frame(self.window)
        self.hud.update()

        self.hud.draw()

