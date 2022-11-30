from math import cos, sin, tan, atan, sqrt , atan2
import pygame as pg
from pygame import Vector2 as v2, Vector3 as v3
from game import *
from config import * # using MAX_RENDER_DISTANCE, RAY_STEP, RES_X, RES_Y
from textures import *

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
theta = lambda n : atan(atanfov * ( 1-(2*n) / RES_X) )

# function for computing the on-screen height of a wall segment
resfovratio = RES_Y / FOV
scr_h = lambda h, d : resfovratio * tan(h/d)

class Ray():
    #def __init__(self, origin: v2, direction: v2):
        #"""
        #Casts a ray in form of a straight line through the map. 
        
        #direction is supposed of magnitude 1.
        
        #If no wall is encontered before a distance of MAX_RENDER_DISTANCE,
        #self.did_encounter is set to False, oterwise True.
        #self.encountered_type
        #"""
        
        ## Algorithm explanation:
        ##    First, a vector is created and initialized with the origin's value.
        ##    Then, at each step t, the function adds RAY_STEP * direction to it
        ##    and tests whether it goes inside a wall or not. This is equivalent
        ##    to testing the points on a straight line with a parametric equation
        ##    M(t) = origin + t*direction, every RAY_STEP.
        
        #M = origin.copy()
        #distance = 0
        ## mobs_encountered = []  # by appending, the first to render will be the last encountered <=> last in the list.
        #while map[int(M.y)//100][int(M.x)//100] == NO_W0 and distance < MAX_RENDER_DISTANCE:  # current poition not in a wall AND below max distance
            #distance += RAY_STEP
            #M += RAY_STEP * direction
        
        #if distance >= MAX_RENDER_DISTANCE:
            #self.did_encounter = False
            #self.distance = -1
            #self.encountered_type = None
        #else:
            #self.did_encounter = True
            #self.distance = distance
            #self.encountered_type = map[int(M.y)//100][int(M.x)//100]
    
    def __init__(self, origin: v2, direction: v2):
        """
        Casts a ray by implementing the DDA algorithm.
        """
        x_dir, y_dir = direction

        x_ratio = sqrt(1 + (y_dir/x_dir) ** 2) if x_dir != 0 else 1e30  # lenght of the hypotenuse for a dx of 1 <=> proportionality ratio between the x side and the hypotenuse.
        y_ratio = sqrt(1 + (x_dir/y_dir) ** 2) if y_dir != 0 else 1e30  # lenght of the hypotenuse for a dy of 1 <=> proportionality ratio between the y side and the hypotenuse.
        
        # Init part
        
        if x_dir < 0:
            x_step = -1
            x_delta = (origin.x % 100) / 100 * x_ratio
            x_rest = (100 - (origin.x % 100)) / 100 * x_ratio  # what will be substracted from the total at the end of the calculation.
        else:
            x_step = 1
            x_delta = (100 - (origin.x % 100)) / 100 * x_ratio
            x_rest = (origin.x % 100) / 100 * x_ratio

        if y_dir < 0:
            y_step = -1
            y_delta = (origin.y % 100) / 100 * y_ratio
            y_rest = (100 - (origin.y % 100)) / 100 * y_ratio  # what will be substracted from the total at the end of the calculation.
        else:
            y_step = 1
            y_delta = (100 - (origin.y % 100)) / 100 * y_ratio
            y_rest = (origin.y % 100) / 100 * y_ratio


        x_orig = int(origin.x)//100  # current cell the ray is in
        y_orig = int(origin.y)//100

        x_cell, y_cell = x_orig, y_orig

        side = ''  # will be 'x' or 'y' depending on the direction of the last move
        
        # Main loop, the DDA algorithm itself
        
        while map[y_cell][x_cell] == NO_W0:
            if x_delta < y_delta:
                x_delta += x_ratio
                x_cell += x_step
                side = 'x'
            else:
                y_delta += y_ratio
                y_cell += y_step
                side = 'y'
        
        
        if side == 'x':
            self.distance = 100 * (abs((x_cell - x_orig) * x_ratio) - abs(x_rest))
        else:  # side == 'y'
            self.distance = 100 * (abs((y_cell - y_orig) * y_ratio) - abs(y_rest))
        
        self.hit_type = map[y_cell][x_cell]
        
        self.hit_position = origin + self.distance * direction
        
        if side == 'x':
            if direction.x > 0:
                self.block_hit_abs = int(self.hit_position.y % 100)
            else:
                self.block_hit_abs = int(100 - (self.hit_position.y % 100))
        else:
            if direction.y > 0:
                self.block_hit_abs = int(100 - (self.hit_position.x % 100))
            else:
                self.block_hit_abs = int(self.hit_position.x % 100)
        



class Camera():
    def __init__(self, player: Player):
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
            
            height = scr_h(WALL_HEIGHT, ray.distance * costh)
            print (height,ray.distance, atan2(ray_direction.y,ray_direction.x))
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
    
