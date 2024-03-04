from SimpleProblemSolvingAgent import SimpleProblemSolvingAgent
from romania_map import romania_map

############################################################################################################
# Romania City App
# John DeLeo
# CS534
# WPI
# IP2
############################################################################################################
# This app will help you find the best path between two cities in Romania.
# This app uses real world data to calculate the distances between cities in Romania.
# The app uses the following search strategies to find the best path:
#     - Greedy Best First Search
#     - A* Search
#     - Hill Climbing Search
#     - Simulated Annealing Search
# The app will prompt the user to enter a start city and a goal city.
# The app will then calculate the best path between the two cities using the above search strategies.
# The app will then prompt the user to find the best path between another pair of cities.
############################################################################################################
# Main function - This function is the entry point of the program.
############################################################################################################

def main():
    # list of valid cities user can enter
    valid_cities = list(romania_map.nodes())
    valid_cities.sort()

    # print the welcome message
    print()
    print("Welcome to Romania City App")
    print()
    print("This app will help you find the best path between two cities in Romania.")
    print()
    print("This app uses real world data to calculate the distances between cities in Romania.")

    # inner_main is a recursive function that prompts the user to enter a start city and a goal city.
    def inner_main():
        print()
        print("Valid cities are: ", ", ".join(valid_cities))
        print()

        start_city = input("Enter a starting city: ")
        print()
        goal_city = input("Enter a destination city: ")
        print()
        valid_check = True

        # check if the start city is valid
        if start_city not in romania_map.nodes():
            valid_check = False
            print("Start city not found. Please enter a valid start city.")
            print()

        # check if the goal city is valid
        if goal_city not in romania_map.nodes():
            valid_check = False
            print("Goal city not found. Please enter a valid goal city.")
            print()

        # check if the start and goal cities are the same
        if goal_city == start_city:
            valid_check = False
            print("The start and destination cities cannot be the same. Please enter two different cities.")
            print()

        if not valid_check:
            print("Valid cities are: ", ", ".join(valid_cities))
            print()
            input("Press enter to try again...")
            print()
            inner_main()
            return

        # create a SimpleProblemSolvingAgent object from SimpleProblemSolvingAgent.py. 
        # Takes in the graph, user entered start city, and user entered goal city.
        agent = SimpleProblemSolvingAgent(romania_map, start_city, goal_city)

        # greedy best first search
        bfs_path, bfs_cost = agent.search(strategy='greedy_best_first')

        # print the path and cost of greedy best first search
        print("Greedy Best First Search:")
        path_str = ""
        for i in bfs_path:
            path_str += i + " → "
        print("     Path: ", path_str[:-3])
        print("     Cost: ", bfs_cost)
        print()

        # a* search
        astar_path, astar_cost = agent.search(strategy='a_star')
        
        # print the path and cost of a* search
        print("A* Search:")
        path_str = ""
        for i in astar_path:
            path_str += i + " → "
        print("     Path: ", path_str[:-3])   
        print("     Cost: ", astar_cost)
        print()

        # hill climbing search
        hill_climbing_path, hill_climbing_cost = agent.search(strategy='hill_climbing')
        
        # print the path and cost of hill climbing search
        print("Hill Climbing Search:")
        path_str = ""
        for i in hill_climbing_path:
            path_str += i + " → "
        print("     Path: ", path_str[:-3])
        print("     Cost: ", hill_climbing_cost)
        print()

        # simulated annealing search
        simulated_annealing_path, simulated_annealing_cost = agent.search(strategy='simulated_annealing')

        # print the path and cost of simulated annealing search
        print("Simulated Annealing Search:")
        path_str = ""
        for i in simulated_annealing_path:
            path_str += i + " → "
        print("     Path: ", path_str[:-3])
        print("     Cost: ", simulated_annealing_cost)
        print()

        # prompt the user to find the best path between another pair of cities
        if (input("Would you like to find the best path between another pair of cities? (y/n): ") == 'y'):
            print()
            print("#################################################")
            inner_main()
        else:
            print()
            print("#################################################")
            print()
            print("Thank you for using our app!")
            print()

    inner_main()

############################################################################################################
# End of main function
############################################################################################################

if __name__ == "__main__":
    main()
