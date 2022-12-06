from math import cos, sin, atan, sqrt
import pygame as pg
from pygame import Vector2 as v2, Vector3 as v3
from game import *
from config import * # using MAX_RENDER_DISTANCE, RAY_STEP, RES_X, RES_Y
from textures import *

VIEW_HEIGHT = Config.VIEW_HEIGHT
RES_X = Config.RES_X
RES_Y = Config.RES_Y
FOV_X = Config.FOV_X
FOV_Y = Config.FOV_Y

# function for computing the ray 's direction vector
atanfov = atan(FOV_X/2)
theta = lambda n : atan(atanfov * ( 1-(2*n) / RES_X) )

# function for computing the on-screen height of a wall segment
resfovratio = RES_Y / FOV_Y
scr_h = lambda h, d : resfovratio * (h/d)

class Ray():
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
        
        while map[y_cell][x_cell] == NO_WALL:
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
        voffset = -self.bound_player.vorientation  # < 0 implies looking up
        
        # Those calls are alternate to those in the display section.
        # TODO benchmark both to keep the most efficient.
        #pg.draw.rect(window, (40, 40, 40), (1, 0, RES_X, RES_Y//2 - voffset))
        #pg.draw.rect(window, (70, 70, 70), (1, RES_Y//2 - voffset, RES_X, RES_Y//2 + voffset))
        
        rays          = []
        z_buffer      = []
        upper_heights = []
        lower_heights = []
               
        
        for n in range(RES_X):
            
            # computing the ray's direction vector            
            th = theta(n)
            
            ray_direction = v2(cos(self.bound_player.orientation + th), 
                               sin(self.bound_player.orientation + th))
            
            # computing the ray and displaying the wall segment.
            ray = Ray(self.bound_player.r, ray_direction)
            rays.append(ray)
            
            distance = ray.distance * cos(th)
            z_buffer.append(distance)
            
            upper_heights.append(scr_h(height_map[ray.hit_type], distance))
            lower_heights.append(scr_h(VIEW_HEIGHT             , distance))
        
        
        
        # Display
        
        #window.blit(skybox, (-int(self.bound_player.orientation*skybox.get_width()/(2*pi)), 0))
        window.blit(skybox, (-int(self.bound_player.orientation//skybox_angle_per_stripe), -RES_Y//2-voffset))
        
        for n in range(RES_X):
            # creation of the texture slice to display
            texture_array = textures[rays[n].hit_type]
            
            units_per_strip = textures_units_per_strip[rays[n].hit_type]
            strip_index = int(rays[n].block_hit_abs//units_per_strip)
            
            strip = texture_array[strip_index]
            texture_slice = pg.transform.scale(strip, (1, upper_heights[n] + lower_heights[n]))
            
            # display ceiling, wall and floor
            #pg.draw.rect(window, (94, 145, 255), (RES_X-n, 0, 1, RES_Y//2 - upper_heights[n] - voffset))
            window.blit(texture_slice, (RES_X-n-1, RES_Y//2 - upper_heights[n] - voffset))
            pg.draw.rect(window, (70, 70, 70), (RES_X-n-1, RES_Y//2 + lower_heights[n] - voffset-1, 1, RES_Y//2 - lower_heights[n] + voffset +2))
