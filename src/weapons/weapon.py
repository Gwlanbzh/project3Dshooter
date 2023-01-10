import pygame as pg
from pygame import Vector2 as v2
from math import hypot, atan, cos, sin, tau, pi
from render.ray import Ray
from render import *
from config import Config


pi_2 = pi / 2

class Weapon():
    def __init__(self):
        self.dmg = 10
        self.delay = 500  # en ms
        self.range = 100  # 100 -> largeur d'un carré

        self.last_shot_time = - self.delay  # moment at which the last shot was fired
                                            # - self.delay to avoid animation at init of the game
        self.play_sound_time = - self.delay
        
        self.time_between_sprites = 200  # ms
        self.image_index = 0

        self.model = "weapon" # reference for sound and display

    def shoot(self, entity, mob_list):
        """
        make the weapon shot if it is possible with the weapon delay, if it is, make the scan of the world to know if a monster
        is touched.

        entity : Creature, the entity who is firing
        mob_list : Body list, List of bodies that must be taken into account by the scan
        """
        t = pg.time.get_ticks()
        # if weapon respect the delay
        if t - self.last_shot_time > self.delay:  # 100 ms between shots 
            # if the entity firing has ammunition
            if entity.ammo > 0:
                self.last_shot_time = t                                                           # update the last shot date
                entity.ammo = max(0, entity.ammo - 1)                                             # ammution is removed
                self.hit_scan(entity.game.world.map.grid, entity.r, entity.orientation, mob_list) # scan of the world
                self.play_sound(entity)                                                           # playing sound of the weapon
            else:
                self.play_sound(entity, no_ammo=True) # playing dry fire sound
    
    def hit_scan(self, map, pos, orientation, mob_list):
        """
        Scan the world to know if a shot from a position has touched one of the body in mob_list
        
        map : Map, map of the current world
        pos : Vector2 (pygame), original position of the shot
        orientation : 0 <= float < 2pi, orientation of the shot
        mob_list : Body list, list of the body that can be shooted
        """

        # création d'une liste de Body triée en fonction de leur distance avec le joueur. On supprime les body avec 0 de vie.
        sorted_mob_list = [(self.dist(pos, mob), mob) for mob in mob_list if mob.health > 0]
        sorted_mob_list = sorted(sorted_mob_list, key=lambda x : x[0])

        # création d'un rayon : sert à calculer la distance entre le joueur et le premier mur sur la trajectoire du tir
        direction = v2(cos(orientation), sin(orientation))
        rayon = Ray(pos, direction, map)

        for dist, mob in sorted_mob_list:
            # si le joueur tire dans un mur avant d'atteindre le mob
            if dist > self.range or rayon.distance < dist:
                return  # la liste étant triée, il ne sert plus à rien de tester le reste des mobs
            else:
                teta_max = atan(mob.size/dist)  # la marge d'erreur pour l'angle de tir du joueur.
                
                # calcule de l'angle entre l'entité qui tire l'entité visée
                x, y = mob.r - pos
                if y == 0 and x < 0:
                    angle_p_m = pi
                else:
                    angle_p_m = 2 * atan(y/(x + dist)) % tau

                teta = orientation - angle_p_m # angle de tir. si teta = 0 alors le joueur touche en plein dans le mille
                # si teta proche de pi, alors le joueur tire dans la direction opposée du mob
                
                # cas limite -> l'angle est très proche de 2pi, il faut tester pour un angle qui tend vers 2pi et pour un angle qui tend vers 0
                if y == 0:
                    if abs(teta) < teta_max:
                        mob.hurt(self.dmg)
                        return
                    
                    teta = tau - teta
                    if abs(teta) < teta_max:
                        mob.hurt(self.dmg)
                        return

                # si teta est plus petit que la marge d'erreur, l'entité atteint sa cible
                if abs(teta) < teta_max:
                    mob.hurt(self.dmg)
                    return  # on interromp la boucle, sinon les balles peuvent traverser les mobs.

    def dist(self, pos, mob):
        """
        Calculet the distance between a position and a Body
        """
        x, y = pos - mob.r
        dist = hypot(x, y)

        return dist

    def draw(self, ressources, window):
        """
        Display the first person view of the weapon
        """
        self.update_image(ressources)
        
        sprites = ressources.weapon_sprites[self.model]

        width, height = sprites[self.image_index].get_size()
        top_left = (
            (Config.RES_X / 2) - (width / 2),
            Config.RES_Y - height
        )
        window.blit(sprites[self.image_index], top_left)

    def draw2d(self, window, r, teta):
        """
        Draw the weapon in the 2D mode
        """
        traylength = self.range
        pg.draw.line(
            window,'yellow', (r),
            (r[0]+ traylength * cos(teta), r[1] + traylength * sin(teta)),
            2
        )

    def update_image(self, Ressources):
        """
        Update the image of the weapon
        """
        i = int((pg.time.get_ticks() - self.last_shot_time) / self.time_between_sprites)
        self.image_index = i if i < len(Ressources.weapon_sprites[self.model]) else 0

    def play_sound(self, entity, no_ammo=False):
        # play the sound of the weapon

        sound = entity.game.sound
        pos_sound = entity.r
        pos_player = entity.game.world.players[0].r
        is_p = (entity.model == "player")

        t = pg.time.get_ticks()
        if no_ammo:
            if t - self.play_sound_time > self.delay:
                self.play_sound_time = t
                sound.play_sound("dryfire", pos_player, pos_sound, is_player=is_p)
        else:
            sound.play_sound(self.model, pos_player, pos_sound, is_player=is_p)
