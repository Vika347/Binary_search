from node import Node


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # добавление элемента
    def add(self, x):
        self.root = self._add(self.root, x)

    def _add(self, node, x):
        if node is None:
            return Node(x)

        if x < node.value:
            node.left = self._add(node.left, x)
        elif x > node.value:
            node.right = self._add(node.right, x)

        return node

    # левый поворот
    def rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        return new_root

    # правый поворот
    def rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        return new_root

    # поворот вокруг заданной вершины
    def rotate(self, x, direction):
        self.root = self._rotate(self.root, x, direction)

    def _rotate(self, node, x, direction):
        if node is None:
            return None

        if x < node.value:
            node.left = self._rotate(node.left, x, direction)

        elif x > node.value:
            node.right = self._rotate(node.right, x, direction)

        else:
            if direction == "left":
                return self.rotate_left(node)
            else:
                return self.rotate_right(node)

        return node

    # прямой обход
    def preorder(self, node, result):
        if node is None:
            return

        result.append(str(node.value))
        self.preorder(node.left, result)
        self.preorder(node.right, result)

    # получение дерева в прямом обходе
    def print_tree(self):
        result = []
        self.preorder(self.root, result)
        return " ".join(result)
