from collections import deque

class Path_finding:
    def __init__(self,game,map) :
        self.map = map.world_map
        self.graph = {}
        self.possible_neighbour = [-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]
        self.create_graph()
        

    def create_graph(self):
        for y, row in enumerate(self.map):
            for x, value in enumerate(row):
                if not value[1]:
                    self.graph[(x,y)] = self.get_neighbour(x,y)
    
    def get_neighbour(self,x_map,y_map):
        """
        return : a list of valid neighbour 
        valid neigbour are 
        """
        return [(x_map+x_relative,y_map+y_relative) 
                for x_relative,y_relative in self.ways 
                    if (x_map+x_relative,y_map+y_relative) not in self.map]

    def heuristic(current,goal):
        (x1,y1) = current
        (x2,y2) = goal
        return abs(x2-x2) + abs(y1-y2)

    def breadth_first_search(self,start, goal, h):
        queue = deque([start])
        visited = {start: None}

        while queue:
            cur_node = queue.popleft()
            if cur_node == goal:
                break
            next_nodes = self.graph[cur_node]

            for next_node in next_nodes:
                if next_node not in visited and next_node not in self.game.object_handler.npc_positions:
                    queue.append(next_node)
                    visited[next_node] = cur_node
        return visited

