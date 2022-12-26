import pygame as pg
from pygame import Vector2 as v2
from math import hypot, atan, acos, cos, sin, tau, pi
from render.ray import Ray
from render import *
from config import Config
from random import choice
from bodys import Mob

pi_2 = pi / 2

class Weapon():
    def __init__(self):
        self.dmg = 10
        self.delay = 500 # en ms
        self.range = 100 # 100 -> largeur d'un carré

        self.last_shot_time = - self.delay # moment at which the last shot was fired
                                           # - self.delay to avoid animation at init of the game
        self.play_sound_time = - self.delay
        
        self.time_between_sprites = 200 # ms
        self.sprite = load_weapon() # from render.weapons
        self.image_index = 0

        self.ammo_sound = [pg.mixer.Sound(Config.SOUNDS_FOLDER + "weapons/debug_ammo.mp3")]
        self.no_ammo_sound = [pg.mixer.Sound(Config.SOUNDS_FOLDER + "weapons/debug_no_ammo.mp3")]

    
    def shoot(self, entity):
        """
        check if a mob is touch on click and act in consequence.
        """
        t = pg.time.get_ticks()
        if t - self.last_shot_time > self.delay: # 100 ms between shots 
            if entity.ammo > 0:
                self.last_shot_time = t
                entity.ammo = max(0, entity.ammo - 1)

                mob_list = entity.game.world.mobs + entity.game.world.props
                self.hit_scan(entity.game.world.map.map, entity.r, entity.orientation, mob_list)
                self.play_sound()
            else:
                self.play_sound(no_ammo=True)
    
    def hit_scan(self, map, pos, orientation, mob_list):

        sorted_mob_list = [(self.dist(pos, mob), mob) for mob in mob_list if mob.health > 0]
        sorted_mob_list = sorted(sorted_mob_list, key=lambda x : x[0])

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
                    
                    else: # cas 2
                        angle_p_m = pi_2 + acos(abs(delta_y)/dist)
                
                else:
                    if delta_y > 0: # cas 3 
                        angle_p_m = tau - acos(abs(delta_x)/dist)
                    
                    elif delta_y == 0: # cas limite ou l'angle peut être aussi bien très proche de 0 que de 2pi
                        teta1 = orientation - tau - acos(abs(delta_x)/dist)
                        teta2 = orientation - acos(abs(delta_x)/dist)
                        if abs(teta1) < teta_max or abs(teta2) < teta_max:
                            self.hurt(mob)
                            return
                        else:
                            continue

                    else: # cas 4
                        angle_p_m = acos(abs(delta_x)/dist)

                teta = orientation - angle_p_m
                if abs(teta) < teta_max:
                    self.hurt(mob)
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
        t = pg.time.get_ticks()
        if no_ammo:
            if t - self.play_sound_time > self.delay:
                self.play_sound_time = t
                choice(self.no_ammo_sound).play()
        else:
            choice(self.ammo_sound).play()

    def hurt(self, body):
        if type(body) is Mob:
            body.health = max(body.health - self.dmg, 0)
        else:
            # dans ce cas c'est une prop
            # voir si on peut casser les props
            pass