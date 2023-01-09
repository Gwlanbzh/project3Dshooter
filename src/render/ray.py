from pygame import Vector2 as v2
from math import sqrt
from render.vars import *
from render.textures import NO_WALL


class Ray():
    def __init__(self, origin: v2, direction: v2, map, skipped_hits=0):
        """
        Casts a ray with a method based on the Digital differential analyzer algorithm.
        Explanations can be found on the web, for instance at https://www.youtube.com/watch?v=NbSee-XM7WA.
        """
        # Useful when wanting to see beyond a secret 9-tile.
        hit_count = skipped_hits + 1

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

        # coordinates of current cell the ray is in
        x_orig = int(origin.x)//100
        y_orig = int(origin.y)//100

        x_cell, y_cell = x_orig, y_orig

        side = ''  # will be set to 'x' or 'y' depending on the direction of the last move
        
        # Main loop, the DDA algorithm itself.
        while hit_count > 0:
            if x_delta < y_delta:
                x_delta += x_ratio
                x_cell += x_step
                side = 'x'
            else:
                y_delta += y_ratio
                y_cell += y_step
                side = 'y'

            if map[y_cell][x_cell] != 0:
                # wall hit
                hit_count -= 1
        
        # computation of the euclidean distance
        if side == 'x':
            self.distance = 100 * (abs((x_cell - x_orig) * x_ratio) - abs(x_rest))
        else:  # side == 'y'
            self.distance = 100 * (abs((y_cell - y_orig) * y_ratio) - abs(y_rest))
        
        self.hit_type = map[y_cell][x_cell]
        
        hit_position = origin + self.distance * direction
        
        # computation of the hit abscissa, taking into account the side of the cell that was hit.
        if side == 'x':
            if direction.x > 0:
                # hit from the left
                self.block_hit_abs = hit_position.y % 100
            else:
                # hit from the right
                self.block_hit_abs = 100 - (hit_position.y % 100)
        else:
            if direction.y > 0:
                # hit from below
                self.block_hit_abs = 100 - (hit_position.x % 100)
            else:
                # hit from above
                self.block_hit_abs = hit_position.x % 100

