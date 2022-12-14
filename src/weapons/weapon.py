import pygame as pg
from pygame import Vector2 as v2
from math import hypot, atan, acos, cos, sin, tau, pi
from render.ray import Ray
from render import *
from config import Config
pi_2 = pi / 2

class Weapon():
    def __init__(self):
        self.dmg = 10
        self.delay = 1000 # en ms
        self.range = 100 # 100 -> largeur d'un carré

        self.last_shot_time = - self.delay # moment at which the last shot was fired
                                           # - self.delay to avoid animation at init of the game
        
        self.time_between_sprites = 200
        self.sprite = load_weapon() # from render.weapons
        self.image_index = 0
    
    def hit_scan(self, map, pos, orientation, mob_list):
        """
        check if a mob is touch on click and act in consequence.
        """
        t = pg.time.get_ticks()
        if t - self.last_shot_time > self.delay: # 100 ms between shots 
            self.last_shot_time = t
            self.play_sound()
        
            sorted_mob_list = [(self.dist(pos, mob), mob) for mob in mob_list]
            sorted_mob_list = sorted(sorted_mob_list)

            for dist, mob in sorted_mob_list:
                # test mur
                direction = v2(cos(mob.orientation), sin(mob.orientation))
                rayon = Ray(mob.r, direction, map)

                if dist > self.range or rayon.distance < dist:
                    return # la liste étant triée, il ne sert plus à rien de tester le reste des mobs
                else:
                    teta_max = atan((mob.size/dist)) # la marge d'erreur pour l'angle de tir du joueur.
                    delta_x = pos.x - mob.r.x
                    delta_y = pos.y - mob.r.y
                    
                    # pour expliquer ça il y a un screen sur le onedrive
                    if delta_x > 0:
                        if delta_y > 0: # cas 1
                            angle_p_m = pi + acos(delta_x/dist)
                        else: # cas 2
                            angle_p_m = pi_2 + acos(abs(delta_y)/dist)
                    else:
                        if delta_y > 0: # cas 3 
                            angle_p_m = tau - acos(abs(delta_x)/dist)
                        else: # cas 4
                            angle_p_m = acos(abs(delta_x)/dist)

                    # angle_p_m (angle player mob) représente la valeur de que player.orientaion devrait avoir pour toucher en plein milieu le mob.
                    teta = orientation - angle_p_m
                    if abs(teta) < teta_max:
                        mob.health = max(mob.health - self.dmg, 0)
                        return # on interromp la boucle, sinon les balles peuvent traverser les mobs.

    def dist(self, pos, mob):
        """
        test if a mob can be shot by a player
        """
        diff = pos - mob.r
        dist = hypot(diff.x, diff.y)

        return dist

    def draw(self, window):
        width, height = self.sprite[self.image_index].get_size()
        top_left = (
            (Config.RES_X / 2) - (width / 2),
            Config.RES_Y - height
        )
        self.update_image()
        window.blit(self.sprite[self.image_index], top_left)

    def update_image(self):
        i = int((pg.time.get_ticks() - self.last_shot_time) / self.time_between_sprites)
        self.image_index = i if i < len(self.sprite) else 0

    def play_sound(self):
        pass
