import pygame as pg
from math import hypot, atan, acos, asin, tau, pi
pi_2 = pi / 2
pi_3_2 = 3 * pi_2
class Weapon():
    def __init__(self):
        self.dmg = 0
        self.delay = 100 # en ms
        self.range = 100 # 100 -> largeur d'un carré

        self.last_shot_time = pg.time.get_ticks()
        # self.sprite = sprite object
        # add sprite
    
    def hit_scan(self, player, mob_list):
        """
        check if a mob is touch on click
        """
        t = pg.time.get_ticks()
        if t - self.last_shot_time > self.delay: # 100 ms between shots 
            self.last_shot_time = t
        
            sorted_mob_list = [(self.dist(player, mob), mob) for mob in mob_list]
            sorted_mob_list = sorted(sorted_mob_list)

            for dist, mob in sorted_mob_list:
                if dist > self.range:
                    break
                else:
                    teta_max = atan((mob.size/dist))
                    delta_x = player.r[0] - mob.r[0]
                    delta_y = player.r[1] - mob.r[1]
                    if delta_x > 0:
                        if delta_y > 0:
                            angle_p_m = acos(abs(delta_x)/dist) + pi
                        else:
                            angle_p_m = acos(abs(delta_y)/dist) + pi_2
                    else:
                        if delta_y > 0:
                            angle_p_m = acos(abs(delta_x)/dist) + pi_3_2
                        else:
                            angle_p_m = acos(abs(delta_x)/dist)

                    
                    teta = player.orientation - angle_p_m
                    print(teta)
                    if abs(teta) < teta_max:
                        print("shoot !")
                        # TODO : remove life to a mob

    def dist(self, player, mob):
        """
        test if a mob can be shot by a player
        """
        x_p, y_p = player.r
        x_m, y_m = mob.r
        dist = hypot(x_p - x_m, y_p - y_m)

        return dist



