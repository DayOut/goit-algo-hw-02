import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вершин (зупинки, станції тощо)
nodes = ["A", "B", "C", "D", "E", "F"]
G.add_nodes_from(nodes)

# Додавання ребер (дороги, маршрути тощо)
edges = [("A", "B"), ("A", "C"), ("B", "C"), ("B", "D"), ("C", "E"), ("D", "E"), ("E", "F")]
G.add_edges_from(edges)

# Візуалізація графа
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color="skyblue", node_size=2000, edge_color="gray", font_size=15, font_weight="bold")
plt.title("Транспортна мережа міста")
plt.show()

# Аналіз основних характеристик
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_centrality = nx.degree_centrality(G)
average_degree = sum(dict(G.degree()).values()) / num_nodes

# Виведення результатів
print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print(f"Ступені вершин: {dict(G.degree())}")
print(f"Центральність ступеня: {degree_centrality}")
print(f"Середній ступінь: {average_degree:.2f}")