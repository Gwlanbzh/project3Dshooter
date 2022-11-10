from creature import *
import pygame as pg  
import math
                     
class Players(Creature):
  def __init__(self):
    super().__init__()
    self.heal_recovery_time = 10000 # valeur arbitraire
    self.weapons = []
    self.ammo = 0 # may change

  def movement(self):
    sin_a = math.sin(self.angle)
    cos_a = math.cos(self.angle)
    dx, dy = 0, 0
    speed = PLAYER_SPEED * self.game.delta_time
    speed_sin = speed * sin_a
    speed_cos = speed * cos_a

    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
      dx += speed_cos
      dy += speed_sin
    if keys[pg.K_s]:
      dx += -speed_cos
      dy += -speed_sin
    if keys[pg.K_a]:
      dx += speed_sin
      dy += -speed_cos
    if keys[pg.K_d]:
      dx += -speed_sin
      dy += speed_cos   

    if keys[pg.K_LEFT]:
        self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
    if keys[pg.K_RIGHT]:
        self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau


    pass