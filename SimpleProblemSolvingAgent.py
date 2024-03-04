
import random
import math
from math import radians, sin, cos, sqrt, atan
import heapq

############################################################################################################
# This file contains the SimpleProblemSolvingAgent class which is a simple 
# problem solving agent that contains methods to perform different search strategies.
 
# SimpleProblemSolvingAgent contains methods to perform Greedy Best-First Search, A* Search, 
# Hill Climbing Search, and Simulated Annealing Search.

# The file also contains helper functions to create an undirected graph, a graph class 
# to represent the map of Romania, a priority queue, and the haversine formula to 
# calculate the distance between two points on the Earth from their latitude and longitude.
############################################################################################################


############################################################################################################
# Helper functions for the SimpleProblemSolvingAgent class
############################################################################################################


############################################################################################################
# Graph class
# Represents the map of Romania
############################################################################################################

class Graph:
    # constructor
    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict
        self.directed = directed
        if not directed:
            self.make_undirected()

    # method to make the graph undirected
    def make_undirected(self):
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.connect1(b, a, dist)

    # method to connect two nodes
    def connect(self, A, B, distance=1):
        self.connect1(A, B, distance)
        if not self.directed:
            self.connect1(B, A, distance)

    # method to connect two nodes
    def connect1(self, A, B, distance):
        self.graph_dict.setdefault(A, {})[B] = distance

    # method to get the links of a node
    def get(self, a, b=None):
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)

    # method to get the nodes of the graph
    def nodes(self):
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)

    # method to get the cost of a node
    def cost(self, current, next):
        return self.graph_dict[current][next]

    # method to get the heuristic of a node
    def heuristic(self, goal, node):
        locs = getattr(self, 'locations', None)
        if locs:
            return int(haversine(locs[goal], locs[node]))
        else:
            return 0

    # method to get the neighbors of a node
    def neighbors(self, node):
        return self.graph_dict[node].keys()

############################################################################################################
# End of Graph class
############################################################################################################


############################################################################################################
# Create an Undirected graph
############################################################################################################

def UndirectedGraph(graph_dict=None):
    return Graph(graph_dict=graph_dict, directed=False)

############################################################################################################
# End of Undirected graph
############################################################################################################


############################################################################################################
# Haversine formula
# Calculatea the distance between two points on the Earth from their latitude and longitude
############################################################################################################

def haversine(coord1, coord2):
    R = 6371
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    phi1, phi2 = radians(lat1), radians(lat2)
    dphi = radians(lat2 - lat1)
    dlambda = radians(lon2 - lon1)
    a = sin(dphi / 2) ** 2 + cos(phi1) * cos(phi2) * sin(dlambda / 2) ** 2
    return 2 * R * atan(sqrt(a))

############################################################################################################
# End of haversine formula
############################################################################################################


############################################################################################################
# Priority Queue
# class to represent a priority queue
############################################################################################################

class PriorityQueue:
    # constructor
    def __init__(self):
        self.elements = []

    # method to check if the queue is empty
    def empty(self):
        return len(self.elements) == 0

    # method to put an item in the queue
    def put(self, item, priority):
        self.elements.append((item, priority))
        self.elements.sort(key=lambda x: x[1])

    # method to get an item from the queue
    def get(self):
        return self.elements.pop(0)[0]

############################################################################################################
# End of Priority Queue
############################################################################################################


############################################################################################################
# SimpleProblemSolvingAgent class
############################################################################################################

