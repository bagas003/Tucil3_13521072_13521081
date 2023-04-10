import astar
from utility import *

while True:
    inp = 0

    filename = input("\nEnter file name:\n>> ")
    graph = readFile(filename)

    if input("\nShow graph? (Y/N):\n>> ").lower().find("y") != -1:
        show(graph)

    while True:
        start, goal = input_destination(graph)

        path = astar.a_star(graph, start, goal)

        print_path(path)
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
