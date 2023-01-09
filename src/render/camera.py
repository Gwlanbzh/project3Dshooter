from pygame import Vector2 as v2
from math import cos, sin, acos
from time import time
from map import *
from render.textures import *
from render.vars import *
from render import *


class Camera():
    def __init__(self, player):
        """
        Create a camera and bind it to a specific player's point of view.
        """
        self._bound_player = player
        self._ressources = self._bound_player.game.world.ressources  # shortcut
        self._voffset = 0   # used for looking up and down
        self._hoffset = 0   # used for bobbing
        self.z_buffer = []  # see https://en.wikipedia.org/wiki/Z-buffering
    
    def _draw_skybox(self, window):
        """
        Draw the skybox; taking into account the vertical orientation of the player.
        """
        skybox, skybox_angle_per_strip = self._ressources.skybox_data
        window.blit(skybox, (-int(self._bound_player.orientation//skybox_angle_per_strip),
                             -RES_Y//2-self._voffset
                            ))
    
    def _draw_floor(self, window):
        """
        Draw the floor, taking into account the vertical orientation of the player.
        """
        pg.draw.rect(window, self._ressources.floor, (1, RES_Y//2 - self._voffset, RES_X, RES_Y//2 + self._voffset))
    
    def _draw_walls(self, window):
        """
        Cast rays, draw the walls and the floor and set self.z-buffer.
        """
        self.z_buffer = []
        map = self._bound_player.game.world.map.grid
        
        for n in range(RES_X):
            # computing the ray's direction vector.
            th = theta(n)
            
            ray_direction = v2(cos(self._bound_player.orientation + th),
                               sin(self._bound_player.orientation + th))
            
            # computing the ray.
            ray = Ray(self._bound_player.r, ray_direction, map)

            if ray.hit_type == 9 and ray.distance <= self._bound_player.size:
                # 9 is a cell type corresponding to secrets, we're not drawing them.
                # Instead, we cast a new ray to see what's behind.
                ray = Ray(self._bound_player.r, ray_direction, map)

            distance = ray.distance * cos(th)
            self.z_buffer.append(ray.distance)

            # heights (above and below the camera, respectively)
            upper_height = scr_h(height_map[ray.hit_type] - self._hoffset, distance)
            lower_height = scr_h(VIEW_HEIGHT + self._hoffset, distance)
        
        
            # creation of the texture slice to display
            texture_array = self._ressources.textures[ray.hit_type]
            
            ## determining the strip to draw on this abscissa
            units_per_strip = self._ressources.textures_units_per_strip[ray.hit_type]
            strip_index = int(ray.block_hit_abs // units_per_strip)
            strip = texture_array[strip_index]

            ## scaling to the actual size on-screen.
            texture_slice = pg.transform.scale(strip, (1, upper_height + lower_height))

            # Display
            window.blit(texture_slice, (n-1,
                                       RES_Y//2 - upper_height - self._voffset
                                       ))
    
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
            # Detect which bodies are to be drawn.
            sprite_data = body.get_sprite()
            delta_r = body.r - self._bound_player.r
            
            if delta_r.magnitude() < self._bound_player.size/2:
                # In this case the scaled strips would suck up a lot of memory,
                # so we do not draw.
                continue
            
            # computation of the angle between the line of sight of the player and the line from it to the mob.
            #
            # here, we use a mix of the two formulae that stem from the dot and cross products,
            # in order to avoid both possible symmetries
            #
            # the magnitude of the direction vector equals 1 (see its expression above), so we don't normalize it.
            vp = direcion_vector.cross(delta_r)
            distance = delta_r.magnitude()
            angle = sign(vp) * acos( direcion_vector.dot(delta_r) / distance )
            
            if abs(angle) > FOV_X/2:
                # out of the frame, there's no need to continue
                continue
            
            # If we got there the body is to display
            bodies_buffer.append((distance, angle, sprite_data))
        
        # Sorting ensures that we draw the closest sprites on top of the further.
        sorted_bodies = sorted(bodies_buffer, reverse=True)
        
        for distance, angle, sprite_data in sorted_bodies:
            sprite = sprite_data.data

            # heights (above and below the camera, respectively)
            upper_height = scr_h(sprite_data.height-(Config.VIEW_HEIGHT + self._hoffset), distance * cos(angle))
            lower_height = scr_h(Config.VIEW_HEIGHT + self._hoffset, distance * cos(angle))
            height = upper_height + lower_height

            width = scr_h(sprite_data.width, distance * cos(angle))
            px_per_stripe = width / len(sprite)
            
            # top-left coordinates of the sprite on the screen.
            draw_x, draw_y = v2(int(RES_X//2 - theta_inv(angle) - width/2),
                                  RES_Y//2 - upper_height - self._voffset
                                 )
            
            for x in range(int(width)):
                i = int(draw_x + x)

                # we must draw the strip only if it is in the frame and closer than the wall on the same abscissa.
                if 0 <= i and i < len(self.z_buffer) and self.z_buffer[i] > distance:
                    # Same method as for the walls.
                    strip_index = int(x // px_per_stripe)
                    stripe = sprite[strip_index]
                    sprite_slice = pg.transform.scale(stripe, (1, height))

                    window.blit(sprite_slice, (i, draw_y))
    
    def draw_frame(self, window):
        """
        Displays elements of the environment based on the state of the world.
        """
        # Vertical rotation (y-shearing)
        self._voffset = - self._bound_player.vorientation  # < 0 implies looking up
        # Bobbing
        self._hoffset = sin(BOBBING_FREQUENCY * time()) * BOBBING_INTENSITY * self._bound_player.v.magnitude()
        
        # Rendering
        self._draw_skybox(window)
        self._draw_floor(window)
        self._draw_walls(window)
        self._draw_sprites(window)
        self._bound_player.current_weapon.draw(self._ressources, window)
        
