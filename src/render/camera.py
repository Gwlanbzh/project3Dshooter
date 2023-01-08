from pygame import Vector2 as v2
from math import cos, sin, acos
from time import time
from map import *
from render.textures import *
from render.vars import *
#from render.sky import skybox, skybox_angle_per_stripe
from render import *


class Camera():
    def __init__(self, player):
        """
        Create a camera and bind it to a specific player's point of view.
        """
        self._bound_player = player
        self._ressources = self._bound_player.game.world.ressources  # shortcut
        self._voffset = 0  # used for looking up and down
        self._hoffset = 0  # used for bobbing
        self.z_buffer = []
    
    def _draw_skybox(self, window):
        """
        Draw the skybox.
        """
        skybox, skybox_angle_per_stripe = self._ressources.skybox_data
        window.blit(skybox, (-int(self._bound_player.orientation//skybox_angle_per_stripe),
                             -RES_Y//2-self._voffset
                            ))
    
    def _draw_floor(self, window):
        """
        Draw the floor.
        """
        pg.draw.rect(window, self._ressources.floor, (1, RES_Y//2 - self._voffset, RES_X, RES_Y//2 + self._voffset))
    
    def _draw_walls(self, window):
        """
        Cast rays, draw the walls and the floor and returns a z-buffer.
        """
        rays          = []
        z_buffer      = []
        upper_heights = []
        lower_heights = []
        
        map = self._bound_player.game.world.map.grid
        
        for n in range(RES_X):
            
            # computing the ray's direction vector            
            th = theta(n)
            
            ray_direction = v2(cos(self._bound_player.orientation + th),
                               sin(self._bound_player.orientation + th))
            
            # computing the ray and displaying the wall segment.
            ray = Ray(self._bound_player.r, ray_direction, map)
            
            distance = ray.distance * cos(th)
            z_buffer.append(ray.distance)

            if ray.hit_type == 9 and distance <= self._bound_player.size:
                #  9 is a cell type corresponding to secrets, we're not drawing them.
                # Instead, we cast a new ray to see what's behind.
                ray = Ray(self._bound_player.r, ray_direction, map)
                distance = ray.distance * cos(th)
                z_buffer[-1] = ray.distance
            
            upper_height = scr_h(height_map[ray.hit_type] - self._hoffset, distance)
            lower_height = scr_h(VIEW_HEIGHT + self._hoffset, distance)
        
        
            # creation of the texture slice to display
            texture_array = self._ressources.textures[ray.hit_type]
            
            units_per_strip = self._ressources.textures_units_per_strip[ray.hit_type]
            strip_index = int(ray.block_hit_abs//units_per_strip)
            
            strip = texture_array[strip_index]
            #if upper_heights[n] + lower_heights[n] > 0:
            texture_slice = pg.transform.scale(strip, (1, upper_height + lower_height))
            
            #texture_slice = pg.transform.scale(global_textures[rays[n].hit_type][int(rays[n].block_hit_abs//units_per_strip)], (1, upper_heights[n] + lower_heights[n]))
            
            # display ceiling, wall and floor
            #pg.draw.rect(window, (94, 145, 255), (RES_X-n, 0, 1, RES_Y//2 - upper_heights[n] - _voffset))

            window.blit(texture_slice,         (RES_X-n-1,
                                                RES_Y//2 - upper_height - self._voffset
                                               ))
            #pg.draw.rect(window, GROUND_COLOR, (RES_X-n-1,
                                                #RES_Y//2 + lower_heights[n] - self._voffset-1,
                                                #1,
                                                #RES_Y//2 - lower_heights[n] + self._voffset +2
                                               #))
        
        self.z_buffer = z_buffer[::-1]
    
    def _draw_sprites(self, window):
        """
        Draw sprites on screen with a z_buffer provided by the ray casting in self._draw_walls().
        """
        direcion_vector = v2(cos(self._bound_player.orientation),
                             sin(self._bound_player.orientation)
                            )

        bodies = self._bound_player.game.world.props + self._bound_player.game.world.pickables + self._bound_player.game.world.mobs
        bodies_buffer = []
        for body in bodies:
            # detect bodies to draw and sort them, their distance and angle.
            #body = bodies[i]
            sprite_data = body.get_sprite()
            delta_r = body.r - self._bound_player.r
            
            #if delta_r == v2(0, 0):   # when itering, will have to replace with "continue"
            if delta_r.magnitude() < self._bound_player.size/2:   # when itering, will have to replace with "continue"
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
            
            bodies_buffer.append((distance, angle, sprite_data))
        
        sorted_bodies = sorted(bodies_buffer, reverse=True)
        
        for distance, angle, sprite_data in sorted_bodies:
            sprite = sprite_data.data
            upper_height = scr_h(sprite_data.height-(Config.VIEW_HEIGHT + self._hoffset), distance * cos(angle))
            lower_height = scr_h(Config.VIEW_HEIGHT + self._hoffset, distance * cos(angle))
            height = upper_height + lower_height

            width = scr_h(sprite_data.width, distance * cos(angle))
            px_per_stripe = width / len(sprite)
            
            draw_x, draw_y = v2(int(RES_X//2 - theta_inv(angle) - width/2), 
                                  RES_Y//2 - upper_height - self._voffset
                                 )
            
            for x in range(int(width)):
                i = int(draw_x + x)

                if 0 <= i and i < len(self.z_buffer) and self.z_buffer[i] > distance:
                    strip_index = int(x // px_per_stripe)
                    stripe = sprite[strip_index]
                    sprite_slice = pg.transform.scale(stripe, (1, height))

                    window.blit(sprite_slice, (i, draw_y))
    
    def draw_frame(self, window):
        """
        Displays elements of the environment based on the state of the world.
        Currently only supports 
        """
        self._voffset = - self._bound_player.vorientation  # < 0 implies looking up
        self._hoffset = sin(BOBBING_FREQUENCY * time()) * BOBBING_INTENSITY * self._bound_player.v.magnitude()
        print(self._hoffset)
        
        self._draw_skybox(window)
        self._draw_floor(window)
        self._draw_walls(window)
        self._draw_sprites(window)
        self._bound_player.current_weapon.draw(window)
        
