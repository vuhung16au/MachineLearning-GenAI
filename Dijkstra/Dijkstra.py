import heapq

def dijkstra(graph, start_node, end_node):
    """
    Applies Dijkstra's algorithm to find the shortest path between two nodes
    in a weighted graph.

    Args:
        graph (dict): A dictionary representing the graph where keys are nodes
                      and values are dictionaries of neighboring nodes with
                      their edge weights.
        start_node: The starting node.
        end_node: The destination node.

    Returns:
        tuple: A tuple containing the shortest distance and the shortest path
               (as a list of nodes) from the start to the end node.
               Returns (infinity, []) if no path exists.
    """
    # Initialization:
    # Mark each location with infinite travel time, except the starting location (marked as 0)
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    
    # Priority queue to store vertices to be processed
    priority_queue = [(0, start_node)]  # (distance, node)
    
    # Track the preceding node for path reconstruction
    previous_nodes = {node: None for node in graph}
    
    # Keep track of explored vertices
    explored = set()
    
    # Iteration:
    while priority_queue:
        # Choose Next Vertex:
        # Select the unexplored vertex with the current shortest estimated travel time
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Skip if we've already explored this vertex or found a better path
        if current_node in explored or current_distance > distances[current_node]:
            continue
        
        # Mark this vertex as explored
        explored.add(current_node)
        
        # Completion check:
        # If we've reached the destination, we can reconstruct the path and return
        if current_node == end_node:
            path = []
            # Reconstruct the path by following the preceding nodes
            while current_node is not None:
                path.insert(0, current_node)
                current_node = previous_nodes[current_node]
            return distances[end_node], path
        
        # Update Estimates:
        # For each neighbor of the current vertex
        for neighbor, weight in graph.get(current_node, {}).items():
            # Skip already explored neighbors
            if neighbor in explored:
                continue
                
            # Calculate new potential distance
            distance = current_distance + weight
            
            # If this offers a shorter path, update the neighbor's distance estimate
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    # Result:
    # If we've exhausted all possible paths without reaching the destination,
    # there is no path from start to end
    return float('inf'), []

# Let's find the shortest path in a sample graph
# Example graph represented as an adjacency list with weights
# The graph is undirected and weighted
# Each key is a node, and the value is a dictionary of neighboring nodes with their edge weights

graph = {
    'A': {'C': 3, 'F': 2},
    'B': {'D': 1, 'E': 2, 'G': 2},
    'C': {'A': 3, 'E': 1, 'F': 2, 'D': 4},
    'D': {'C': 4, 'B': 1, 'E': 1},
    'E': {'C': 1, 'D': 1, 'F': 3, 'B': 2},
    'F': {'A': 2, 'C': 2, 'E': 3, 'G': 5},
    'G': {'B': 2, 'F': 5}
}

# Example usage: Find the shortest path from node A to node B
start_node = 'A'
end_node = 'B'
shortest_distance, shortest_path = dijkstra(graph, start_node, end_node)

print(f"Shortest distance from {start_node} to {end_node}: {shortest_distance}")
print(f"Shortest path from {start_node} to {end_node}: {shortest_path}")

# You can change the start_node and end_node to find the shortest path
# between any two nodes in the graph.