import uuid
import networkx as nx
import matplotlib.pyplot as plt
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

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    plt.figure(figsize=(12, 8))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
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

def dfs(node, visited=None):
    if visited is None:
        visited = []
    if node:
        visited.append(node.val)
        dfs(node.left, visited)
        dfs(node.right, visited)
    return visited

def bfs(root):
    visited = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            visited.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    return visited

# Приклад масиву значень
values = [3, 9, 2, 1, 4, 5]

# Створення купи та відображення дерева
root = heapify(values)
draw_tree(root)

# Виконання обходу в глибину та в ширину
dfs_result = dfs(root)
bfs_result = bfs(root)

print("DFS Order:", dfs_result)
print("BFS Order:", bfs_result)