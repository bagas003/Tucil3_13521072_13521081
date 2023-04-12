import folium
import webbrowser
import os
from utility import *

# Create a networkx graph
G = readFile("cisitu.txt")

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
    folium.PolyLine(locations=route, color='blue', weight=5).add_to(m)

m.save('src/map.html')
webbrowser.open('file://' + os.path.realpath('map.html'))
