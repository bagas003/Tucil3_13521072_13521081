import heapq
import utility

def a_star(graph, start, finish):
    # Initialize node and priority queue
    check = [(0, [start])]
    visited = set()
    cost = {start: 0}

    while check:
        # pop the path with the lowest total cost
        current_cost, current_path = heapq.heappop(check)
        node = current_path[-1]

        # return the path if node is goal
        if node == finish:
            return current_path

        # set node to visited
        visited.add(node)

        # explore the neighbors
        for neighbor in graph[node]:
            # calculate the cost
            neighbor_cost = cost[node] + graph[node][neighbor]['weight']

            if neighbor not in visited or neighbor_cost < cost[neighbor]:
                # Update the path cost and priority queue
                cost[neighbor] = neighbor_cost
                total_cost = neighbor_cost + utility.dist(graph, neighbor, finish)
                new_path = current_path + [neighbor]
                heapq.heappush(check, (total_cost, new_path))

    # no path was found, return None
    return None