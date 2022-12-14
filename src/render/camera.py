from pygame import Vector2 as v2
from math import cos, sin, acos
from config import *  # using RES_X, RES_Y, FOV_X
from map import *
from render.textures import *
from render.vars import *
from render.sky import skybox, skybox_angle_per_stripe
from render import *


class Camera():
    def __init__(self, player):
        """
        Create a camera and bind it to a specific player's point of view.
        """
        self.bound_player = player
        self.voffset = 0
    
    def draw_skybox(self, window):
        """
        Draw the skybox.
        """
        window.blit(skybox, (-int(self.bound_player.orientation//skybox_angle_per_stripe),
                             -RES_Y//2-self.voffset
                            ))
    
    def draw_walls(self, window):
        """
        Cast rays, draw the walls and the floor and returns a z-buffer.
        """
        rays          = []
        z_buffer      = []
        upper_heights = []
        lower_heights = []
        
        map = self.bound_player.game.world.map.map
        
        for n in range(RES_X):
            
            # computing the ray's direction vector            
            th = theta(n)
            
            ray_direction = v2(cos(self.bound_player.orientation + th), 
                               sin(self.bound_player.orientation + th))
            
            # computing the ray and displaying the wall segment.
            ray = Ray(self.bound_player.r, ray_direction, map)
            rays.append(ray)
            
            distance = ray.distance * cos(th)
            z_buffer.append(ray.distance)
            
            upper_heights.append(scr_h(height_map[ray.hit_type], distance))
            lower_heights.append(scr_h(VIEW_HEIGHT             , distance))
        
        
        for n in range(RES_X):
            # creation of the texture slice to display
            texture_array = global_textures[rays[n].hit_type]
            
            units_per_strip = textures_units_per_strip[rays[n].hit_type]
            strip_index = int(rays[n].block_hit_abs//units_per_strip)
            
            strip = texture_array[strip_index]
            texture_slice = pg.transform.scale(strip, (1, upper_heights[n] + lower_heights[n]))
            
            #texture_slice = pg.transform.scale(global_textures[rays[n].hit_type][int(rays[n].block_hit_abs//units_per_strip)], (1, upper_heights[n] + lower_heights[n]))
            
            # display ceiling, wall and floor
            #pg.draw.rect(window, (94, 145, 255), (RES_X-n, 0, 1, RES_Y//2 - upper_heights[n] - voffset))
            window.blit(texture_slice,         (RES_X-n-1,
                                                RES_Y//2 - upper_heights[n] - self.voffset
                                               ))
            #pg.draw.rect(window, GROUND_COLOR, (RES_X-n-1,
                                                #RES_Y//2 + lower_heights[n] - self.voffset-1,
                                                #1,
                                                #RES_Y//2 - lower_heights[n] + self.voffset +2
                                               #))
        
        return z_buffer
    
    def draw_sprites(self, window, z_buffer):
        """
        Draw sprites on screen with a z_buffer provided by the ray casting in self.draw_walls().
        """
        direcion_vector = v2(cos(self.bound_player.orientation),
                             sin(self.bound_player.orientation)
                            )

        bodies = self.bound_player.game.world.props + self.bound_player.game.world.pickables + self.bound_player.game.world.mobs
        bodies_buffer = []
        for body in bodies:
            # detect bodies to draw and sort them, their distance and angle.
            #body = bodies[i]
            sprite_structure = body.get_sprite()
            delta_r = body.r - self.bound_player.r
            
            #if delta_r == v2(0, 0):   # when itering, will have to replace with "continue"
            if delta_r.magnitude() < self.bound_player.size:   # when itering, will have to replace with "continue"
                # edge case in which we won't draw
                continue
                
            vp = direcion_vector.cross(delta_r)
            distance = delta_r.magnitude()
            
            # combinaison des formules des angles avec cos est sin pour éviter les deux symétries
            # la norme du vecteur direction est 1
            angle = sign(vp) * acos( direcion_vector.dot(delta_r) / distance )
            
            if abs(angle) > FOV_X/2:
                # out of frame, no need to continue
                continue
            
            bodies_buffer.append((distance, angle, sprite_structure))
        
        sorted_bodies = sorted(bodies_buffer, reverse=True)
        
        for distance, angle, sprite_structure in sorted_bodies:
            upper_height = scr_h(sprite_structure.height-Config.VIEW_HEIGHT, distance)
            lower_height = scr_h(Config.VIEW_HEIGHT, distance)
            height = upper_height + lower_height

            width = scr_h(sprite_structure.width, distance)
            px_per_stripe = width / len(sprite_structure.sprite)
            
            draw_x, draw_y = v2(int(RES_X//2 - theta_inv(angle) - width/2), 
                                  RES_Y//2 - upper_height - self.voffset
                                 )
            
            for x in range(int(width)):
                strip_index = int(x // px_per_stripe)
                stripe = sprite_structure.sprite[strip_index]
                sprite_slice = pg.transform.scale(stripe, (1, height))
                
                i = int(draw_x + x)
                if 0 <= i and i < len(z_buffer) and z_buffer[i] > distance:
                    window.blit(sprite_slice, (i, draw_y))
    
    def draw_frame(self, window):
        """
        Displays elements of the environment based on the state of the world.
        Currently only supports 
        """
        self.voffset = - self.bound_player.vorientation  # < 0 implies looking up
        
        # This call is alternate to those in draw_walls.
        # TODO benchmark both to keep the most efficient.
        pg.draw.rect(window, (70, 70, 70), (1, RES_Y//2 - self.voffset, RES_X, RES_Y//2 + self.voffset))
        
        self.draw_skybox(window)
        z_buffer = self.draw_walls(window)[::-1]
        self.draw_sprites(window, z_buffer)
        
        
        
