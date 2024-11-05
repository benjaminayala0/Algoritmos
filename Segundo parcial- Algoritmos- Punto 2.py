from cola import Queue
from heap import HeapMin
from pila import Stack

class Graph:
    def __init__(self, dirigido=True):
        self.elements = []
        self.dirigido = dirigido

    def show_graph(self):
        print("\nNodos:")
        for index, nodo in enumerate(self.elements):
            print(f"{nodo['value']}")
            print("  Aristas:")
            for arista in nodo['aristas']:
                print(f"    destino: {arista['value']}, peso: {arista['peso']}")
        print()

    def search(self, value):
        for index, element in enumerate(self.elements):
            if element['value'] == value:
                return index
        return None

    def insert_vertice(self, value):
        if self.search(value) is None:
            nodo = {
                'value': value,
                'aristas': [],
                'visitado': False,
            }
            self.elements.append(nodo)

    def insert_arista(self, origen, destino, peso):
        pos_origen = self.search(origen)
        pos_destino = self.search(destino)
        if pos_origen is not None and pos_destino is not None:
            arista = {
                'value': destino,
                'peso': peso
            }
            self.elements[pos_origen]['aristas'].append(arista)
            if not self.dirigido:
                arista = {
                    'value': origen,
                    'peso': peso
                }
                self.elements[pos_destino]['aristas'].append(arista)

    def mark_as_not_visited(self):
        for nodo in self.elements:
            nodo['visitado'] = False

    def get_all_edges(self):
        edges = []
        for nodo in self.elements:
            for arista in nodo['aristas']:
                edges.append((nodo['value'], arista['value'], arista['peso']))
        return edges

    
    def kruskal_mst(self):
        edges = self.get_all_edges()
        edges.sort(key=lambda x: x[2])#ordenar las aristas por peso
        parent = {}
        rank = {}

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            if root1 != root2:
                if rank[root1] > rank[root2]:
                    parent[root2] = root1
                else:
                    parent[root1] = root2
                    if rank[root1] == rank[root2]:
                        rank[root2] += 1

        #iniciar conjuntos
        for nodo in self.elements:
            parent[nodo['value']] = nodo['value']
            rank[nodo['value']] = 0

        mst = []
        for origen, destino, peso in edges:
            if find(origen) != find(destino):
                union(origen, destino)
                mst.append((origen, destino, peso))

        return mst

    def contains_yoda_in_mst(self):
        mst = self.kruskal_mst()
        for edge in mst:
            if "Yoda" in edge:
                return "Yoda si esta"
        return "Yoda no esta"

    
    def max_episodes_shared(self):
        max_peso = 0
        personajes = ("", "")
        for nodo in self.elements:
            for arista in nodo['aristas']:
                if arista['peso'] > max_peso:
                    max_peso = arista['peso']
                    personajes = (nodo['value'], arista['value'])
        return max_peso, personajes

grafo_star_wars = Graph(dirigido=False)

#agregar personajes al grafo (vertices)
personajes = [
    "Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", "C-3PO",
    "Leia Organa", "Rey", "Kylo Ren", "Chewbacca", "Han Solo", "R2-D2", "BB-8"
]

for personaje in personajes:
    grafo_star_wars.insert_vertice(personaje)

#agregar aristas (cantidad de episodios compartidos)
grafo_star_wars.insert_arista("Luke Skywalker", "Darth Vader", 20)
grafo_star_wars.insert_arista("Luke Skywalker", "Han Solo", 1)
grafo_star_wars.insert_arista("Luke Skywalker", "Leia Organa", 3)
grafo_star_wars.insert_arista("Han Solo", "Leia Organa", 3)
grafo_star_wars.insert_arista("Obi-Wan Kenobi", "Darth Vader", 1)
grafo_star_wars.insert_arista("Yoda", "Luke Skywalker", 1)
grafo_star_wars.insert_arista("Rey", "BB-8", 20)
grafo_star_wars.insert_arista("Kylo Ren", "Leia Organa", 4)
grafo_star_wars.insert_arista("Chewbacca", "Han Solo", 50)
grafo_star_wars.insert_arista("R2-D2", "C-3PO", 9)
grafo_star_wars.insert_arista("Luke Skywalker", "Rey", 1)
grafo_star_wars.insert_arista("Leia Organa", "C-3PO", 9)

#mostrar grafo
grafo_star_wars.show_graph()

#C-
mst = grafo_star_wars.kruskal_mst()
print("B.1- Arbol de expansion Minimo:", mst)
print()
print("B.2- ¿El arbol de expansion minimo contiene a Yoda?", grafo_star_wars.contains_yoda_in_mst())
print()

#D-
max_peso, personajes = grafo_star_wars.max_episodes_shared()
print(f"C- El numero maximo de episodios compartidos es {max_peso} entre {personajes[0]} y {personajes[1]}")