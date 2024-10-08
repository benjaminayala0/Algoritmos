from queue import Queue

class BinaryTree:
    class __Node:
        def __init__(self, value, left=None, right=None, other_value=None):
            self.value = value
            self.left = left
            self.right = right
            self.other_value = other_value

    def __init__(self):
        self.root = None

    def insert_node(self, value, other_value=None):
        def __insert(root, value, other_value=None):
            if root is None:
                return BinaryTree.__Node(value, other_value=other_value)
            elif value < root.value:
                root.left = __insert(root.left, value, other_value)
            else:
                root.right = __insert(root.right, value, other_value)
            return root

        self.root = __insert(self.root, value, other_value)

    #b
    def inorden_villanos(self):
        def __inorden_villanos(root):
            if root is not None:
                __inorden_villanos(root.left)
                if root.other_value.get('is_hero') is not True:
                    print(root.value)
                __inorden_villanos(root.right)

        if self.root is not None:
            __inorden_villanos(self.root)

    #c
    def inorden_superheros_start_with(self, start):
        def __inorden_superheros_start_with(root, start):
            if root is not None:
                __inorden_superheros_start_with(root.left, start)
                if root.other_value.get('is_hero') is True and root.value.startswith(start):
                    print(root.value)
                __inorden_superheros_start_with(root.right, start)

        if self.root is not None:
            __inorden_superheros_start_with(self.root, start)

    #d
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

    #e
    def search_and_modify(self, partial_name, new_name):
        def __search_and_modify(root, partial_name, new_name):
            if root is not None:
                if partial_name.lower() in root.value.lower():  # Búsqueda por coincidencia parcial
                    print(f"Modificando {root.value} a {new_name}")
                    root.value = new_name  # Modificar el nombre
                    return root
                elif partial_name < root.value:
                    return __search_and_modify(root.left, partial_name, new_name)
                else:
                    return __search_and_modify(root.right, partial_name, new_name)
            return None

        return __search_and_modify(self.root, partial_name, new_name)

    #f
    def inorden_superheroes_desc(self):
        def __inorden_superheroes_desc(root):
            if root is not None:
                __inorden_superheroes_desc(root.right)
                if root.other_value.get('is_hero') is True:
                    print(root.value)
                __inorden_superheroes_desc(root.left)

        if self.root is not None:
            __inorden_superheroes_desc(self.root)

    #funcion para recorrido por niveles
    def by_level(self):
        pendientes = Queue()
        if self.root is not None:
            pendientes.put(self.root)

        while not pendientes.empty():
            node = pendientes.get()
            print(node.value)
            if node.left is not None:
                pendientes.put(node.left)
            if node.right is not None:
                pendientes.put(node.right)

    #g
    def dividir_en_superheroes_y_villanos(self):
        heroes_tree = BinaryTree()
        villanos_tree = BinaryTree()

        def __dividir(root):
            if root is not None:
                if root.other_value.get('is_hero') is True:
                    heroes_tree.insert_node(root.value, root.other_value)
                else:
                    villanos_tree.insert_node(root.value, root.other_value)
                __dividir(root.left)
                __dividir(root.right)

        __dividir(self.root)

        return heroes_tree, villanos_tree

    #g)I
    def contar_nodos(self):
        def __contar_nodos(root):
            if root is None:
                return 0
            return 1 + __contar_nodos(root.left) + __contar_nodos(root.right)

        return __contar_nodos(self.root)

    #g)II
    def inorden(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(root.value)
                __inorden(root.right)

        if self.root is not None:
            __inorden(self.root)

tree = BinaryTree()

#personajes
tree.insert_node('Iron Man', {'is_hero': True})
tree.insert_node('Capitan America', {'is_hero': True})
tree.insert_node('Doctor Strange', {'is_hero': True})
tree.insert_node('Thanos', {'is_hero': False})
tree.insert_node('Loki', {'is_hero': False})
tree.insert_node('Black Widow', {'is_hero': True})

print("B- Villanos en orden alfabetico:")
tree.inorden_villanos()

print("\nC- Superheroes que empiezan con C:")
tree.inorden_superheros_start_with('C')

print("\nD- Numero total de superheroes en el arbol:")
print(tree.contar_super_heroes())

print("\nE- Modificando Doctor Strange a Dr. Strange:")
tree.search_and_modify("Strange", "Dr. Strange")

print("\nF- Superheroes en orden descendente:")
tree.inorden_superheroes_desc()

heroes_tree, villanos_tree = tree.dividir_en_superheroes_y_villanos()

print("D- \nNumero de nodos en el arbol de superheroes:")
print(heroes_tree.contar_nodos())

print("G)I- \nNumero de nodos en el arbol de villanos:")
print(villanos_tree.contar_nodos())

print("G)II- \nBarrido ordenado alfabeticamente de superheroes:")
heroes_tree.inorden()

print("G)II- \nBarrido ordenado alfabeticamente de villanos:")
villanos_tree.inorden()