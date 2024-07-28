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

# Функція для знаходження шляху за допомогою DFS
def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

# Функція для знаходження шляху за допомогою BFS
def bfs_path(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

# Знаходження шляхів за допомогою DFS та BFS
start_node = "A"
goal_node = "F"

dfs_paths = list(dfs_path(G, start_node, goal_node))
bfs_paths = list(bfs_path(G, start_node, goal_node))

# Виведення результатів
print("Шляхи за допомогою DFS:")
for path in dfs_paths:
    print(path)

print("\nШляхи за допомогою BFS:")
for path in bfs_paths:
    print(path)

# Візуалізація графу
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color="skyblue", node_size=2000, edge_color="gray", font_size=15, font_weight="bold")
plt.title("Транспортна мережа міста")
plt.show()