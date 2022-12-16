from collections import deque
import math

class Path_finding:
    def __init__(self,game) :
        #[-1, 1] [0, 1] [1, 1]
        #[-1, 0] [0, 0] [1, 0]
        #[-1,-1] [0,-1] [1,-1]
        # print(self.graph)
        self.Astar((1,1),(0,41))
        pass

    def heuristic(self,current,goal):
        (x1,y1) = current
        (x2,y2) = goal
        return abs(x1-x2) + abs(y1-y2)

    def heuristic2(self,current,goal):
        (x1,y1) = current
        (x2,y2) = goal
        return math.sqrt ((x1 - x2)^2 + 
            (y1-y2)^2 )

#    def lowestFrankNode(self,nodelist,goal):
#        lowestnode = nodelist[0]        
#        for node in nodelist:
#            currenth = {node : (0,)}  
#            opennode ={current : (0,(self.heuristic2(current,goal))) }
#            visitednode = []
#            print(current)
#            print(opennode)
#            print(lowestFrankNode(opennode))





