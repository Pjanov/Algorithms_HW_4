"""
Необходимо превратить собранное на семинаре дерево поиска в полноценное левостороннее 
красно-черное дерево. И реализовать в нем метод добавления новых элементов с 
балансировкой.

Красно-черное дерево имеет следующие критерии:
• Каждая нода имеет цвет (красный или черный)
• Корень дерева всегда черный
• Новая нода всегда красная
• Красные ноды могут быть только левым ребенком
• У краной ноды все дети черного цвета

Соответственно, чтобы данные условия выполнялись, после добавления элемента в дерево 
необходимо произвести балансировку, благодаря которой все критерии выше 
станут валидными. Для балансировки существует 3 операции – левый малый поворот, 
правый малый поворот и смена цвета.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.color = "RED"


class RedBlackTree:
    def __init__(self):
        self.root = None

    # Проверяем, является ли узел красным
    def is_red(self, node):
        if node is None:
            return False
        return node.color == "RED"

    # Поворот влево
    def rotate_left(self, node):
        temp = node.right
        node.right = temp.left
        temp.left = node
        temp.color = node.color
        node.color = "RED"
        return temp

    # Поворот вправо
    def rotate_right(self, node):
        temp = node.left
        node.left = temp.right
        temp.right = node
        temp.color = node.color
        node.color = "RED"
        return temp

    # Функция перекрашивания узлов
    def flip_colors(self, node):
        node.color = "RED"
        node.left.color = "BLACK"
        node.right.color = "BLACK"

    # Добавление узла
    def add_node(self, data):
        if self.root is None:
            self.root = Node(data)
            self.root.color = "BLACK"
            return

        self.root = self._add_node(self.root, data)
        self.root.color = "BLACK"

    # Рекурсивная функция добавления узла
    def _add_node(self, node, data):
        if node is None:
            return Node(data)
        if data < node.data:
            # Добавляем узел слева, если значение меньше текущего узла
            node.left = self._add_node(node.left, data)
        elif data > node.data:
            # Добавляем узел справа, если значение больше текущего узла
            node.right = self._add_node(node.right, data)

        # Проверяем условия и выполняем повороты и перекрашивания
        if self.is_red(node.right) and not self.is_red(node.left):
            node = self.rotate_left(node)
        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self.rotate_right(node)
        if self.is_red(node.left) and self.is_red(node.right):
            self.flip_colors(node)
        return node


# В данной реализации в методе _add_node() происходит добавление новой ноды и ее
# последующая балансировка по условиям красно-черного дерева. Методы rotate_left(),
# rotate_right() и flip_colors() выполняют соответствующие операции по балансировке.
# Метод is_red() проверяет, является ли данная нода красной.
# Пример использования:


tree = RedBlackTree()
tree.add_node(10)
tree.add_node(5)
tree.add_node(15)
tree.add_node(3)
tree.add_node(8)
tree.add_node(12)
tree.add_node(18)


# Теперь дерево будет балансироваться автоматически при добавлении новых элементов.
# Для проверки правильности работы, можно выполнить метод print_tree(),
# который выводит значения элементов дерева в порядке возрастания:
def print_tree(node):
    if node:
        print_tree(node.left)
        print(node.data)
        print_tree(node.right)


print_tree(tree.root)
