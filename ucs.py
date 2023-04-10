from queue import PriorityQueue

def ucs(graph, start, goal):
    prioQ = PriorityQueue()
    prioQ.put(start, 0, [])
    visited = []

    while(prioQ.not_empty):
        curretNode, cost, path = prioQ.get()

        if curretNode in visited:
            continue

        path += curretNode

        if(curretNode == goal):
            return cost, path
        
        visited.append(curretNode)

        for (nextNode, c) in graph[curretNode].items():
            if(nextNode not in visited):
                nextCost = cost + c
                prioQ.put(nextNode, nextCost, path)

    return None