class SimpleProblemSolvingAgent:

    # constructor takes in a graph, start city, and goal city and initializes the heuristics dictionary (distances from each city to the goal city)
    def __init__(self, graph, start_city, goal_city):
        self.start_city = start_city
        self.goal_city = goal_city
        self.graph = graph
        self.heuristics = {}
        # calculate all heuristics for all cities and goal city
        for city in self.graph.nodes():
            self.heuristics[city] = self.graph.heuristic(self.goal_city, city)

    # method to call a specific search based on strategy type
    def search(self, strategy):
        if strategy == 'greedy_best_first':
            return self.greedy_best_first_search()
        elif strategy == 'a_star':
            return self.a_star_search()
        elif strategy == 'hill_climbing':
            return self.hill_climbing_search()
        elif strategy == 'simulated_annealing':
            return self.simulated_annealing_search()
        else:
            return "Invalid strategy"

    ############################################################################################################
    # Greedy Best-First Search - 
    # selects path that appears best at each step using heuristic function to estimate 
    # how close the end of the path is to the goal.
    ############################################################################################################
    
    def greedy_best_first_search(self):
        # create a priority queue
        frontier = [(self.heuristics[self.start_city], self.start_city)]
        heapq.heapify(frontier)
        cost = 0
        came_from = {self.start_city: None}

        # while the queue is not empty
        while frontier:
            # get the current node from the queue
            current = heapq.heappop(frontier)[1]
            closest = None

            # if the current node is the goal node, break
            if current == self.goal_city:
                break
            
            # for each neighbor of the current node
            for next in self.graph.neighbors(current):
                # if the neighbor is not in the came_from dictionary
                if next not in came_from:
                    # if the closest node is None or the heuristic of the neighbor is less than the heuristic of the closest node, update the closest node
                    if closest is None or self.heuristics[next] < self.heuristics[closest]:
                        closest = next
                        
            # if the closest node is not None, add the closest node to the queue and the came_from dictionary
            if closest:
                heapq.heappush(frontier, (self.heuristics[closest], closest))
                came_from[closest] = current, self.graph.cost(current, closest)
                    
        # reconstruct the path from the came_from dictionary
        path = self.reconstruct_path(came_from)
        
        # calculate the cost of the path
        cost = self.calculate_cost(path)

        return path, cost
    
    ############################################################################################################
    # End of Greedy Best-First Search
    ############################################################################################################
    
    
    
    ############################################################################################################
    # A* search
    # uses both the cost to reach the node and the cost to get from the node 
    # to the goal to determine the priority of the node in the queue.
    ############################################################################################################
    
    def a_star_search(self):
        # create a priority queue
        frontier = PriorityQueue()
        frontier.put(self.start_city, 0)
        came_from = {self.start_city: None}
        cost_so_far = {self.start_city: 0}
        path = []
        cost = 0

        # while the queue is not empty
        while not frontier.empty():
            current = frontier.get()
            
            # if the current node is the goal node, break
            if current == self.goal_city:
                break

            # for each neighbor of the current node
            for next in self.graph.neighbors(current):
                # calculate the new cost
                new_cost = cost_so_far[current] + self.graph.cost(current, next)
                # if the neighbor is not in the cost_so_far dictionary or the new cost is less than the cost in the cost_so_far dictionary
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    # update the cost_so_far dictionary
                    cost_so_far[next] = new_cost
                    # calculate the priority of the neighbor
                    priority = new_cost + self.heuristics[next]
                    # add the neighbor to the queue
                    frontier.put(next, priority)
                    # add the neighbor to the came_from dictionary
                    came_from[next] = current, self.graph.cost(current, next)

        # reconstruct the path from the came_from dictionary
        path = self.reconstruct_path(came_from)

        # calculate the cost of the path
        cost = self.calculate_cost(path)
        
        return path, cost
    
    ############################################################################################################
    # End of A* search
    ############################################################################################################
    
    
    ############################################################################################################
    # Hill Climbing Search 
    # move to the neighbor that offers lowest cost compared to the current node. 
    # To overcome bad paths, I implemented a tried list to keep track 
    # of nodes that have already been tried and prevent the agent from going back to them.
    # Will not pursue paths where neighbor only has one neighbor (dead ends)
    ############################################################################################################
    
    def hill_climbing_search(self):
        # set the current node to the start node
        current = self.start_city
        path = [current]
        cost = 0
        tried = []

        # while the current node is not the goal node
        while current != self.goal_city:

            # get the neighbors of the current node
            neighbors = list(self.graph.neighbors(current))
            next = None
            next_cost = 0
            best_cost = float('inf')
            best_neighbor = None

            # if this triggers, it means we are back at the start node
            if current == self.start_city:
                for city in tried:
                    if city in neighbors:
                        # removes the paths through neighbors that have already been tried and resets the cost and path since we are back at the start node
                        neighbors.remove(city)
                        cost = 0
                        path = [self.start_city]

            # for each neighbor of the current node
            for neighbor in neighbors:
                # if the neighbor is the goal node, set the best neighbor and best cost to the goal city and break out
                if neighbor == self.goal_city:
                    best_neighbor = neighbor
                    best_cost = self.graph.cost(current, neighbor)
                    break

                # if the neighbor has already been tried or is in the path, continue
                if neighbor in tried:
                    continue
                if neighbor in path:
                    continue

                # if neighbor has only one neighbor continue
                if len(list(self.graph.neighbors(neighbor))) == 1:
                    continue
                
                # calculate the cost of the neighbor
                next_cost = self.graph.cost(current, neighbor)
                
                # if the cost of the neighbor is less than the best cost, update the best cost and best neighbor
                if next_cost < best_cost:
                    best_cost = next_cost
                    best_neighbor = neighbor
            
            # if the best neighbor exists, add the best neighbor to tried nodes
            # if there is no best neighbor, add the current node to tried nodes and set the current node to the second to last node in the path
            if best_neighbor:
                tried.append(best_neighbor)
            else:
                tried.append(current)
                current = path[-2]
                path.pop()
                continue
            
            # if the best neighbor exists, set the current node to the best neighbor and add the best neighbor to the path
            # if there is no best neighbor, break
            if best_neighbor:
                current = best_neighbor
                path.append(current)
                cost += best_cost
            else:
                break     
        return path, cost

    ############################################################################################################
    # End of Hill Climbing Search
    ############################################################################################################
    
    
    ############################################################################################################
    # Simulated Annealing Search 
    # uses probability function to determine whether to move to a neighbor or not. 
    # Default number of iterations is 10. The higher the number of iterations, the higher the precision.
    ############################################################################################################
    
    def simulated_annealing_search(self):
        # higher number of iterations increases precision
        number_of_iterations = 10

        # Higher T increases probability of accepting worse solutions
        T = 100

        # Lower T_min increases precision
        T_min = 0.00001

        # Rate of decrease of temperature
        alpha = 0.9

        # function to perform simulated annealing ONE TIME
        def simulated_annealing(T, T_min, alpha):
            current = self.start_city
            path = [current]
            cost = 0

            # while the temperature is greater than the minimum temperature
            while T > T_min:
                neighbors = list(self.graph.neighbors(current))
                next = random.choice(neighbors)
                if next in path and len(neighbors) > 1:
                    neighbors.remove(next)
                    next = random.choice(neighbors)
                
                if next in path and len(neighbors) == 1:
                    break

                next_cost = self.graph.cost(current, next)
                delta = next_cost - cost
                if delta < 0 or math.exp(-delta/T) > random.random():
                    path.append(next)
                    cost += next_cost
                    current = next
                if current == self.goal_city:
                    break
                else:
                    T *= alpha
                
            if current != self.goal_city:
                return path, float('inf')
            else:
                return path, cost

        # perform simulated annealing multiple times and return the best path and cost
        for i in range(number_of_iterations):
            path, cost = simulated_annealing(T, T_min, alpha)
            if i == 0:
                best_path = path
                best_cost = cost
            else:
                if cost < best_cost:
                    best_path = path
                    best_cost = cost

        return best_path, best_cost  

    ############################################################################################################
    # End of Simulated Annealing Search
    ############################################################################################################
    

    ############################################################################################################
    # Reconstructs path from came_from dictionary
    ############################################################################################################     
    
    def reconstruct_path(self, came_from):
        current = self.goal_city
        total_path = [current]

        while current != self.start_city:
            current, cost = came_from[current]
            total_path.append(current)

        return total_path[::-1]

    ############################################################################################################
    # End of reconstruct_path
    ############################################################################################################
    
    
    ############################################################################################################
    # takes path and calculates total cost
    ############################################################################################################
    
    def calculate_cost(self, path):
        cost = 0
        for i in range(len(path) - 1):
            cost += self.graph.cost(path[i], path[i + 1])
        return cost
    
    ############################################################################################################
    # End of calculate_cost  
    ############################################################################################################


############################################################################################################
# End of SimpleProblemSolvingAgent class
############################################################################################################

                   

    










