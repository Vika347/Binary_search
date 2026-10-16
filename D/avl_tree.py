
from node import Node


# AVL-дерево
class AVLTree:
    def __init__(self):
        self.root = None

    # получение высоты вершины
    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    # обновление высоты вершины
    def update_height(self, node):
        left = self.get_height(node.left)
        right = self.get_height(node.right)
        node.height = max(left, right) + 1

    # вычисление баланса вершины
    def get_balance(self, node):
        return self.get_height(node.right) - self.get_height(node.left)

    # левый поворот
    def rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        self.update_height(node)
        self.update_height(new_root)

        return new_root

    # правый поворот
    def rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        self.update_height(node)
        self.update_height(new_root)

        return new_root

    # балансировка дерева
    def fix_balance(self, node):
        self.update_height(node)
        balance = self.get_balance(node)

        # перевес вправо
        if balance == 2:
            if self.get_balance(node.right) < 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        # перевес влево
        if balance == -2:
            if self.get_balance(node.left) > 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        return node

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
        else:
            return node

        return self.fix_balance(node)

    # поиск минимальной вершины
    def find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    # удаление элемента
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
            # Нет левого ребёнка
            if node.left is None:
                return node.right

            # Нет правого ребёнка
            if node.right is None:
                return node.left

            # Два ребёнка
            min_node = self.find_min(node.right)
            node.value = min_node.value
            node.right = self._delete(node.right, min_node.value)

        return self.fix_balance(node)

    # проверка существования элемента
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

    # поиск минимального ключа >= x
    def next(self, x):
        node = self.root
        result = None

        while node is not None:
            if node.value >= x:
                result = node.value
                node = node.left
            else:
                node = node.right

        return result

    # поиск максимального ключа <= x
    def prev(self, x):
        node = self.root
        result = None

        while node is not None:
            if node.value <= x:
                result = node.value
                node = node.right
            else:
                node = node.left

        return result

    # получение корня дерева
    def get_root(self):
        if self.root is None:
            return "Empty"
        return str(self.root.value)

    # получение высоты дерева
    def tree_height(self):
        return self.get_height(self.root)

    # прямой обход дерева
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
