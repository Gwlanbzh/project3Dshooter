# Attention pour le draw de Map il faut mieux avec une taille d'ecran egale a 100 * la taille du tableau
# genre pour la map ici c genre largeur = 12*100 et hauteur = 8*100

import pygame as pg
from pygame import Vector2 as v2, Vector3 as v3
from config import Config


# Defnition de la map 
# 0 = False = vide
# 1..n = Wall type
# WAll type, will certainly be wall with different texture like reppresented on the top preview

textures = {'d': "default"}

# the map contains tuples (wall_type: int, texture: str), defined here.
NO_W0 = 0   # no wall
W_DEF = 1  # squared wall
W_TX1 = 2  # triangled wall nb 1
W_TX2 = 3  # triangled wall nb 2

colors = [v3(0, 0, 0),
          v3(255, 0, 0),
          v3(0, 255, 0),
          v3(0, 100, 255),
          ]

print(colors[0])

map = [
    [W_TX1, W_DEF, W_TX1, W_DEF, W_DEF, W_TX2, W_TX2, W_TX2, W_DEF, W_DEF, W_DEF, W_DEF],
    [W_DEF, NO_W0, NO_W0, NO_W0, NO_W0, NO_W0, NO_W0, NO_W0, NO_W0, NO_W0, NO_W0, W_DEF],
    [W_TX2, NO_W0, NO_W0, W_DEF, NO_W0, NO_W0, NO_W0, W_DEF, W_DEF, W_DEF, NO_W0, W_DEF],
    [W_DEF, W_TX2, W_DEF, W_DEF, NO_W0, NO_W0, NO_W0, W_DEF, NO_W0, NO_W0, NO_W0, W_DEF],
    [W_DEF, NO_W0, NO_W0, NO_W0, NO_W0, W_TX1, NO_W0, NO_W0, NO_W0, NO_W0, NO_W0, W_DEF],
    [W_DEF, NO_W0, W_TX1, W_TX1, W_TX1, NO_W0, W_TX1, W_TX1, NO_W0, NO_W0, W_DEF, W_DEF],
    [W_DEF, NO_W0, NO_W0, NO_W0, NO_W0, NO_W0, NO_W0, NO_W0, NO_W0, W_DEF, W_DEF, W_DEF],
    [W_DEF, W_DEF, W_DEF, W_DEF, W_DEF, W_DEF, W_DEF, W_DEF, W_DEF, W_DEF, W_DEF, W_DEF]
]

class Map:
    def __init__(self, game):
        self.game = game
        self.map = map
        self.world = {}
        self.gen_world_map()
  
    def gen_world_map(self):
        '''
        temporary for draw world map, migh be use for collission,render,pathfinding
        Utiliter discutable mais utiliser pour draw la map
        genere le un monde avec en clef les coordoné et en value l'élement a cette position
        '''
        for j,row in enumerate(self.map):
            for i, value in enumerate(row):
                if value != NO_W0:
                    self.world[(i,j)] = value
  
    def draw(self, game):
        """
        temporary, waitting for true render false 3D
        pour rapple _RectValue c'est sous la forme : 
          Rect(left, top, width, height) -> Rect
        """
        for position in self.world:
            if self.world[position][0] == 1: # index 0 extracts the type of wall.
                pg.draw.rect(game.window,"black",
                              (position[0] * 100,position[1] * 100,100,100),2)
            if self.world[position][0] == 2:
                pg.draw.rect(game.window,"blue",
                              (position[0] * 100,position[1] * 100,100,100),2)

            if self.world[position][0] == 3:
                pg.draw.rect(game.window,"orange",
                              (position[0] * 100,position[1] * 100,100,100),2)
  
