entrenadores = [
    {
        "nombre": "Ash Ketchum",
        "torneos_ganados": 7,
        "batallas_perdidas": 50,
        "batallas_ganadas": 120,
        "equipo": [
            {
                "nombre": "Pikachu",
                "nivel": 35,
                "tipo": "Eléctrico",
                "subtipo": None
            },
            {
                "nombre": "Charizard",
                "nivel": 40,
                "tipo": "Fuego",
                "subtipo": "Volador"
            },
            {
                "nombre": "Bulbasaur",
                "nivel": 30,
                "tipo": "Planta",
                "subtipo": "Veneno"
            }
        ]
    },
    {
        "nombre": "Goh",
        "torneos_ganados": 2,
        "batallas_perdidas": 10,
        "batallas_ganadas": 40,
        "equipo": [
            {
                "nombre": "Scorbunny",
                "nivel": 25,
                "tipo": "Fuego",
                "subtipo": None
            },
            {
                "nombre": "Caterpie",
                "nivel": 15,
                "tipo": "Bicho",
                "subtipo": None
            },
            {
                "nombre": "Grookey",
                "nivel": 20,
                "tipo": "Planta",
                "subtipo": None
            }
        ]
    },
    {
        "nombre": "Leon",
        "torneos_ganados": 10,
        "batallas_perdidas": 5,
        "batallas_ganadas": 100,
        "equipo": [
            {
                "nombre": "Charizard",
                "nivel": 50,
                "tipo": "Fuego",
                "subtipo": "Volador"
            },
            {
                "nombre": "Dragapult",
                "nivel": 55,
                "tipo": "Dragón",
                "subtipo": "Fantasma"
            },
            {
                "nombre": "Aegislash",
                "nivel": 48,
                "tipo": "Acero",
                "subtipo": "Fantasma"
            }
        ]
    },
    {
        "nombre": "Chloe",
        "torneos_ganados": 1,
        "batallas_perdidas": 8,
        "batallas_ganadas": 30,
        "equipo": [
            {
                "nombre": "Yamper",
                "nivel": 22,
                "tipo": "Eléctrico",
                "subtipo": None
            },
            {
                "nombre": "Eevee",
                "nivel": 18,
                "tipo": "Normal",
                "subtipo": None
            },
            {
                "nombre": "Bunnelby",
                "nivel": 16,
                "tipo": "Normal",
                "subtipo": "Tierra"
            }
        ]
    },
    {
        "nombre": "Raihan",
        "torneos_ganados": 4,
        "batallas_perdidas": 15,
        "batallas_ganadas": 60,
        "equipo": [
            {
                "nombre": "Duraludon",
                "nivel": 45,
                "tipo": "Acero",
                "subtipo": "Dragón"
            },
            {
                "nombre": "Flygon",
                "nivel": 42,
                "tipo": "Tierra",
                "subtipo": "Dragón"
            },
            {
                "nombre": "Gigalith",
                "nivel": 40,
                "tipo": "Roca",
                "subtipo": None
            }
        ]
    }
]

# A-
def cantidad_pokemons(entrenadores, nombre_entrenador):
    for entrenador in entrenadores:
        if entrenador["nombre"] == nombre_entrenador:
            return len(entrenador["equipo"])
    return 0

print("A-")
print("Cantidad de Pokemones de Ash Ketchum: ", cantidad_pokemons(entrenadores, "Ash Ketchum"))

# B-
def entrenadores_mas_de_tres_torneos(entrenadores):
    for entrenador in entrenadores:
        if entrenador["torneos_ganados"] > 3:
            print(entrenador["nombre"])
print("B-")
print("Entrenadores con mas de tres torneos ganados: ")
entrenadores_mas_de_tres_torneos(entrenadores)

# C-
def pokemon_mayor_nivel(entrenadores):
    max_torneos = 0
    entrenador_con_mas_torneos = None
    
    for entrenador in entrenadores:
        if entrenador["torneos_ganados"] > max_torneos:
            max_torneos = entrenador["torneos_ganados"]
            entrenador_con_mas_torneos = entrenador
    
    if entrenador_con_mas_torneos:
        pokemons = entrenador_con_mas_torneos["equipo"]
        pokemon_mayor_nivel = max(pokemons, key=lambda p: p["nivel"])
        return pokemon_mayor_nivel
    
    return None

print("C-")
print("Pokemon de mayor nivel del entrenador con mas torneos ganados: ", pokemon_mayor_nivel(entrenadores))

# D-
def entrenador_y_pokemons(entrenadores, nombre_entrenador):
    for entrenador in entrenadores:
        if entrenador["nombre"] == nombre_entrenador:
            print("Nombre:", entrenador["nombre"])
            print("Torneos ganados:", entrenador["torneos_ganados"])
            print("Batallas perdidas:", entrenador["batallas_perdidas"])
            print("Batallas ganadas:", entrenador["batallas_ganadas"])
            print("Pokemones:")
            for pokemon in entrenador["equipo"]:
                print(f"  - Nombre: {pokemon['nombre']}, Nivel: {pokemon['nivel']}, Tipo: {pokemon['tipo']}, Subtipo: {pokemon['subtipo']}")
            return
            
