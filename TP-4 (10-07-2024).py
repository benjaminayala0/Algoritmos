class Pokemon:
    def __init__(self, nombre, tipos, numero, nivel):
        self.nombre = nombre
        self.tipos = tipos  
        self.numero = numero
        self.nivel = nivel

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if value not in self.table[index]:
            self.table[index].append(value)

    def get(self, key):
        index = self.hash_function(key)
        return self.table[index]
def hash_por_tipo(pokemon): #hash para pokemon
    return pokemon.tipos
def hash_por_ultimo_digito(pokemon):
    return pokemon.numero % 10
def hash_por_nivel(pokemon):
    return pokemon.nivel // 10

#tabla hash 
size = 5  
tabla_hash_tipo = HashTable(size)
tabla_hash_digito = HashTable(size)
tabla_hash_nivel = HashTable(size)

#agregar un Pokemon en las tres tablas hash:
def insertar_pokemon(pokemon):
    #tabla hash por tipo
    tipos = hash_por_tipo(pokemon)
    for tipo in tipos:
        tabla_hash_tipo.insert(tipo, pokemon)
    #tabla hash por ultimo digito del numero
    key_digito = hash_por_ultimo_digito(pokemon)
    tabla_hash_digito.insert(key_digito, pokemon)
    #tabla hash por nivel
    key_nivel = hash_por_nivel(pokemon)
    tabla_hash_nivel.insert(key_nivel, pokemon)

#cargar un nuevo Pokemon 
def cargar_pokemon(nombre, tipos, numero, nivel):
    if isinstance(tipos, str):
        tipos = [tipos]  # convertir a lista si solo se proporciona un tipo
    pokemon = Pokemon(nombre, tipos, numero, nivel)
    insertar_pokemon(pokemon)

#E-
def pokemon_por_ultimos_digitos(tabla_hash, digitos):
    resultado = []
    for digito in digitos:
        pokemons = tabla_hash.get(digito)
        resultado.extend(pokemons)
    return list(set(resultado))

#f-
def pokemon_por_multiplos_de_nivel(tabla_hash, multiplos):
    resultado = []
    for bucket in tabla_hash.table:
        for pokemon in bucket:
            if any(pokemon.nivel % multiplo == 0 for multiplo in multiplos):
                resultado.append(pokemon)
    return list(set(resultado))

#G-
def pokemon_por_tipos(tabla_hash, tipos_deseados):
    resultado = []
    for tipo in tipos_deseados:
        pokemons = tabla_hash.get(tipo)
        resultado.extend(pokemons)
    return list(set(resultado))

#uso
cargar_pokemon("Pikachu", "Electrico", 25, 15)
cargar_pokemon("Charmander", "Fuego", 4, 10)
cargar_pokemon("Squirtle", "Agua", 7, 12)  # ORDEN PARA CARGAR POKEMON: nombre-elemento-numero de pokemon-nivel
cargar_pokemon("Bulbasaur", ["Planta", "Veneno"], 1, 5)
cargar_pokemon("Magneton", ["Electrico", "Acero"], 82, 22)
cargar_pokemon("Lapras", ["Agua", "Hielo"], 131, 30)

#datos de las tablas hash
def mostrar_tabla_hash(tabla_hash):
    for index, bucket in enumerate(tabla_hash.table):
        print(f"indice {index}: {[p.nombre for p in bucket]}")

print("A-")
print("Tabla Hash por tipo: ")
mostrar_tabla_hash(tabla_hash_tipo)

print("\nTabla Hash por ultimo Digito del numero: ")
mostrar_tabla_hash(tabla_hash_digito)

print("\nTabla Hash por nivel :")
mostrar_tabla_hash(tabla_hash_nivel)

#Pokemones que terminan en (3, 7 y 9): 
pokemons_especificos = pokemon_por_ultimos_digitos(tabla_hash_digito, [3, 7, 9])
print("B-")
print("\nPokemones que su numero termine en 3, 7 y 9: ")
for pokemon in pokemons_especificos:
    print(f"Nombre: {pokemon.nombre}, Numero: {pokemon.numero}, Tipos: {pokemon.tipos}, Nivel: {pokemon.nivel}")
    
#Pokemones cuyos niveles son multiplos de (2, 5 y 10)
pokemons_multiplos_nivel = pokemon_por_multiplos_de_nivel(tabla_hash_nivel, [2, 5, 10])
print("F-")
print("\nPokemones cuyo multiplo sea 2, 5 y 10: ")
for pokemon in pokemons_multiplos_nivel:
    print(f"Nombre: {pokemon.nombre}, Numero: {pokemon.numero}, Tipos: {pokemon.tipos}, Nivel: {pokemon.nivel}")

pokemons_tipos_deseados = pokemon_por_tipos(tabla_hash_tipo, ["Acero", "Fuego", "Electrico", "Hielo"])
print("G-")
print("\nPokemones de distintos tipos [Acero-Fuego-Electrico-Hielo]:")
for pokemon in pokemons_tipos_deseados:
    print(f"Nombre: {pokemon.nombre}, Numero: {pokemon.numero}, Tipos: {pokemon.tipos}, Nivel: {pokemon.nivel}")