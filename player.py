from creature import *

class Players(Creature):
  def __init__(self):
    super().__init__()
    self.weapons = []
    self.ammo = 0 # may change

  def fet_inputs():
    pass