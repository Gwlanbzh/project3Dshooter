from collections import deque
import math

class Path_finding:
    def __init__(self,game,map) :
        #[-1, 1] [0, 1] [1, 1]
        #[-1, 0] [0, 0] [1, 0]
        #[-1,-1] [0,-1] [1,-1]
        self.map_dic = map.world_map
        self.graph = {}
        self.possible_neighbour = [-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]
        self.create_graph()
        # print(self.graph)
        # self.Astar((1,1),(0,41))


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

    def heuristic(current,goal):
        (x1,y1) = current
        (x2,y2) = goal
        return abs(x1-x2) + abs(y1-y2)

    # def heuristic2(current,goal):
    #     (x1,y1) = current
    #     (x2,y2) = goal
    #     return math.sqrt ((x1 - x2)^2 + 
    #         (y1-y2)^2 )

    #         lowestnode = nodelist[0]        def lowestFrankNode(nodelist):
    #         for node in nodelist:

    #             pass
    #     currenth = heuristic 
    #     opennode ={current : (0,(self.heuristic2(current,goal)) }
    #     visitednode = []
    #     print(current)
    #     print(opennode)
    #     print(lowestFrankNode(opennode))





