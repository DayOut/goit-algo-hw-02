import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Створення графа
G = nx.Graph()

# Додавання вершин (зупинки, станції тощо)
nodes = ["A", "B", "C", "D", "E", "F"]
G.add_nodes_from(nodes)

# Додавання ребер з вагами (дороги, маршрути тощо)
edges_with_weights = [("A", "B", 4), ("A", "C", 2), ("B", "C", 1), ("B", "D", 5), ("C", "E", 10), ("D", "E", 3), ("E", "F", 8)]
G.add_weighted_edges_from(edges_with_weights)


# Функція для знаходження найкоротшого шляху за допомогою алгоритму Дейкстри
def dijkstra(graph, start):
    shortest_paths = {node: float('inf') for node in graph.nodes}
    shortest_paths[start] = 0
    priority_queue = [(0, start)]
    previous_nodes = {node: None for node in graph.nodes}

    while priority_queue:
        current_weight, current_node = heapq.heappop(priority_queue)

        if current_weight > shortest_paths[current_node]:
            continue

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = current_weight + weight
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths, previous_nodes


# Функція для відновлення шляху з попередніх вершин
def reconstruct_path(previous_nodes, start, end):
    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    path.reverse()
    return path if path[0] == start else []


# Знаходження найкоротших шляхів від кожної вершини
shortest_paths = {}
shortest_lengths = {}

for node in G.nodes:
    distances, previous_nodes = dijkstra(G, node)
    shortest_paths[node] = {end: reconstruct_path(previous_nodes, node, end) for end in G.nodes}
    shortest_lengths[node] = distances

# Виведення результатів
print("Найкоротші шляхи між усіма вершинами:")
for start_node in shortest_paths:
    for end_node in shortest_paths[start_node]:
        print(
            f"Від {start_node} до {end_node}: шлях - {shortest_paths[start_node][end_node]}, довжина - {shortest_lengths[start_node][end_node]}")

# Візуалізація графа з вагами
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=2000, edge_color="gray", font_size=15,
        font_weight="bold")
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Зважена транспортна мережа міста")
plt.show()