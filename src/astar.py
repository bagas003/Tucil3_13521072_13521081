import heapq
import utility

def a_star(graph, start, goal):
    # Initialize the starting node and priority queue
    frontier = [(0, [start])]
    visited = set()
    path_costs = {start: 0}

    # A* algorithm
    while frontier:
        # Pop the path with the lowest total cost from the priority queue
        current_cost, current_path = heapq.heappop(frontier)
        current_node = current_path[-1]

        # If the current node is the goal, return the path to it
        if current_node == goal:
            return current_path

        # Add the current node to the visited set
        visited.add(current_node)

        # Explore the neighbors of the current node
        for neighbor in graph[current_node]:
            # Calculate the cost of the path to the neighbor node
            neighbor_cost = path_costs[current_node] + graph[current_node][neighbor]['weight']

            # If the neighbor node has not been visited or the new path cost is less than the old one
            if neighbor not in visited or neighbor_cost < path_costs[neighbor]:
                # Update the path cost and priority queue
                path_costs[neighbor] = neighbor_cost
                total_cost = neighbor_cost + utility.dist(graph, neighbor, goal)
                new_path = current_path + [neighbor]
                heapq.heappush(frontier, (total_cost, new_path))

    # If no path was found, return None
    return None