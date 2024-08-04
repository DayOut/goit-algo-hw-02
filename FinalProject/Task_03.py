import heapq

class Graph:
    def __init__(self, num_vertices):
        self.v = num_vertices
        self.edges = [[] for _ in range(num_vertices)]

    def add_edge(self, u, v, weight):
        self.edges[u].append((v, weight))
        self.edges[v].append((u, weight))

def dijkstra(graph, start_vertex):
    distances = {vertex: float('infinity') for vertex in range(graph.v)}
    distances[start_vertex] = 0
    priority_queue = [(0, start_vertex)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph.edges[current_vertex]:
            distance = current_distance + weight

            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Приклад використання
graph = Graph(6)
graph.add_edge(0, 1, 5)
graph.add_edge(0, 2, 1)
graph.add_edge(1, 2, 2)
graph.add_edge(1, 3, 3)
graph.add_edge(2, 3, 8)
graph.add_edge(2, 4, 10)
graph.add_edge(3, 4, 2)
graph.add_edge(3, 5, 1)
graph.add_edge(4, 5, 7)

start_vertex = 0
distances = dijkstra(graph, start_vertex)
print("Найкоротші шляхи від вершини", start_vertex, "до всіх інших вершин:")
print(distances)