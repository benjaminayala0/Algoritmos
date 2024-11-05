from cola import Queue
from heap import HeapMin
from pila import Stack

class Graph:
    def __init__(self, dirigido=False):
        self.adj_list = {}
        self.dirigido = dirigido

    def insert_vertice(self, vertice):
        if vertice not in self.adj_list:
            self.adj_list[vertice] = []

    def insert_arista(self, origen, destino, peso=1):
        self.adj_list[origen].append((destino, peso))
        if not self.dirigido:
            self.adj_list[destino].append((origen, peso))

    def dijkstra(self, inicio):
        distancias = {vertice: float('inf') for vertice in self.adj_list}
        previos = {vertice: None for vertice in self.adj_list}
        distancias[inicio] = 0
        min_heap = HeapMin()

        min_heap.add((0, inicio))

        while len(min_heap.elements) > 0:
            distancia_actual, actual = min_heap.remove()

            for vecino, peso in self.adj_list[actual]:
                distancia = distancia_actual + peso

                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    previos[vecino] = actual
                    min_heap.add((distancia, vecino))

        return {vertice: (distancias[vertice], previos[vertice]) for vertice in self.adj_list}

    def kruskal(self):
        aristas = []
        for origen in self.adj_list:
            for destino, peso in self.adj_list[origen]:
                if (origen, destino, peso) not in aristas and (destino, origen, peso) not in aristas:
                    aristas.append((origen, destino, peso))

        aristas.sort(key=lambda arista: arista[2])

        parent = {}
        rank = {}

        def find(vertice):
            if parent[vertice] != vertice:
                parent[vertice] = find(parent[vertice])
            return parent[vertice]

        def union(vertice1, vertice2):
            root1 = find(vertice1)
            root2 = find(vertice2)

            if root1 != root2:
                if rank[root1] > rank[root2]:
                    parent[root2] = root1
                else:
                    parent[root1] = root2
                    if rank[root1] == rank[root2]:
                        rank[root2] += 1

        for vertice in self.adj_list:
            parent[vertice] = vertice
            rank[vertice] = 0

        mst = []
        for origen, destino, peso in aristas:
            if find(origen) != find(destino):
                union(origen, destino)
                mst.append((origen, destino, peso))

        return mst

    def show_graph(self):
        for vertice, aristas in self.adj_list.items():
            print(f"{vertice}: {aristas}")

# grafo
casa = Graph(dirigido=False)
ambientes = ['cocina', 'comedor', 'cochera', 'quincho', 'baño 1', 'baño 2',
             'habitacion 1', 'habitacion 2', 'sala de estar', 'terraza', 'patio']
for ambiente in ambientes:
    casa.insert_vertice(ambiente)

# conexiones con pesos (en metros)
casa.insert_arista('cocina', 'comedor', 2)
casa.insert_arista('cocina', 'cochera', 5)
casa.insert_arista('cocina', 'terraza', 4)
casa.insert_arista('cocina', 'sala de estar', 3)
casa.insert_arista('cocina', 'patio', 6)

casa.insert_arista('comedor', 'sala de estar', 3)
casa.insert_arista('comedor', 'baño 1', 2)
casa.insert_arista('comedor', 'quincho', 7)
casa.insert_arista('comedor', 'habitacion 1', 5)
casa.insert_arista('comedor', 'habitacion 2', 8)

casa.insert_arista('sala de estar', 'habitacion 1', 4)
casa.insert_arista('sala de estar', 'habitacion 2', 6)
casa.insert_arista('sala de estar', 'terraza', 5)

casa.insert_arista('habitacion 1', 'baño 1', 1)
casa.insert_arista('habitacion 1', 'patio', 7)
casa.insert_arista('habitacion 1', 'quincho', 4)

casa.insert_arista('habitacion 2', 'baño 2', 1)
casa.insert_arista('habitacion 2', 'terraza', 6)
casa.insert_arista('habitacion 2', 'quincho', 5)

casa.insert_arista('terraza', 'patio', 2)
casa.insert_arista('terraza', 'quincho', 3)

casa.insert_arista('quincho', 'patio', 3)
casa.insert_arista('quincho', 'baño 1', 8)
casa.insert_arista('quincho', 'baño 2', 4)

casa.insert_arista('cochera', 'patio', 7)
casa.insert_arista('cochera', 'baño 1', 3)
casa.insert_arista('cochera', 'habitacion 2', 6)

#caminos mas cortos desde cocina a los demas ambientes
caminos = casa.dijkstra('cocina')
print("caminos mas cortos desde cocina a los demas ambientes:")
for destino, (distancia, previo) in caminos.items():
    print(f"{destino}: distancia {distancia} metros, previo {previo}")

#C.1-
mst = casa.kruskal()
print("\nC.1 - Arbol de expansion minima para conectar todos los ambientes:")
for origen, destino, peso in mst:
    print(f"{origen} - {destino} (peso: {peso} metros)")

#B-
print("\nB - Grafo:")
casa.show_graph()

#C.2-
metros_de_cable = sum(peso for _, _, peso in mst)
print("\nC.2 - Cantidad total de metros de cable necesarios:")
print(f"{metros_de_cable} metros")

#D-
caminos = casa.dijkstra('habitacion 1')
distancia, previo = caminos['sala de estar']
print("\nD - Cantidad de metros de cable de red necesarios para conectar habitación 1 con sala de estar:")
print(f"{distancia} metros")
