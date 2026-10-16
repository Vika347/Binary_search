from node import Node


# бинарное дерево поиска
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

    # проверка существования
    def exists(self, x):
        node = self.root

        while node is not None:
            if x == node.value:
                return True
            elif x < node.value:
                node = node.left
            else:
                node = node.right

        return False

    # поиск минимального
    def find_min(self, node):
        while node.left is not None:
            node = node.left
        return node.value

    # удаление
    def delete(self, x):
        self.root = self._delete(self.root, x)

    def _delete(self, node, x):
        if node is None:
            return None

        if x < node.value:
            node.left = self._delete(node.left, x)

        elif x > node.value:
            node.right = self._delete(node.right, x)

        else:
            # нет левого ребёнка
            if node.left is None:
                return node.right

            # нет правого ребёнка
            if node.right is None:
                return node.left

            # два ребёнка
            value = self.find_min(node.right)
            node.value = value
            node.right = self._delete(node.right, value)

        return node

    # вычисление высоты дерева
    def height(self, node):
        if node is None:
            return 0

        left = self.height(node.left)
        right = self.height(node.right)

        return max(left, right) + 1

    # получение высоты
    def tree_height(self):
        return self.height(self.root)

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

        if not result:
            return "Empty"

        return " ".join(result)
