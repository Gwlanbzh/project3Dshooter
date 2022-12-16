import pygame as pg
from pygame import Vector3 as v3
from config import Config
from config import WALL_WIDTH

class Map:
    def __init__(self, game):
        self.game = game
        
        # Defnition de la map 
        # 0 = False = vide
        # 1..n = Wall type
        # WAll type, will certainly be wall with different texture like reppresented on the top preview
        self.map = [[1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
                    [1, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
                    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
                    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
                    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1, ],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 5, 1, ],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ]
        ]
        
        self.world_map = {}
        self.gen_world_map()

        self.map_dic = {}
        self.possible_neighbour = [-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]
        self.create_graph()
  
    def gen_world_map(self):
        '''
        temporary for draw world map, migh be use for collission,render,pathfinding
        Utiliter discutable mais utiliser pour draw la map
        genere le un monde avec en clef les coordoné et en value l'élement a cette position
        '''
        for j,row in enumerate(self.map):
            for i, value in enumerate(row):
                if value != 0:
                    self.world_map[(i,j)] = value

    def create_graph(self):
        for y, row in enumerate(self.map_dic):
            for x, value in enumerate(row):
                if not value:
                    self.graph[(x,y)] = self.get_neighbour(x,y)

    def get_neighbour(self,x_map,y_map):
        """
        return : a list of valid neighbour
        valid neigbour are
        """
        return [(x_map+x_relative,y_map+y_relative)
                for x_relative,y_relative in self.possible_neighbour
                    if ((x_map,y_map) not in self.map_dic and ((x_map+x_relative,y_map+y_relative) not in self.map_dic))]
  
    def draw(self, game):
        """
        temporary, waitting for true render false 3D
        pour rapple _RectValue c'est sous la forme : 
          Rect(left, top, width, height) -> Rect
        """
        for position in self.map_dic:
            if self.map_dic[position] == 1: # index 0 extracts the type of wall.
                pg.draw.rect(game.window,"black",
                              (position[0] * 100,position[1] * 100,100,100),2)
            if self.map_dic[position] == 2:
                pg.draw.rect(game.window,"blue",
                              (position[0] * WALL_WIDTH, position[1] * 100,100,100),2)

            if self.map_dic[position] == 3:
                pg.draw.rect(game.window,"orange",
                              (position[0] * WALL_WIDTH, position[1] * 100, 100, 100),2)
  
