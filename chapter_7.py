import heapq


def dijkstra(graph, start):
    # Ensure the start vertex is in the graph
    if start not in graph:
        raise ValueError("Start vertex not in graph")

    # Initialize distances with infinity, except for the start vertex at zero
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0

    # Priority queue for managing vertices to be processed
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Skip processing if a better path has already been found
        if current_distance > distances[current_vertex]:
            continue

        # Explore each adjacent vertex and update paths
        for neighbor, weight in graph[current_vertex].items():
            new_distance = current_distance + weight

            # Update the distance if a shorter path is found
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances


graph = {
    "A": {"B": 1, "C": 4},
    "B": {"A": 1, "C": 2, "D": 5},
    "C": {"A": 4, "B": 2, "D": 1},
    "D": {"B": 5, "C": 1},
}

print(dijkstra(graph, "A"))  # -> {'A': 0, 'B': 1, 'C': 3, 'D': 4}
print(dijkstra(graph, "B"))  # -> {'A': 1, 'B': 0, 'C': 2, 'D': 3}
print(dijkstra(graph, "C"))  # -> {'A': 3, 'B': 2, 'C': 0, 'D': 1}
print(dijkstra(graph, "D"))  # -> {'A': 4, 'B': 3, 'C': 1, 'D': 0}
