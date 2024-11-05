from arbol_avl import BinaryTree
from cola import Queue

arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()

pokemones = [
    {"nombre": "Pikachu", "numero": 25, "tipo": "Electric"},
    {"nombre": "Charmander", "numero": 4, "tipo": "Fire"},
    {"nombre": "Bulbasaur", "numero": 1, "tipo": "Grass/Poison"},
    {"nombre": "Squirtle", "numero": 7, "tipo": "steel"},
    {"nombre": "Jolteon", "numero": 135, "tipo": "Electric"},
    {"nombre": "Lycanroc", "numero": 745, "tipo": "Rock"},
    {"nombre": "Tyrantrum", "numero": 697, "tipo": "Rock/Dragon"},
]

for pokemon in pokemones:
    arbol_nombre.insert_node(pokemon['nombre'], other_value=pokemon)
    arbol_numero.insert_node(pokemon['numero'], other_value=pokemon)
    tipos = pokemon['tipo'].split('/')
    for tipo in tipos:
        nodo_tipo = arbol_tipo.search(tipo)
        if nodo_tipo:
            if isinstance(nodo_tipo.other_value, list):
                nodo_tipo.other_value.append(pokemon)
            else:
                nodo_tipo.other_value = [nodo_tipo.other_value, pokemon]
        else:
            arbol_tipo.insert_node(tipo, other_value=pokemon)

#mostrar Pokemon en una lista
def mostrar_pokemon_lista(lista):
    for pokemon in lista:
        print(pokemon)

def mostrar_pokemon_por_numero_y_nombre(numero, nombre_proximidad):
    #buscar por numero exacto
    resultado_numero = arbol_numero.search(numero)
    if resultado_numero:
        print(f"\nB- Pokemon encontrado por numero {numero}:")
        print(resultado_numero.other_value)
    else:
        print(f"\nPokemon con numero {numero} no encontrado")

    #buscar por nombre por proximidad
    resultados_proximidad = arbol_nombre.proximity_search(nombre_proximidad)
    if resultados_proximidad:
        print(f"\nB.1- Pokemon(s) encontrado(s) por proximidad en nombre '{nombre_proximidad}':")
        for res in resultados_proximidad:
            print(res)
    else:
        print(f"\nNo se encontraron Pokemones cuyo nombre contenga '{nombre_proximidad}'")

def mostrar_nombres_por_tipo(tipo):
    resultados_tipo = arbol_tipo.search_by_type(tipo)
    if resultados_tipo:
        print(f"\nC- Pokemon(s) de tipo '{tipo}':")
        for res in resultados_tipo:
            print(res["nombre"])
    else:
        print(f"\nNo se encontraron Pokemones de tipo '{tipo}'")

def realizar_listados():
    #listado en orden ascendente por numero
    print("\nD.1- Pokemon en orden ascendente por numero:")
    pokemons_orden_numero = arbol_numero.inorden()
    mostrar_pokemon_lista(pokemons_orden_numero)

    #listado en orden ascendente por nombre
    print("\nD.2- Pokemon en orden ascendente por nombre:")
    pokemons_orden_nombre = arbol_nombre.inorden()
    mostrar_pokemon_lista(pokemons_orden_nombre)

    #listado por nivel por nombre
    print("\nD.3- Pokemon listados por nivel de profundidad en el arbol de nombres:")
    pokemons_por_nivel = arbol_nombre.by_level()
    for nivel, nombre in pokemons_por_nivel:
        print(f"Nivel {nivel}: {nombre}")

def mostrar_pokemones_especificos(nombres):
    print("\nE- Datos de Pokemon especificos:")
    for nombre in nombres:
        pokemon_encontrado = arbol_nombre.search(nombre)
        if pokemon_encontrado:
            print(pokemon_encontrado.other_value)
        else:
            print(f"Pokemon {nombre} no encontrado")
        
def contar_pokemon_por_tipos():
    tipos_a_contar = ["Electric", "Steel"]
    contador = {} 
    for tipo in tipos_a_contar:
        resultados_tipo = arbol_tipo.search_by_type(tipo)
        contador[tipo] = len(resultados_tipo)
    print()
    print(f"F- Cantidad de Pokemon de tipo electrico: {contador.get('Electric', 0)}")
    print(f"Cantidad de Pokemon de tipo acero: {contador.get('Steel', 0)}")

#B-
mostrar_pokemon_por_numero_y_nombre(7, "bul")#ej:numero 7 y proximidad "bul"

#C-
tipos_a_buscar = ["Water", "Fire", "Rock", "Electric"]
for tipo in tipos_a_buscar:
    mostrar_nombres_por_tipo(tipo)

#D-
realizar_listados()

#E-
pokemones_especificos = ["Jolteon", "Lycanroc", "Tyrantrum"]
mostrar_pokemones_especificos(pokemones_especificos)

#F-
contar_pokemon_por_tipos()
