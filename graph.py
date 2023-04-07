import matplotlib.pyplot as plt

class Node:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.parent = None

    def __repr__(self):
        return self.name + ": " + str(self.x) + ", " + str(self.y)
    
    def dist(self, other):
        return ((self.x - other.x) ** 2 + (self.y + other.y) ** 2) ** 0.5

    def add_parent(self, other):
        self.parent = other
    

class Graph:
    def __init__(self, num):
        self.num = num
        self.matrix = [[0 for i in range(num)] for j in range(num)]
        self.nodes = []

    def add_node(self, node):
        self.nodes += [node]

    def add_edge(self, idx1, idx2):
        self.matrix[idx1][idx2] = 1
        self.matrix[idx2][idx1] = 1

    def get_index(self, name):
        for i in range(self.num):
            if self.nodes[i].name == name:
                return i
            
    def get_neighbors(self, name):
        neighbors = []
        i = self.get_index(name)
        for j in range(self.num):
            if self.matrix[i][j] == 1:
                neighbors.append(self.nodes[j])
        return neighbors
    
    def show(self):
        x_val = [node.x for node in self.nodes]
        y_val = [node.y for node in self.nodes]

        fig, ax = plt.subplots()
        ax.scatter(x_val, y_val)

        for node in self.nodes:
            ax.text(node.x, node.y, node.name)
            for neighbor in self.get_neighbors(node.name):
                ax.plot([node.x, neighbor.x], [node.y, neighbor.y], color='blue')

        plt.show()


def readFile(filename):
    f = open(filename.encode('unicode_escape').decode().replace("\"", ""), 'r')
    raw = f.readlines()

    g = Graph(int(raw[0]))
    for i in range(1, g.num + 1):
        name = raw[2*i-1].replace("\n","")
        x, y = raw[2*i].split(" ")

        g.add_node(Node(name, int(x), int(y)))
    
    for i in range(g.num*2+1, g.num*3):
        temp = [int(j) for j in raw[i].split(" ")]
        for j in range(g.num):
            if temp[j] == 1:
                g.add_edge(i - g.num*2 - 1, j)

    return g



if __name__ == "__main__":
    g = readFile("input.txt")
    g.show()