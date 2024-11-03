from collections import deque
import heapq

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def arrive(self, item):
        self.queue.append(item)
    
    def attention(self):
        return self.queue.popleft() if self.queue else None
    
    def size(self):
        return len(self.queue)

class HeapMin:
    def __init__(self):
        self.elements = []
    
    def arrive(self, item):
        heapq.heappush(self.elements, item)
    
    def attention(self):
        return heapq.heappop(self.elements) if self.elements else None
    
    def size(self):
        return len(self.elements)

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        return self.stack.pop() if self.stack else None
    
    def size(self):
        return len(self.stack)

class Graph:
    def __init__(self, dirigido=False):
        self.elements = []
        self.dirigido = dirigido

    def show_graph(self):
        print("\nGrafo:")
        for nodo in self.elements:
            print(f"Vertice: {nodo['value']}")
            for arista in nodo['aristas']:
                print(f"    {arista['value']} (peso: {arista['peso']} metros)")
        print()

    def search(self, value):
        for index, element in enumerate(self.elements):
            if element['value'] == value:
                return index
        return None

    def insert_vertice(self, value):
        if self.search(value) is None:
            self.elements.append({'value': value, 'aristas': [], 'visitado': False})

    def insert_arista(self, origen, destino, peso):
        pos_origen = self.search(origen)
        pos_destino = self.search(destino)
        if pos_origen is not None and pos_destino is not None:
            self.elements[pos_origen]['aristas'].append({'value': destino, 'peso': peso})
            if not self.dirigido:
                self.elements[pos_destino]['aristas'].append({'value': origen, 'peso': peso})

    def mark_as_not_visited(self):
        for nodo in self.elements:
            nodo['visitado'] = False

    def dijkstra(self, origen):
        from math import inf
        no_visitados = HeapMin()
        caminos = {nodo['value']: (inf, None) for nodo in self.elements} 
        caminos[origen] = (0, None)  
        no_visitados.arrive((0, origen))  

        while no_visitados.size() > 0:
            distancia_actual, nodo_actual = no_visitados.attention()

            pos_actual = self.search(nodo_actual)
            if pos_actual is not None:
                for adyacente in self.elements[pos_actual]['aristas']:
                    distancia_nueva = distancia_actual + adyacente['peso']
                    if distancia_nueva < caminos[adyacente['value']][0]:
                        caminos[adyacente['value']] = (distancia_nueva, nodo_actual)
                        no_visitados.arrive((distancia_nueva, adyacente['value']))

        return caminos
    def kruskal(self):
        def find(parent, vertex):
            if parent[vertex] == vertex:
                return vertex
            return find(parent, parent[vertex])

        def union(parent, rank, v1, v2):
            root1 = find(parent, v1)
            root2 = find(parent, v2)
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1

        edges = []
        for nodo in self.elements:
            for arista in nodo['aristas']:
                edges.append((arista['peso'], nodo['value'], arista['value']))
        edges = sorted(edges, key=lambda x: x[0])

        parent = {nodo['value']: nodo['value'] for nodo in self.elements}
        rank = {nodo['value']: 0 for nodo in self.elements}
        mst = []

        for peso, origen, destino in edges:
            root_origen = find(parent, origen)
            root_destino = find(parent, destino)
            if root_origen != root_destino:
                mst.append((origen, destino, peso))
                union(parent, rank, root_origen, root_destino)

        return mst


#grafo con los ambientes de la casa
casa = Graph(dirigido=False)
ambientes = ['cocina', 'comedor', 'cochera', 'quincho', 'baño 1', 'baño 2', 
             'habitacion 1', 'habitacion 2', 'sala de estar', 'terraza', 'patio']
for ambiente in ambientes:
    casa.insert_vertice(ambiente)

#conexiones con pesos (en metros)
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

#A.1
caminos = casa.dijkstra('cocina')
print("A.1-Caminos mas cortos desde cocina a los demas ambientes:")
for destino, (distancia, previo) in caminos.items():
    print(f"{destino}: distancia {distancia} metros, previo {previo}")

#A.2
mst = casa.kruskal()
print("A.2-\nArbol de expansion minima para conectar todos los ambientes:")
for origen, destino, peso in mst:
    print(f"{origen} - {destino} (peso: {peso} metros)")

#B
print("\nB y C-")
casa.show_graph()
mst = casa.kruskal()

#C.2
metros_de_cable = sum(peso for _, _, peso in mst)
print("C.2- \nCantidad total de metros de cable necesarios para conectar todos los ambientes:")
print(f"{metros_de_cable} metros")

#D
caminos = casa.dijkstra('habitacion 1')
distancia, previo = caminos['sala de estar']

print("D- \nCantidad de metros de cable de red necesarios para conectar el router con el Smart TV:")
print(f"{distancia} metros")
