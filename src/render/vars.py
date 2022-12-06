from config import *
from math import atan

VIEW_HEIGHT = Config.VIEW_HEIGHT
RES_X = Config.RES_X
RES_Y = Config.RES_Y
FOV_X = Config.FOV_X
FOV_Y = Config.FOV_Y

# function for computing the ray 's direction vector
atanfov = atan(FOV_X/2)
theta = lambda n : atan(atanfov * ( 1-(2*n) / RES_X) )

# function for computing the on-screen height of a wall segment
resfovratio = RES_Y / FOV_Y
scr_h = lambda h, d : resfovratio * (h/d)