print("D-")
print("Datos de Ash Ketchum y sus Pokemones: ")
entrenador_y_pokemons(entrenadores, "Ash Ketchum")

# E-
def entrenadores_mayor_porcentaje_victorias(entrenadores):
    for entrenador in entrenadores:
        batallas_totales = entrenador["batallas_perdidas"] + entrenador["batallas_ganadas"]
        if batallas_totales > 0:
            porcentaje_victorias = (entrenador["batallas_ganadas"] / batallas_totales) * 100
            if porcentaje_victorias > 79:
                print(entrenador["nombre"])

print("E-")
print("Entrenadores con mas del 79% de batallas ganadas: ")
entrenadores_mayor_porcentaje_victorias(entrenadores)

# F - Entrenadores con Pokemones de tipo Fuego/Planta o Agua/Volador
def entrenadores_con_pokemons_especiales(entrenadores):
    for entrenador in entrenadores:
        tiene_fuego_planta = False
        tiene_agua_volador = False
        for pokemon in entrenador["equipo"]:
            if (pokemon["tipo"] == "Fuego" or pokemon["tipo"] == "Planta"):
                tiene_fuego_planta = True
            if (pokemon["tipo"] == "Agua" or pokemon["tipo"] == "Volador"):
                tiene_agua_volador = True
        if tiene_fuego_planta or tiene_agua_volador:
            print(entrenador["nombre"])

print("F-")
print("Entrenadores con Pokemones de tipo Fuego/Planta o Agua/Volador: ")
entrenadores_con_pokemons_especiales(entrenadores)


# G-
def promedio_nivel_pokemons(entrenadores, nombre_entrenador):
    for entrenador in entrenadores:
        if entrenador["nombre"] == nombre_entrenador:
            total_nivel = sum([pokemon["nivel"] for pokemon in entrenador["equipo"]])
            cantidad_pokemons = len(entrenador["equipo"])
            if cantidad_pokemons > 0:
                return total_nivel / cantidad_pokemons
    return 0

print("G-")
print("Promedio de nivel de los Pokemones de Ash Ketchum:", promedio_nivel_pokemons(entrenadores, "Ash Ketchum"))

# H-
def entrenadores_con_pokemon(entrenadores, nombre_pokemon):
    print("H-")
    count = 0
    for entrenador in entrenadores:
        for pokemon in entrenador["equipo"]:
            if pokemon["nombre"] == nombre_pokemon:
                count += 1
                break
    return count

print("Numero de entrenadores con Pikachu:", entrenadores_con_pokemon(entrenadores, "Pikachu"))

# I - Entrenadores con Pokemones repetidos
def entrenadores_con_pokemons_repetidos(entrenadores):
    for entrenador in entrenadores:
        nombres_pokemons = [pokemon["nombre"] for pokemon in entrenador["equipo"]]
        if len(nombres_pokemons) != len(set(nombres_pokemons)):
            print(entrenador["nombre"])

print("I-")
print("Entrenadores con Pokemones repetidos: ")
entrenadores_con_pokemons_repetidos(entrenadores)
# J-
def entrenadores_con_pokemons_especificos(entrenadores):
    pokemons_buscados = {"Tyrantrum", "Terrakion", "Wingull"}
    for entrenador in entrenadores:
        for pokemon in entrenador["equipo"]:
            if pokemon["nombre"] in pokemons_buscados:
                print(entrenador["nombre"])
                break
print("J-")
print("Entrenadores con Tyrantrum, Terrakion o Wingull:")
entrenadores_con_pokemons_especificos(entrenadores)

# K-
def entrenador_tiene_pokemon(entrenadores, nombre_entrenador, nombre_pokemon):
    for entrenador in entrenadores:
        if entrenador["nombre"] == nombre_entrenador:
            for pokemon in entrenador["equipo"]:
                if pokemon["nombre"] == nombre_pokemon:
                    print(f"El entrenador {nombre_entrenador} tiene al Pokémon {nombre_pokemon}.")
                    print("Datos del entrenador:")
                    print(f"Nombre: {entrenador['nombre']}, Torneos ganados: {entrenador['torneos_ganados']}, Batallas perdidas: {entrenador['batallas_perdidas']}, Batallas ganadas: {entrenador['batallas_ganadas']}")
                    print("Datos del Pokémon:")
                    print(f"Nombre: {pokemon['nombre']}, Nivel: {pokemon['nivel']}, Tipo: {pokemon['tipo']}, Subtipo: {pokemon['subtipo']}")
                    return
    print(f"El entrenador {nombre_entrenador} no tiene al Pokemon {nombre_pokemon}")

print("K-")
entrenador_tiene_pokemon(entrenadores, "Ash Ketchum", "Pikachu")
