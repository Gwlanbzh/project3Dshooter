# Attention pour le draw de Map il faut mieux avec une taille d'ecran egale a 50 * la taille du tableau
# genre pour la map ici c genre largeur = 12*50 et hauteur = 8*50

import pygame as pg
from config import Config

e = False
map = [
    [1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,0,0,0,0,1,1,1,0,1],
    [1,0,1,0,0,0,0,1,0,0,0,1],
    [1,0,0,0,0,2,0,0,0,0,0,1],
    [1,0,2,2,2,0,2,2,0,0,1,1],
    [1,0,0,0,0,0,0,0,0,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1]
]

class Map:
    def __init__(self,game):
        self.game = game
        self.map = map
        self.world = {}
        self.gen_world_map()
  
    def gen_world_map(self):
        '''
        Utiliter discutable mais utiliser pour draw la map
        genere le un monde avec en clef les coordoné et en value l'élement a cette position
        '''
        for j,row in enumerate(self.map):
            for i, value in enumerate(row):
                if value :
                    self.world[(i,j)] = value
  
    def draw(self,game):
        """
        pour rapple _RectValue c'est sous la forme : 
          Rect(left, top, width, height) -> Rect
        """
        for position in self.world:
            if self.world[position] == 1:
                pg.draw.rect(game.window,"black",
                              (position[0] * 100,position[1] * 100,100,100),2)
            if self.world[position] == 2:
                pg.draw.rect(game.window,"blue",
                              (position[0] * 100,position[1] * 100,100,100),2)
  