import pygame as pg
from pygame import Vector3 as v3


class Map:
    def __init__(self, game, grid):
        self.game = game
        
        # Defnition de la map 
        # 0 = False = vide
        # 1..n = Wall type
        # WAll type, will certainly be wall with different texture like reppresented on the top preview
        self.grid = grid
        
        self.world = {}
        self.gen_world_map()
  
    def gen_world_map(self):
        '''
        temporary for draw world map, migh be use for collission,render,pathfinding
        Utiliter discutable mais utiliser pour draw la map
        genere le un monde avec en clef les coordoné et en value l'élement a cette position
        '''
        for j,row in enumerate(self.grid):
            for i, value in enumerate(row):
                if value != 0:
                    self.world[(i,j)] = value
  
    def draw(self, game):
        """
        temporary, waitting for true render false 3D
        pour rapple _RectValue c'est sous la forme : 
          Rect(left, top, width, height) -> Rect
        """
        for position in self.world:
            if self.world[position] == 1: # index 0 extracts the type of wall.
                pg.draw.rect(game.window,"black",
                              (position[0] * 100,position[1] * 100,100,100),2)
            if self.world[position] == 2:
                pg.draw.rect(game.window,"blue",
                              (position[0] * 100,position[1] * 100,100,100),2)

            if self.world[position] == 3:
                pg.draw.rect(game.window,"orange",
                              (position[0] * 100,position[1] * 100,100,100),2)
  
