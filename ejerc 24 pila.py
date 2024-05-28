class Stack:
    def __init__(self):
        self.__elements = []

    def push(self, element):
        self.__elements.append(element)

    def pop(self):
        if self.__elements:
            return self.__elements.pop()
        return None

    def on_top(self):
        if self.__elements:
            return self.__elements[-1]
        return None

    def size(self):
        return len(self.__elements)

    def is_empty(self):
        return len(self.__elements) == 0

    def __repr__(self):
        return repr(self.__elements)

# Crear la pila de personajes del MCU
pila_personajes = Stack()
pila_personajes.push(("Viuda Negra", 6))
pila_personajes.push(("Groot", 5))
pila_personajes.push(("Thor", 7))
pila_personajes.push(("Doctor Strange", 3))
pila_personajes.push(("Capitan America", 6))
pila_personajes.push(("Rocket Raccoon", 4))
pila_personajes.push(("Black Panther", 3))
pila_personajes.push(("Spider-Man", 5))

def copiar_pila(pila):
    copia = Stack()
    elementos_temporales = []
    while not pila.is_empty():
        elementos_temporales.append(pila.pop())
    for elemento in reversed(elementos_temporales):
        pila.push(elemento)
        copia.push(elemento)
    return copia

def posicion_rocket_groot(pila):
    "Posicion de Rocket Raccoon o Groot en la pila"
    copia_pila = copiar_pila(pila)
    posicion = 1
    encontrado = False

    while copia_pila.size() > 0 and not encontrado:
        personaje = copia_pila.pop()
        if personaje[0] == "Rocket Raccoon" or personaje[0] == "Groot":
            encontrado = True
        else:
            posicion += 1

    if encontrado:
        print(f"Rocket Raccoon y Groot estan en la posicion {posicion} de la pila")
    else:
        print("Rocket Raccoon y Groot no estan en la pila")

def personajes_mas_de_5_peliculas(pila):
    "Personajes que han participado en mas de 5 películas"
    copia_pila = copiar_pila(pila)
    print("Personajes que participaron en mas de 5 películas de la saga:")
    while copia_pila.size() > 0:
        personaje = copia_pila.pop()
        if personaje[1] > 5:
            print(f"{personaje[0]}: {personaje[1]} películas")

def peliculas_viuda_negra(pila):
    "cantidad de películas en las que participo Viuda Negra"
    copia_pila = copiar_pila(pila)
    cantidad_peliculas = 0
    encontrado = False

    while copia_pila.size() > 0 and not encontrado:
        personaje = copia_pila.pop()
        if personaje[0] == "Viuda Negra":
            cantidad_peliculas = personaje[1]
            encontrado = True

    if encontrado:
        print(f"la viuda negra (black widow) participo en {cantidad_peliculas} peliculas")
    else:
        print("Viuda Negra no se encuentra en la pila")

def mostrar_personajes_c_d_g(pila):
    "Personajes cuyos nombres empiezan con C, D o G."
    copia_pila = copiar_pila(pila)
    print("Personajes cuyos nombres empiezan con C, D o G:")
    while copia_pila.size() > 0:
        personaje = copia_pila.pop()
        if personaje[0][0] in ['C', 'D', 'G']:
            print(personaje[0])

#mostrar respuestas
posicion_rocket_groot(pila_personajes) #A
personajes_mas_de_5_peliculas(pila_personajes) #B
peliculas_viuda_negra(pila_personajes) #C 
mostrar_personajes_c_d_g(pila_personajes) #D
