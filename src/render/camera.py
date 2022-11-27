import pygame as pg
from math import cos, sin, tan, atan, sqrt

from pygame import Vector2 as v2, Vector3 as v3

from config import * # using MAX_RENDER_DISTANCE, RAY_STEP, RES_X, RES_Y
from textures import *
from map import *
from textures import *
from render import Ray

BLACK = v3(0, 0, 0)
CYAN = v3(0, 255, 255)

DISTANCE_FADING = Config.DISTANCE_FADING

WALL_HEIGHT = Config.WALL_HEIGHT
MAX_RENDER_DISTANCE = Config.MAX_RENDER_DISTANCE
RAY_STEP = Config.RAY_STEP
RES_X = Config.RES_X
RES_Y = Config.RES_Y
FOV = Config.FOV

# function for computing the ray 's direction vector
atanfov = atan(FOV/2)
theta = lambda n : tan(atanfov * ( 1-(2*n) / RES_X) )

# function for computing the on-screen height of a wall segment
resfovratio = RES_Y / FOV
scr_h = lambda h, d : resfovratio * tan(h/d)

class Camera():
    def __init__(self, player):
        """
        Create a camera and bind it to a specific player's point of view.
        """
        self.bound_player = player
    
    def draw_frame(self, window):
        """
        Displays elements of the environment based on the state of the world.
        Currently only supports 
        """
        window.fill(BLACK)
        
        # calculate the coordinates of the so-defined player's view vector
        view_vector = v2(cos(self.bound_player.orientation), 
                         sin(self.bound_player.orientation))
        
        for n in range(RES_X):
            
            # computing the angle between the player's view vector and the ray's and
            # applying a rotation matrix of this angle to get the ray's vector.
            # This vector is demonstrated to have a magnitude of 1.
            
            th = theta(n)
            costh = cos(th)
            sinth = sin(th)
            ray_direction = v2(costh * view_vector.x - sinth * view_vector.y,
                               sinth * view_vector.x + costh * view_vector.y)
            
            # finally, computing the ray and displaying the wall segment.
            ray = Ray(self.bound_player.r, ray_direction)
            
            height = scr_h(WALL_HEIGHT, ray.distance)
            if height < 1:
                height = 1
            
            #pg.draw.rect(window, tuple(colors[ray.hit_type] /(DISTANCE_FADING ** ray.distance)), (RES_X-n, RES_Y//2 - height//2, 1, height))
            texture_array = textures[textures_map[ray.hit_type]]
            units_per_strip = 100/len(texture_array)
            strip_index = int(ray.block_hit_abs//units_per_strip)
            strip = texture_array[strip_index]
            #print(ray.block_hit_abs//int(100/len(texture_array)))
            #column = texture_array[ray.block_hit_abs//int(100/len(texture_array))]
            texture_slice = pg.transform.scale(strip, (1, height))
            window.blit(texture_slice, (RES_X-n, RES_Y//2 - height//2))


if __name__ == "__main__":
    # FIXME testing stuff, to delete.
    
    from time import time
    from game import Game

    game = Game()
    print("game initialized")
    
    window = pg.display.set_mode((RES_X, RES_Y))
    
    camera = Camera(game.world.players[0])
    
    t = time()
    camera.draw_frame(window)
    print(time()-t)
    
    pg.display.update()
    
    
    while True:
        pg.time.delay(100)
    
