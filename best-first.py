import heapq

def best_first_search(graph, start, goal, heuristic):
    # Priority queue to store the nodes to be explored
    priority_queue = []
    # Push the start node with its heuristic value
    heapq.heappush(priority_queue, (heuristic[start], start))
    
    # Set to keep track of visited nodes
    visited = set()
    
    # Dictionary to keep track of the path
    came_from = {start: None}
    
    while priority_queue:
        # Get the node with the lowest heuristic value
        current_heuristic, current_node = heapq.heappop(priority_queue)
        
        # If the goal is reached, reconstruct the path
        if current_node == goal:
            path = []
            while current_node:
                path.append(current_node)
                current_node = came_from[current_node]
            return path[::-1]
        
        # Mark the current node as visited
        visited.add(current_node)
        
        # Explore neighbors
        for neighbor, cost in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))
                came_from[neighbor] = current_node
    
    # Return None if no path is found
    return None

# Example graph
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 2), ('E', 4)],
    'C': [('F', 2)],
    'D': [('G', 1)],
    'E': [('G', 1)],
    'F': [('G', 1)],
    'G': []
}

# Example heuristic function
heuristic = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 4,
    'E': 3,
    'F': 2,
    'G': 0
}

# Run the Best-First Search
start = 'A'
goal = 'G'
path = best_first_search(graph, start, goal, heuristic)

print("Path found:", path)
