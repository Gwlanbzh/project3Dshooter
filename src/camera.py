from math import cos, sin, tan, atan
import pygame as pg
from pygame import Vector2 as v2
#from world import *
from game import *
from config import * # using MAX_RENDER_DISTANCE, RAY_STEP, RES_X, RES_Y

MAX_RENDER_DISTANCE = Config.MAX_RENDER_DISTANCE
RAY_STEP = Config.RAY_STEP
RES_X = Config.RES_X
RES_Y = Config.RES_Y
FOV = Config.FOV

atanfov = atan(FOV/2)
theta = lambda n : tan(atanfov * ( 1-(2*n) / RES_X) )

class Ray():
    def __init__(self, origin: v2, direction: v2):
        """
        Casts a ray in form of a straight line through the map. 
        
        direction is supposed of magnitude 1.
        
        If no wall is encontered before a distance of MAX_RENDER_DISTANCE,
        self.did_encounter is set to False, oterwise True.
        self.encountered_type
        """
        # Algorithm explanation:
        #    First, a vector is created and initialized with the origin value.
        #    Then, at each step t, the function adds RAY_STEP * direction to it
        #    and tests whether it goes inside a wall or not. This is equivalent
        #    to testing the points on a straight line with a parametric equation
        #    M(t) = origin + t*direction, every RAY_STEP.
        
        M = origin
        distance = 0
        # mobs_encountered = []  # by appending, the first to render will be the last encountered <=> last in the list.
        while map[int(M.y)//100][int(M.x)//100] == NO_W0 and distance < MAX_RENDER_DISTANCE:  # current poition not in a wall AND below max distance
            distance += RAY_STEP
            M += RAY_STEP * direction
        
        if distance == MAX_RENDER_DISTANCE:
            self.encounter_distance = -1
            self.encountered_type = None
        else:
            self.did_encounter = False
            self.encounter_distance = distance
            self.encountered_type = map[int(M.y)//100][int(M.x)//100]



def Camera():
    def __init__(self, player: Player):
        """
        Create a camera and bind it to a specific player's point of view.
        """
        self.bound_player = player
    
    def get_frame(self):
        """
        Displays elements of the environment based on the state of the world.
        Currently only supports 
        """
        n = RES_X/2  # arbitrary value for testing. TODO: loop through all pixels
        
        # calculate the coordinates of the so-defined player's view vector
        view_vector = v2(cos(self.bound_player.orientation), 
                              sin(self.bound_player.orientation))
        
        # computing the angle between the player's view vector and the ray's and
        # applying a rotation matrix of this angle to get the ray's vector.
        # This vector is demonstrated to have a magnitude of 1.
        th = theta(n)
        costh = cos(th)
        sinth = sin(th)
        ray_direction = v2(costh * view_vector.x - sinth * view_vector.y,
                           sinth * view_vector.x + costh * view_vector.y)

if __name__ == "__main__":
    game = Game()
    print("game initialized")
    
    window = pg.display.set_mode((RES_X, RES_Y))
    # show the line numbers
    ray = Ray(game.world.players[0].r, v2(1, 0))
    x = RES_X // 2
    #pg.draw.rect(window, (0, 255, 255), (x, ray.encounter_distance, ))
    pg.draw.rect(window, (0, 255, 255), (x, 200, 1, ray.encounter_distance))
    pg.display.update()
    print("ray done")
    
    
    while True:
        pg.time.delay(100)
    
