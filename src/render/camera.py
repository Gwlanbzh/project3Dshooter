from pygame import Vector2 as v2
from math import cos, sin
from config import * # using MAX_RENDER_DISTANCE, RAY_STEP, RES_X, RES_Y
from map import *
from render.textures import *
from render.vars import *
from render import Ray
from bodys import Player


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
