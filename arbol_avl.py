from cola import Queue
class BinaryTree:
    class __Node:
        def __init__(self, value, left=None, right=None, other_value=None):
            self.value = value
            self.left = left
            self.right = right
            self.other_value = other_value
            self.height = 0

    def __init__(self):
        self.root = None

    def height_node(self, root):
        if root is None:
            return -1
        else:
            return root.height

    def update_height(self, root):
        if root is not None:
            left_height = self.height_node(root.left)
            right_height = self.height_node(root.right)
            root.height = max(left_height, right_height) + 1

    def simple_rotation(self, root, control):
        if control:
            aux = root.left
            root.left = aux.right
            aux.right = root
        else:
            aux = root.right
            root.right = aux.left
            aux.left = root
        self.update_height(root)
        self.update_height(aux)
        root = aux
        return root

    def double_rotation(self, root, control):
        if control:
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else:
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        return root

    def balancing(self, root):
        if root is not None:
            balance = self.height_node(root.left) - self.height_node(root.right)
            if balance == 2:
                if self.height_node(root.left.left) >= self.height_node(root.left.right):
                    root = self.simple_rotation(root, True)
                else:
                    root = self.double_rotation(root, True)
            elif balance == -2:
                if self.height_node(root.right.right) >= self.height_node(root.right.left):
                    root = self.simple_rotation(root, False)
                else:
                    root = self.double_rotation(root, False)
        return root

    def insert_node(self, value, other_value=None):
        def __insert(root, value, other_value=None):
            if root is None:
                return BinaryTree.__Node(value, other_value=other_value)
            elif value < root.value:
                root.left = __insert(root.left, value, other_value)
            elif value > root.value:
                root.right = __insert(root.right, value, other_value)
            else:
                if isinstance(root.other_value, list):
                    root.other_value.append(other_value)
                else:
                    root.other_value = [root.other_value, other_value]
            root = self.balancing(root)
            self.update_height(root)
            return root

        self.root = __insert(self.root, value, other_value)

    def search(self, key):
        def __search(root, key):
            if root is not None:
                if root.value == key:
                    return root
                elif key < root.value:
                    return __search(root.left, key)
                else:
                    return __search(root.right, key)
            return None

        return __search(self.root, key)

    def preorden(self):
        def __preorden(root):
            if root is not None:
                print(root.value)
                __preorden(root.left)
                __preorden(root.right)

        if self.root is not None:
            __preorden(self.root)

    def contar_super_heroes(self):
        def __contar_super_heroes(root):
            counter = 0
            if root is not None:
                if root.other_value.get('is_hero') is True:
                    counter = 1
                counter += __contar_super_heroes(root.left)
                counter += __contar_super_heroes(root.right)
            return counter

        return __contar_super_heroes(self.root)

    def inorden(self):
        def __inorden(root, result):
            if root is not None:
                __inorden(root.left, result)
                result.append(root.other_value)
                __inorden(root.right, result)
            return result

        if self.root is not None:
            return __inorden(self.root, [])
        return []

    def postorden(self):
        def __postorden(root):
            if root is not None:
                __postorden(root.right)
                print(root.value)
                __postorden(root.left)

        if self.root is not None:
            __postorden(self.root)

    def inorden_villanos(self):
        def __inorden_villanos(root):
            if root is not None:
                __inorden_villanos(root.left)
                if root.other_value.get('is_hero') is not True:
                    print(root.value)
                __inorden_villanos(root.right)

        if self.root is not None:
            __inorden_villanos(self.root)

    def inorden_superheros_start_with(self, start):
        def __inorden_superheros_start_with(root, start):
            if root is not None:
                __inorden_superheros_start_with(root.left, start)
                if root.other_value.get('is_hero') is True and root.value.startswith(start):
                    print(root.value)
                __inorden_superheros_start_with(root.right, start)

        if self.root is not None:
            __inorden_superheros_start_with(self.root, start)

    def proximity_search(self, search_value):
        matches = []
        def __proximity_search(root, search_value, matches):
            if root is not None:
                __proximity_search(root.left, search_value, matches)
                if search_value.lower() in root.value.lower():
                    matches.append(root.other_value)
                __proximity_search(root.right, search_value, matches)
        __proximity_search(self.root, search_value, matches)
        return matches

    def search_by_type(self, tipo):
        matches = []
        def __search_by_type(root, tipo, matches):
            if root is not None:
                if tipo.lower() in [t.lower() for t in root.value.split('/')]:
                    if isinstance(root.other_value, list):
                        matches.extend(root.other_value)
                    else:
                        matches.append(root.other_value)
                __search_by_type(root.left, tipo, matches)
                __search_by_type(root.right, tipo, matches)
        __search_by_type(self.root, tipo, matches)
        return matches

    def by_level(self):
        pendientes = Queue()
        result = []
        if self.root is not None:
            pendientes.arrive(self.root)

        while pendientes.size() > 0:
            node = pendientes.attention()
            result.append((node.height, node.value))
            if node.left is not None:
                pendientes.arrive(node.left)
            if node.right is not None:
                pendientes.arrive(node.right)
        return result

    def delete_node(self, value):
        def __replace(root):
            if root.right is None:
                return root.left, root
            else:
                root.right, replace_node = __replace(root.right)
                return root, replace_node

        def __delete(root, value):
            value_delete = None
            extra_data_delete = None
            if root is not None:
                if value < root.value:
                    root.left, value_delete, extra_data_delete = __delete(root.left, value)
                elif value > root.value:
                    root.right, value_delete, extra_data_delete = __delete(root.right, value)
                else:
                    value_delete = root.value
                    extra_data_delete = root.other_value
                    if root.left is None:
                        return root.right, value_delete, extra_data_delete
                    elif root.right is None:
                        return root.left, value_delete, extra_data_delete
                    else:
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value
                        root.other_value = replace_node.other_value
                root = self.balancing(root)
                self.update_height(root)
            return root, value_delete, extra_data_delete

        delete_value = None
        delete_extra_value = None
        if self.root is not None:
            self.root, delete_value, delete_extra_value = __delete(self.root, value)
        return delete_value, delete_extra_value

arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()

# tree = BinaryTree()

# tree.insert_node('B')
# tree.insert_node('W')
# tree.insert_node('V')
# tree.insert_node('I')
# tree.insert_node('M')
# tree.insert_node('R')
# tree.insert_node('Z')
# tree.root = tree.balancing(tree.root)
# for i in range(1, 16):
#     tree.insert_node(i)
#     tree.by_level()
#     a = input()


# print('diferencia de altura', tree.height(tree.root.right) - tree.height(tree.root.left))
# tree.insert_node(19)
# tree.insert_node(7)
# tree.insert_node(31)
# tree.insert_node(11)
# tree.insert_node(10)
# tree.insert_node(45)
# tree.insert_node(22)
# tree.insert_node(27)

# pos = tree.search(27)
# if pos:
#     print('lo encontre', pos.value)
# else:
#     print('no esta')

# tree.delete_node(7)
# tree.delete_node(11)
# tree.delete_node(31)
# tree.delete_node(27)
# tree.delete_node(45)
# tree.delete_node(22)
# tree.delete_node(19)
# tree.delete_node(10)
# tree.insert_node(27)

# print(tree.delete_node(100))
# tree.preorden()

# print(tree.root.right)

# tree.by_level()
