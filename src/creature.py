from body import *

class Creature(Body):
  def __init__(self) -> None:
    super().__init__()
    self.a = 0
    self.v = 0
    self.orientation = 0.0

  