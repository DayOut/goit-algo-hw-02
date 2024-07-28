import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вершин (зупинки, станції тощо)
nodes = ["A", "B", "C", "D", "E", "F"]
G.add_nodes_from(nodes)

# Додавання ребер з вагами (дороги, маршрути тощо)
edges_with_weights = [("A", "B", 4), ("A", "C", 2), ("B", "C", 1), ("B", "D", 5), ("C", "E", 10), ("D", "E", 3), ("E", "F", 8)]
G.add_weighted_edges_from(edges_with_weights)

# Візуалізація графа з вагами
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=2000, edge_color="gray", font_size=15, font_weight="bold")
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Зважена транспортна мережа міста")
plt.show()

# Функція для знаходження найкоротшого шляху за допомогою алгоритму Дейкстри
def dijkstra_paths(graph, source):
    return nx.single_source_dijkstra_path(graph, source)

def dijkstra_lengths(graph, source):
    return nx.single_source_dijkstra_path_length(graph, source)

# Знаходження найкоротших шляхів від кожної вершини
shortest_paths = {}
shortest_lengths = {}

for node in G.nodes:
    shortest_paths[node] = dijkstra_paths(G, node)
    shortest_lengths[node] = dijkstra_lengths(G, node)

# Виведення результатів
print("Найкоротші шляхи між усіма вершинами:")
for start_node in shortest_paths:
    for end_node in shortest_paths[start_node]:
        print(f"Від {start_node} до {end_node}: шлях - {shortest_paths[start_node][end_node]}, довжина - {shortest_lengths[start_node][end_node]}")