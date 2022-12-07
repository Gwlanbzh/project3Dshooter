from pygame import Vector2 as v2
from math import cos, sin, asin, acos
from config import * # using RES_X, RES_Y, FOV_X
from map import *
from render.textures import *
from render.vars import *
from render import Ray


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
        voffset = -self.bound_player.vorientation  # < 0 implies looking up
        
        # Those calls are alternate to those in the display section.
        # TODO benchmark both to keep the most efficient.
        #pg.draw.rect(window, (40, 40, 40), (1, 0, RES_X, RES_Y//2 - voffset))
        #pg.draw.rect(window, (70, 70, 70), (1, RES_Y//2 - voffset, RES_X, RES_Y//2 + voffset))
        
        rays          = []
        z_buffer      = []
        upper_heights = []
        lower_heights = []
               
        direcion_vector = v2(cos(self.bound_player.orientation),
                             sin(self.bound_player.orientation)
                            )
        
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
        
        ## skybox
        window.blit(skybox, (-int(self.bound_player.orientation//skybox_angle_per_stripe),
                             -RES_Y//2-voffset
                            ))
        
        ## walls
        for n in range(RES_X):
            # creation of the texture slice to display
            texture_array = textures[rays[n].hit_type]
            
            units_per_strip = textures_units_per_strip[rays[n].hit_type]
            strip_index = int(rays[n].block_hit_abs//units_per_strip)
            
            strip = texture_array[strip_index]
            texture_slice = pg.transform.scale(strip, (1, upper_heights[n] + lower_heights[n]))
            
            # display ceiling, wall and floor
            #pg.draw.rect(window, (94, 145, 255), (RES_X-n, 0, 1, RES_Y//2 - upper_heights[n] - voffset))
            window.blit(texture_slice,         (RES_X-n-1,
                                                RES_Y//2 - upper_heights[n] - voffset
                                               ))
            pg.draw.rect(window, (70, 70, 70), (RES_X-n-1,
                                                RES_Y//2 + lower_heights[n] - voffset-1,
                                                1,
                                                RES_Y//2 - lower_heights[n] + voffset +2
                                               ))
        
        ## sprites
        #i = 0
        bodies = self.bound_player.game.world.props + self.bound_player.game.world.mobs
        for i in range(len(bodies)):
            body = bodies[i]
            sprite = body.get_sprite()
            #print("r", body.r)
            delta_r = body.r - self.bound_player.r
            #print("delta_r", delta_r)
            vp = direcion_vector.cross(delta_r)
            
            if delta_r != v2(0, 0):   # when itering, will have to replace with "continue"
                # edge case in which we won't draw
            
                #angle = acos( direcion_vector.dot(delta_r) / (direcion_vector.magnitude() * delta_r.magnitude()) )
                
                #angle = sign(vp) * asin( abs(vp) / (direcion_vector.magnitude() * delta_r.magnitude()) )
                
                # combinaison des formules des angles avec cos est sin pour éviter les deux symétries
                angle = sign(vp) * acos( direcion_vector.dot(delta_r) / (direcion_vector.magnitude() * delta_r.magnitude()) )
                #print("angle", angle)
                
                if abs(angle) < FOV_X/2 :
                    upper_height = scr_h(body.sprite[0].get_height()-Config.VIEW_HEIGHT, delta_r.magnitude()*cos(angle))
                    lower_height = scr_h(Config.VIEW_HEIGHT, delta_r.magnitude()*cos(angle))
                    draw_coordinates = v2(RES_X//2 - theta_inv(angle) - len(body.sprite)/2, 
                                        RES_Y//2 - upper_height - voffset
                                        )
                    #print("scr_h", draw_coordinates.y+voffset)
                    
                    for x in range(len(body.sprite)):
                        window.blit(pg.transform.scale(sprite[x], (1, upper_height+lower_height)), draw_coordinates+v2(x, 0))
            
