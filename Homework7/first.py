import random

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.height = 1


class AVLTree:
    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and key < root.left.val:
            return self.right_rotate(root)
        if balance < -1 and key > root.right.val:
            return self.left_rotate(root)
        if balance > 1 and key > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and key < root.right.val:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def find_maximum_value(self, root):
        current_node = root
        while current_node.right is not None:
            current_node = current_node.right
        return current_node.val

    def find_minimum_value(self, root):
        current_node = root
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.val

    def find_sum_of_values(self, root):
        if root is None:
            return 0
        return root.val + self.find_sum_of_values(root.left) + self.find_sum_of_values(root.right)

# Приклад використання
if __name__ == "__main__":
    tree = AVLTree()
    root = None
    #keys = [10, 20, 30, 40, 50, 25]
    keys = [random.randint(1,100) for _ in range(20)]
    print(f"Expected sum: {sum(keys)}")
    print(keys)

    for key in keys:
        root = tree.insert(root, key)

    max_value = tree.find_maximum_value(root)
    print(f"Найбільше значення в AVL-дереві: {max_value}")

    min_value = tree.find_minimum_value(root)
    print(f"Найменше значення в AVL-дереві: {min_value}")

    total_sum = tree.find_sum_of_values(root)
    print(f"Сума всіх значень в AVL-дереві: {total_sum}")