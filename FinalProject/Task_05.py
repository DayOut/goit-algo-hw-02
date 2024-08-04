import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import heapq

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree_animation(tree_root, order, order_type="DFS"):
    fig, ax = plt.subplots(figsize=(12, 8))

    # Отримуємо позиції та кольори вузлів
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(nx.DiGraph(), tree_root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    def update(num):
        colors = ['skyblue' for _ in tree.nodes()]
        for idx, node in enumerate(order[:num + 1]):
            node_intensity = idx / len(order)
            colors[list(tree.nodes()).index(node.id)] = (0, 0, 1 - 0.7 * node_intensity)
            nx.draw(tree, pos=pos, labels=labels, node_color=colors, node_size=2500, arrows=False, ax=ax)
            ax.set_title(f"{order_type} Order Step {num + 1}: Visiting Node {node.val}")

    ani = animation.FuncAnimation(fig, update, frames=len(order), repeat=True)
    plt.show()

def heapify(arr):
    heapq.heapify(arr)
    nodes = {}
    for i, val in enumerate(arr):
        node = Node(val)
        nodes[i] = node
        if i != 0:
            parent = (i - 1) // 2
            if not nodes[parent].left:
                nodes[parent].left = node
            else:
                nodes[parent].right = node
    return nodes[0]


def dfs(node, visited=None, order=None):
    if visited is None:
        visited = set()
    if order is None:
        order = []
    if node and node.id not in visited:
        visited.add(node.id)
        order.append(node)
        dfs(node.left, visited, order)
        dfs(node.right, visited, order)
    return order

def bfs(root):
    visited, order = set(), []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node and node.id not in visited:
            visited.add(node.id)
            order.append(node)
            queue.append(node.left)
            queue.append(node.right)
    return order

# Приклад масиву значень
values = [3, 9, 2, 1, 4, 5]

# Створення купи та анімація обходу
root = heapify(values)
dfs_order = dfs(root)
bfs_order = bfs(root)

draw_tree_animation(root, dfs_order, "DFS")
draw_tree_animation(root, bfs_order, "BFS")