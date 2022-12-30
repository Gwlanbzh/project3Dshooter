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
                    [1, 0, 0, 0, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
                    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
                    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
                    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
                    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1, ],
                    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 5, 1, ],
                    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
                    [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ]
        ]

        self.map_height = len(self.map)
        self.map_width = len(self.map[0])
        self.map_dic = {}
        self.gen_world_map_dic()
        self.graph = {}
        self.create_graph()

  
    def gen_world_map_dic(self):
        '''
        temporary for draw world map, migh be use for collission,render,pathfinding
        Utiliter discutable mais utiliser pour draw la map
        genere le un monde avec en clef les coordoné et en value l'élement a cette position
        '''
        for j,row in enumerate(self.map):
            for i, value in enumerate(row):
                if value != 0:
                    self.map_dic[(i,j)] = value

    def create_graph(self):
        for y, row in enumerate(self.map):
            for x, value in enumerate(row):
                if value == 0:
                    self.graph[(x,y)] = Node((x,y))

        for y, row in enumerate(self.map):
            for x, value in enumerate(row):
                if value == 0:
                    self.graph[(x,y)] = Node((x,y),self.get_neighbour(x,y))

    def get_neighbour(self,x_map,y_map,allow_diagonal_movment = False):
        """
        return : a list of valid neighbour
        valid neigbour are
        """
        if allow_diagonal_movment:
            possible_neighbour = [-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]
        else:
            possible_neighbour = [-1,0],[0,-1],[0,1],[1,0]
        return [(x_map+x_relative,y_map+y_relative)
                for x_relative,y_relative in possible_neighbour
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

        for position in self.graph:
            pg.draw.rect(game.window,"red",(position[0]*100,position[1]*100,10,10))

class Node:
    def __init__(self,position,neighbour = None):
        self.position = position
        self.neighbour = neighbour
        self.parent = None
        self.cost = 0
        self.heuristic = 0
        self.total_cost = 0

    def __eq__(self, other):
        return self.position == other.position
    
    def __repr__(self):
      return f"{self.position} - g: {self.cost} h: {self.heuristic}"

    # defining less than for purposes of heap queue
    def __lt__(self, other):
      return self.total_cost < other.total_cost
    
    # defining greater than for purposes of heap queue
    def __gt__(self, other):
      return self.total_cost > other.total_cost

        