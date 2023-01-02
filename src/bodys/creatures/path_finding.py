from collections import deque
from map import Node
import math
import heapq

class PathFinding:
    def __init__(self,game) :
        self.map_height = game.world.map.map_height
        self.map_width = game.world.map.map_width
        self.graph = game.world.map.graph
        pass

    def get_path(self,current_node):
        """
        unfold the path compute by Astar
        """
        path = []
        current = current_node
        while current is not None:
            if len(path) > 20:
                break
            path.append(current.position)
            current = current.parent

        if len(path)<2:
            return path[-1]  # Return reversed path
        return path[-2]  # Return reversed path


    def Astar(self,start_map_pos,goal_map_pos):
        """
        Implementation of the A* algorithm 
        start_pos: must be a tuple of int
        goal_pos: must be a tuple of int

        return the next map_position to go
        """
        start_node = self.graph[(start_map_pos)]

        # Set of node to be evaluted
        open_list = []
        close_list = []

        # Heapify the open_list and Add the start node
        heapq.heapify(open_list) 
        heapq.heappush(open_list, start_node)

        # Adding a stop condition
        iterations = 0
        max_iterations = 1000

        # Loop until the queue is empty
        while len(open_list) > 0:
            iterations += 1

            if iterations > max_iterations:
                # the goal will not be contain
                return self.get_path(current_node)
    
            # Get the current node
            current_node = heapq.heappop(open_list)
            close_list.append(current_node)

            # Goal is Found
            if current_node.position == goal_map_pos:
                return self.get_path(current_node)
            # Generate children
            children = []
        
            for child_pos in current_node.neighbour:

                if child_pos != current_node.position: 
                    # Update node parent
                    new_node = Node(child_pos,self.graph[child_pos].neighbour)
                    new_node.parent = current_node

                # Append
                children.append(new_node)

            # Loop through children
            for child in children:
                # Child is on the closed list
                if len([closed_child for closed_child in close_list if closed_child == child]) > 0:
                    continue
                # Create the f, g, and h values
                child.cost = current_node.cost + 1
                child.heuristic = self.heuristic(child.position,goal_map_pos)
                child.total_cost = child.cost + child.heuristic

                # Child is already in the open list
                if len([open_node for open_node in open_list if child.position == open_node.position and child.cost > open_node.cost ]) > 0:
                    continue

                # Add the child to the open list
                heapq.heappush(open_list, child)
        return None

    def heuristic(self,current,goal):
        (x1,y1) = current
        (x2,y2) = goal
        return abs(x1-x2) + abs(y1-y2)

    def heuristic2(self,current,goal):
        (x1,y1) = current
        (x2,y2) = goal
        return math.sqrt ((x1 - x2)^2 + 
            (y1-y2)^2 )

    def heuristic3(self,current,goal):
        return ((current[0] - goal[0]) ** 2) + ((current[1] - goal[1]) ** 2)