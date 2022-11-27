
from pygame import Vector2 as v2
from map import *
from math import sqrt

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
        