import pygame as pg
from math import hypot, atan, acos, tau, pi
pi_2 = pi / 2

class Weapon():
    def __init__(self):
        self.dmg = 0
        self.delay = 100 # en ms
        self.range = 100 # 100 -> largeur d'un carré

        self.last_shot_time = pg.time.get_ticks() # moment at which the last shot was fired
        # self.sprite = sprite object
        # add sprite
    
    def hit_scan(self, pos, orientation, mob_list):
        """
        check if a mob is touch on click and act in consequence.
        """
        t = pg.time.get_ticks()
        if t - self.last_shot_time > self.delay: # 100 ms between shots 
            self.last_shot_time = t
        
            sorted_mob_list = [(self.dist(pos, mob), mob) for mob in mob_list]
            sorted_mob_list = sorted(sorted_mob_list)

            for dist, mob in sorted_mob_list:
                if dist > self.range:
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
                        print("shoot !")
                        return # on interromp la boucle, sinon les balles peuvent traverser les mobs.

    def dist(self, pos, mob):
        """
        test if a mob can be shot by a player
        """
        diff = pos - mob.r
        dist = hypot(diff.x, diff.y)

        return dist

    def draw(self, game):
        pass

