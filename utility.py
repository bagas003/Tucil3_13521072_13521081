import networkx as nx
import matplotlib.pyplot as plt
import math

def dist(graph, node1, node2):
    return math.dist(graph.nodes[node1]['pos'], graph.nodes[node2]['pos'])

def readFile(filename):
    f = open(filename.encode('unicode_escape').decode().replace("\"", ""), 'r')
    raw = f.readlines()

    graph = nx.Graph()

    n = int(raw[0])
    for i in range(1,n+1):
        name = raw[2*i-1].replace("\n","")
        [y, x] = [float(i)*111139 for i in raw[2*i].replace(",","").split(" ")]

        graph.add_node(name, pos=(x, y))

    nodes = list(graph.nodes())
    
    for i in range(n*2+1, n*3):
        temp = [int(j) for j in raw[i].split(" ")]
        for j in range(n):
            if temp[j] == 1:
                n1, n2 = nodes[i-n*2-1], nodes[j]
                w = dist(graph, n1, n2)
                graph.add_edge(n1, n2, weight=w)
    
    return graph


def show(graph):
    coor = nx.get_node_attributes(graph, 'pos')
    nx.draw(graph, coor, with_labels=True)
    edge_labels = {(u, v): f"{w:.2f}" for u, v, w in graph.edges(data='weight')}
    nx.draw_networkx_edge_labels(graph, pos=coor, edge_labels=edge_labels)
    plt.show()


def show_path(graph, path):
    coor = nx.get_node_attributes(graph, 'pos')

    path_graph = nx.Graph()
    path_graph.add_node(path[0], pos=coor[path[0]])
    for i in range(1,len(path)):
        path_graph.add_node(path[i], pos=coor[path[i]])
        path_graph.add_edge(path[i-1], path[i], weight=dist(graph, path[i-1], path[i]))

    path_coor = nx.get_node_attributes(path_graph, 'pos')

    nx.draw(graph, coor, with_labels=True)
    nx.draw(path_graph, path_coor, edge_color='red', node_color='red')
    edge_labels = {(u, v): f"{w:.2f}" for u, v, w in graph.edges(data='weight')}
    nx.draw_networkx_edge_labels(graph, pos=coor, edge_labels=edge_labels)
    plt.show()



def input_destination(graph):
    nodes = list(graph.nodes())

    print("\nNodes list:")    

    i = 1
    for node in nodes:
        print(f"{i}. {node}")
        i += 1
    
    n1 = 0
    n2 = 0

    while n1 == 0:
        temp = input("\nEnter starting point number.\nEnter 0 to show graph\n>> ")
        if not temp.isnumeric() or int(temp) < 0 or int(temp) > len(nodes)+1:
            print("Invalid input!")
            continue

        n1 = int(temp)
        if n1 == 0:
            show(graph)
        
    
    while n2 == 0:
        temp = input("\nEnter goal point number.\nEnter 0 to show graph\n>> ")
        if not temp.isnumeric() or int(temp) < 0 or int(temp) > len(nodes)+1:
            print("Invalid input!")
            continue
        
        n2 = int(temp)
        if n2 == 0:
            show(graph)
    
    return nodes[n1-1], nodes[n2-1]

def print_path(path):
    print('\nShortest path: ', end='')
    if path != None:
        print(path[0], end='')
        for i in range(1,len(path)):
            print(' - ', path[i], end='')
    else:
        print('None')
    print()
            



if __name__ == "__main__":
    show(readFile("cisitu.txt"))
