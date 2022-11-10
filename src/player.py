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
    pass