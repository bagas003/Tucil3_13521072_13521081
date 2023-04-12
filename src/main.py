import astar
import ucs
from utility import *

while True:
    inp = 0

    filename = input("\nEnter file name:\n>> ")
    try:
        graph = readFile(filename)
    except ValueError:
        print("There is something wrong with your input file!")
        continue
    except FileNotFoundError:
        print("No file .txt found, Please check your file name or its directory.")
        continue
    except IsADirectoryError:
        print(("Please enter your file name!"))
        continue


    while True:
        start, goal = input_destination(graph)

        inputAlg = int(input("\n Choose your algorithm :\n1. UCS \n2. A* (A Star)\n>>"))

        if(inputAlg == 1):
            path = ucs.ucs(graph, start, goal)
        elif (inputAlg == 2):
            path = astar.a_star(graph, start, goal)
        else:
            print("Invalid input. Try again.")
            continue

        print_path(path)
        print(f"Shortest path distance: {get_total_dist(graph, path):.2f} m")
        if input("\nShow path? (Y/N):\n>> ").lower().find("y") != -1:
            show_path(graph, path)
        
        temp = input("\nContinue?\n1. Continue with the same graph\n2. Continue with different graph\n3. Quit\n>> ")
        while not temp.isnumeric() or int(temp) < 1 or int(temp) > 3:
            print("Invalid input!")
            temp = input("\nContinue?\n1. Continue with the same graph\n2. Continue with different graph\n3. Quit\n>> ")
    
        inp = int(temp)
        if inp == 2 or inp == 3:
            break

    if inp == 3:
        break
