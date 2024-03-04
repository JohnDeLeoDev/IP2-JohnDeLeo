# Romania Map Path Finder
# An agent built with python that will attempt to find the shortest path along roads between two Romanian cities.

### Necessary Files
- `README.md` - This file
- `romania_map.py` - The map of Romania as a graph and latitude/longitude coordinates
- `RomaniaCityApp.py` - The main application file
- `SimpleProblemSolvingAgent.py` - Contains the SimpleProblemSolvingAgent class

### Extra Files
- `RomaniaMap.png` - A visual representation of the Romania map
- `CalculatedDistances.txt` - A text file containing the calculated distances between cities
- `CalcAllDistances.py` - A script to calculate the distances between cities and write them to `CalculatedDistances.txt`

### Running the Application
- Run `RomaniaCityApp.py` to start the application
    Example in terminal: `python3 RomaniaCityApp.py`

- The application will prompt you to enter a start city and a goal city
    - The start city and goal city must be one of the following:
        - Arad
        - Bucharest
        - Craiova
        - Dobreta
        - Eforie
        - Fagaras
        - Giurgiu
        - Hirsova
        - Iasi
        - Lugoj
        - Mehadia
        - Neamt
        - Oradea
        - Pitesti
        - Rimnicu Vilcea
        - Sibiu
        - Timisoara
        - Urziceni
        - Vaslui
        - Zerind

- The application will then display the path and cost of that path (total distance) from the start city to the goal city using four different methods of search:
    - Greedy Best First Search
    - A* Search
    - Hill Climbing Search
    - Simulated Annealing Search

### Sample Output
```
     Enter a starting city: Arad

     Enter a destination city: Bucharest

     Greedy Best First Search:
          Path:  Arad → Sibiu → Rimnicu → Pitesti → Bucharest
          Cost:  460

     A* Search:
          Path:  Arad → Sibiu → Rimnicu → Pitesti → Bucharest
          Cost:  460

     Hill Climbing Search:
          Path:  Arad → Timisoara → Lugoj → Mehadia → Drobeta → Craiova → Rimnicu → Pitesti → Bucharest
          Cost:  586

     Simulated Annealing Search:
          Path:  Arad → Sibiu → Rimnicu → Pitesti → Bucharest
          Cost:  460
```

### Notes
- The precision of the simulated annealing search can be changed by manipulating the `number_of_iterations` variable in the `SimulatedAnnealingSearch` method in `RomaniaCityApp.py`. By default, it is set to 10 iterations. The precision can also be changed by manipulating the `temperature` variable in the `SimulatedAnnealingSearch` method in `RomaniaCityApp.py`. By default, it is set to 100. Under current implementation, there is a possibility of returning INF path length when using lower iteration counts or higher starting temperatures.







