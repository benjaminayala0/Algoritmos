class Stack:
    def __init__(self):
        self.__elements = []

    def push(self, element):
        self.__elements.append(element)

    def pop(self):
        if len(self.__elements) > 0:
            return self.__elements.pop()
        else:
            return None

    def on_top(self):
        if len(self.__elements) > 0:
            return self.__elements[-1]
        else:
            return None

    def size(self):
        return len(self.__elements)
        
    def get_elements(self):
        return self.__elements.copy()

#Pilas 
pila_episodio_v = Stack()
pila_episodio_vii = Stack()

#nombres de personajes
personajes_episodio_v = ["luke skywalker", "boba fett", "han solo", "darth vader"]
personajes_episodio_vii = ["Luke Skywalker", "Rey", "Finn", "Kylo Ren"]

#pila del episodio V
for personaje in personajes_episodio_v:
    pila_episodio_v.push(personaje.lower())  #minusculas para comparación

#pila del episodio VII
for personaje in personajes_episodio_vii:
    pila_episodio_vii.push(personaje.lower())  #minusculas para comparacion

#interseccion de ambas pilas
def interseccion_pilas(pila1, pila2):
    interseccion = Stack()
    temp1 = Stack()
    temp2 = Stack()
    elementos_pila1 = set(pila1.get_elements())

    #elementos de la segunda pila temporalmente
    while pila2.size() > 0:
        personaje = pila2.pop()
        if personaje in elementos_pila1:
            interseccion.push(personaje)
        temp2.push(personaje)

    #elementos de la segunda pila
    while temp2.size() > 0:
        pila2.push(temp2.pop())

    #elementos de la primera pila
    while pila1.size() > 0:
        temp1.push(pila1.pop())
    while temp1.size() > 0:
        pila1.push(temp1.pop())

    return interseccion

#interseccion de ambas pilas
personajes_interseccion = interseccion_pilas(pila_episodio_v, pila_episodio_vii)

#Mostrar los personajes que aparecen en ambos episodios
print("Personajes que aparecen en los dos episodios:")
while personajes_interseccion.size() > 0:
    print(personajes_interseccion.pop())
