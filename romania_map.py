from SimpleProblemSolvingAgent import UndirectedGraph, Graph
##############################################################################
# This file contains the graph of Romania and the locations of each city. 
# The graph is used to calculate the distances between cities in Romania.
##############################################################################
 
 # Provided graph of Romania - not being used in my implementation
'''
# romania_map is a graph of the cities in Romania, with the cost of travel between each pair of cities.
romania_map = UndirectedGraph(dict(
    Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
    Bucharest=dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
    Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
    Drobeta=dict(Mehadia=75),
    Eforie=dict(Hirsova=86),
    Fagaras=dict(Sibiu=99),
    Hirsova=dict(Urziceni=98),
    Iasi=dict(Vaslui=92, Neamt=87),
    Lugoj=dict(Timisoara=111, Mehadia=70),
    Oradea=dict(Zerind=71, Sibiu=151),
    Pitesti=dict(Rimnicu=97),
    Rimnicu=dict(Sibiu=80),
    Urziceni=dict(Vaslui=142)))
'''

# Calculated distances between cities in Romania using the haversine formula
romania_map = UndirectedGraph(dict(
    Arad=dict(Zerind=51, Sibiu=223, Timisoara=49),
    Bucharest=dict(Urziceni=54, Pitesti=109, Giurgiu=59, Fagaras=181),
    Craiova=dict(Drobeta=96, Rimnicu=97, Pitesti=103),
    Drobeta=dict(Mehadia=38),
    Eforie=dict(Hirsova=89),
    Fagaras=dict(Sibiu=64),
    Hirsova=dict(Urziceni=103),
    Iasi=dict(Vaslui=58, Neamt=95),
    Lugoj=dict(Timisoara=54, Mehadia=95),
    Oradea=dict(Zerind=56, Sibiu=220),
    Pitesti=dict(Rimnicu=48),
    Rimnicu=dict(Sibiu=80),
    Urziceni=dict(Vaslui=230)))

# The locations (latitude/longitude) of each city in the map
romania_map.locations = dict(
    Arad=(46.1866, 21.3123), Bucharest=(44.4268, 26.1025), Craiova=(44.3302, 23.7949),
    Drobeta=(44.6369, 22.6597), Eforie=(44.0613, 28.6310), Fagaras=(45.8416, 24.9731),
    Giurgiu=(43.9037, 25.9699), Hirsova=(44.6893, 27.9457), Iasi=(47.1585, 27.6014),
    Lugoj=(45.6910, 21.9035), Mehadia=(44.9052, 22.3673), Neamt=(46.9759, 26.3819),
    Oradea=(47.0465, 21.9189), Pitesti=(44.8565, 24.8692), Rimnicu=(45.0997, 24.3693),
    Sibiu=(45.8035, 24.1450), Timisoara=(45.7489, 21.2087), Urziceni=(44.7181, 26.6453),
    Vaslui=(46.6407, 27.7276), Zerind=(46.6225, 21.5174))