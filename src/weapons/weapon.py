import pygame as pg
from pygame import Vector2 as v2
from math import hypot, atan, acos, cos, sin, tau, pi
from render.ray import Ray
from render import *
from config import Config
from random import choice
pi_2 = pi / 2

class Weapon():
    def __init__(self):
        self.dmg = 10
        self.delay = 500 # en ms
        self.range = 100 # 100 -> largeur d'un carré

        self.last_shot_time = - self.delay # moment at which the last shot was fired
                                           # - self.delay to avoid animation at init of the game
        
        self.time_between_sprites = 200
        self.sprite = load_weapon() # from render.weapons
        self.image_index = 0

        # TODO : deux sons à initialiser :
        #    - une liste de sons pour quand l'arme est chargée
        #    - un son pour l'arme quand on a plus de munitions

        self.ammo_sound = [pg.mixer.Sound(Config.SOUNDS_FOLDER + "weapons/debug_ammo.mp3")]
        self.no_ammo_sound = [pg.mixer.Sound(Config.SOUNDS_FOLDER + "weapons/debug_no_ammo.mp3")]
    
    def shoot(self, entity):
        """
        check if a mob is touch on click and act in consequence.
        """
        t = pg.time.get_ticks()
        if t - self.last_shot_time > self.delay: # 100 ms between shots 
            self.last_shot_time = t
            if entity.ammo > 0:
                entity.ammo = max(0, entity.ammo - 1)

                mob_list = entity.game.world.mobs
                self.hit_scan(entity.game.world.map.map, entity.r, entity.orientation, mob_list)
                self.play_sound()            
            else:
                self.play_sound(no_ammo=True)
    
    def hit_scan(self, map, pos, orientation, mob_list):

        sorted_mob_list = [(self.dist(pos, mob), mob) for mob in mob_list if mob.health > 0]
        sorted_mob_list = sorted(sorted_mob_list)

        for dist, mob in sorted_mob_list:
            # test mur
            direction = v2(cos(orientation), sin(orientation))
            rayon = Ray(pos, direction, map)

            if dist > self.range or rayon.distance < dist:
                return # la liste étant triée, il ne sert plus à rien de tester le reste des mobs
            else:
                teta_max = atan(mob.size/dist) # la marge d'erreur pour l'angle de tir du joueur.
                delta_x = pos.x - mob.r.x
                delta_y = pos.y - mob.r.y
                
                # pour expliquer ça il y a un screen sur le onedrive
                if delta_x > 0:
                    if delta_y > 0: # cas 1
                        angle_p_m = pi + acos(delta_x/dist)

                    elif delta_y == 0:
                        teta1 = orientation -  pi + acos(delta_x/dist)
                        teta2 = orientation -  pi_2 + acos(abs(delta_y)/dist)
                        if abs(teta1) < teta_max or abs(teta2) < teta_max:
                            mob.health = max(mob.health - self.dmg, 0)
                            return
                        else:
                            continue
                    else: # cas 2
                        angle_p_m = pi_2 + acos(abs(delta_y)/dist)
                
                else:
                    if delta_y > 0: # cas 3 
                        angle_p_m = tau - acos(abs(delta_x)/dist)
                    
                    elif delta_y == 0:
                        teta1 = orientation - tau - acos(abs(delta_x)/dist)
                        teta2 = orientation - acos(abs(delta_x)/dist)
                        if abs(teta1) < teta_max or abs(teta2) < teta_max:
                            mob.health = max(mob.health - self.dmg, 0)
                            return
                        else:
                            continue

                    else: # cas 4
                        angle_p_m = acos(abs(delta_x)/dist)

                teta = orientation - angle_p_m
                if abs(teta) < teta_max:
                    mob.health = max(mob.health - self.dmg, 0)
                    return # on interromp la boucle, sinon les balles peuvent traverser les mobs.

    def dist(self, pos, mob):
        """
        test if a mob can be shot by a player
        """
        x, y = pos - mob.r
        dist = hypot(x, y)

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

    def play_sound(self, no_ammo=False):
        if no_ammo:
            choice(self.no_ammo_sound).play()
        else:
            choice(self.ammo_sound).play()
