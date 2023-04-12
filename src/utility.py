import networkx as nx
import math
import folium
import matplotlib.pyplot as plt
import subprocess

def dist(graph, node1, node2):
    x = graph.nodes[node1]['pos']
    y = graph.nodes[node2]['pos']
    return math.dist(x, y)*111139

def readFile(filename):
    filename = "test/" + filename
    f = open(filename.encode('unicode_escape').decode().replace("\"", ""), 'r')
    raw = f.readlines()

    graph = nx.Graph()

    n = int(raw[0])
    for i in range(1,n+1):
        name = raw[2*i-1].replace("\n","")
        [x, y] = [float(i) for i in raw[2*i].replace(",","").split(" ")]

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



def show_path(G, path):
    xmax, ymax, xmin, ymin = 0, 0, 0, 0
    for node in G.nodes():
        [x, y] = [i for i in G.nodes()[node]['pos']]
        if (xmax, ymax, xmin, ymin) == (0, 0, 0, 0):
            xmax, ymax, xmin, ymin = x, y, x, y
        if x > xmax: xmax = x
        if x < xmin: xmin = x
        if y > ymax: ymax = y
        if y < ymin: ymin = y
        

    # Create a folium map
    m = folium.Map(location=[(xmax + xmin)/2, (ymax + ymin)/2], zoom_start=17)

    for node in G.nodes():
        [x, y] = [i for i in G.nodes()[node]['pos']]
        folium.Marker(location=[x, y], popup=node).add_to(m)

    routes = [[]]
    for (node1, node2) in G.edges():
        [x1, y1] = [i for i in G.nodes()[node1]['pos']]
        [x2, y2] = [i for i in G.nodes()[node2]['pos']]
        routes += [[(x1, y1), (x2, y2)]]
    routes = routes[1:]

    for route in routes:
        folium.PolyLine(locations=route, color='orange', weight=5).add_to(m)

    path_route = []
    for p in path:
        [x, y] = [i for i in G.nodes()[p]['pos']]
        path_route += [(x, y)]

    folium.PolyLine(locations=path_route, color='red', weight=5).add_to(m)

    m.save('src/templates/map.html')
    subprocess.run(["python", "src/app.py"])
    # webbrowser.open('file://' + os.path.realpath('map.html'), new=2, autoraise=False)
    


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
        if not temp.isnumeric() or int(temp) < 0 or int(temp) > len(nodes):
            print("Invalid input!")
            continue

        n1 = int(temp)
        if n1 == 0:
            show(graph)
        
    
    while n2 == 0:
        temp = input("\nEnter goal point number.\nEnter 0 to show graph\n>> ")
        if not temp.isnumeric() or int(temp) < 0 or int(temp) > len(nodes):
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


def get_total_dist(graph, path):
    d = 0
    for i in range(1,len(path)):
        d += graph.get_edge_data(path[i-1],path[i])['weight']
    return d
            



if __name__ == "__main__":
    g = readFile('sukoharjo.txt')
    show(g)