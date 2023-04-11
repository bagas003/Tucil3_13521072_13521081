import queue

def ucs(graph, start, goal):
    prioQueue = queue.PriorityQueue()
    prioQueue.put((0, start, [])) # cost = 0 , starting node, path = " "
    visited = set()

    while not prioQueue.empty():
        (totalCost, currentNode, path) = prioQueue.get() # Get the front of queue based on its weight

        if currentNode in visited: #currentNode already visited, continue next iteration
            continue

        path += [currentNode]

        if currentNode == goal:
            return path

        visited.add(currentNode)

        for nextNode in graph.neighbors(currentNode):
            tempCost = graph.get_edge_data(currentNode, nextNode)['weight']
            if nextNode not in visited:
                nextCost = totalCost + tempCost
                newPath = path.copy()  # make a copy of the current path before updating it
                newPath += [currentNode]  # add the current node to the new path
                prioQueue.put((nextCost, nextNode, newPath))


    return None