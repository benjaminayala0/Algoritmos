superheroes = [
    {
        "nombre": "Linterna Verde",
        "anio_aparicion": 1940,
        "casa_comic": "DC",
        "biografia": "El Linterna Verde original es Alan Scott, pero el más conocido es Hal Jordan, quien es miembro de los Green Lantern Corps."
    },
    {
        "nombre": "Doctor Strange",
        "anio_aparicion": 1963,
        "casa_comic": "DC",
        "biografia": "Hechicero supremo del universo Marvel, maestro de las artes místicas y protector de la realidad."
    },
    {
        "nombre": "Superman",
        "anio_aparicion": 1938,
        "casa_comic": "DC",
        "biografia": "Superman es uno de los superhéroes más icónicos del universo de DC Comics."
    },
    {
        "nombre": "Wolverine",
        "anio_aparicion": 1974,
        "casa_comic": "Marvel",
        "biografia": "Mutante con garras retráctiles y habilidades regenerativas, miembro de los X-Men."
    },
    {
        "nombre": "Spider-Man",
        "anio_aparicion": 1962,
        "casa_comic": "Marvel",
        "biografia": "Spider-Man, también conocido como Peter Parker, es un superhéroe de Marvel Comics."
    }, 
    {
        "nombre": "Mujer Maravilla",
        "anio_aparicion": 1941,
        "casa_comic": "DC",
        "biografia": "Princesa amazona y una de las principales defensoras de la justicia y la igualdad en el Universo DC."
    },
    {
        "nombre": "Capitana Marvel",
        "anio_aparicion": 1968,
        "casa_comic": "Marvel",
        "biografia": "Heroína cósmica con poderes de vuelo, fuerza sobrehumana y energía cósmica."
    },
    {
        "nombre": "Iron Man",
        "anio_aparicion": 1963,
        "casa_comic": "Marvel",
        "biografia": "Tony Stark, genio multimillonario y superhéroe con una armadura tecnológica de alta tecnología."
    },
    {
        "nombre": "Batman",
        "anio_aparicion": 1939,
        "casa_comic": "DC",
        "biografia": "El Caballero Oscuro, detective y luchador experto que protege Gotham City con su traje especializado."
    },
    {
        "nombre": "Flash",
        "anio_aparicion": 1940,
        "casa_comic": "DC",
        "biografia": "El superhéroe más rápido del universo DC, capaz de moverse a velocidades increíbles."
    },
    {
        "nombre": "Star-Lord",
        "anio_aparicion": 1976,
        "casa_comic": "Marvel",
        "biografia": "Líder de los Guardianes de la Galaxia, un aventurero espacial y maestro de las tácticas."
    }
]

#A-
def eliminar_superheroe(superheroes, nombre):
    for i, heroe in enumerate(superheroes):
        if heroe["nombre"] == nombre:
            del superheroes[i]
            print(f"Se ha eliminado a {nombre} de la lista")
            return
    print(f"{nombre} no se encontro en la lista")
eliminar_superheroe(superheroes, "Linterna Verde")

def imprimir_superheroes(superheroes):
    for heroe in superheroes:
        print("Nombre:", heroe["nombre"])
        print("Año de Aparicion:", heroe["anio_aparicion"])
        print("Casa de Comic:", heroe["casa_comic"])
        print("Biografia:", heroe["biografia"])
        print()

print("A-")
print("Lista actualizada sin Linterna Verde :")
imprimir_superheroes(superheroes)

#B-
def mostrar_anio_aparicion(superheroes, nombre):
    for heroe in superheroes:
        if heroe["nombre"] == nombre:
            print(f"Año de aparicion de {nombre}: {heroe['anio_aparicion']}")
            return
    print(f"{nombre} no se encontro en la lista")

print ("B-")
print("año de aparicion de Wolverine :")
mostrar_anio_aparicion(superheroes, "Wolverine")

#C-
def cambiar_casa_comic(superheroes, nombre, nueva_casa):
    for heroe in superheroes:
        if heroe["nombre"] == nombre:
            heroe["casa_comic"] = nueva_casa
            print("C-")
            print(f"Se ha cambiado la casa de {nombre} a {nueva_casa}")
            return
    print(f"{nombre} no se encontro en la lista")
cambiar_casa_comic(superheroes, "Doctor Strange", "Marvel")
print("La nueva casa de Doctor Strange es: ")
imprimir_superheroes(superheroes)

#D-
def superheroe_con_traje_o_armadura(superheroes):
    for heroe in superheroes:
        if "traje" in heroe["biografia"].lower() or "armadura" in heroe["biografia"].lower():
            print(heroe["nombre"])

print("D-")
print("Superheroes con 'traje' o 'armadura' en su biografia :")
superheroe_con_traje_o_armadura(superheroes)

#E-
def superheroes_anteriores_1963(superheroes):
    for heroe in superheroes:
        if heroe["anio_aparicion"] < 1963:
            print(f"Nombre: {heroe['nombre']}, Casa de Comic: {heroe['casa_comic']}")

print("E-")
print("Superheroes cuya fecha de aparicion es antes de 1963 :")
superheroes_anteriores_1963(superheroes)

#F-
def casa_superheroes(superheroes, nombres):
    for heroe in superheroes:
        if heroe["nombre"] in nombres:
            print(f"{heroe['nombre']} pertenece a la casa de comic: {heroe['casa_comic']}")

nombres_superheroes = ["Capitana Marvel", "Mujer Maravilla"]

print("F-")
print("Mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla :")
casa_superheroes(superheroes, nombres_superheroes)

#G-
def info_superheroes(superheroes, nombres):
    for heroe in superheroes:
        if heroe["nombre"] in nombres:
            print(f"Informacion de {heroe['nombre']} :")
            for clave, valor in heroe.items():
                print(f"{clave.capitalize()}: {valor}")
            print()

nombres_superheroes = ["Flash", "Star-Lord"]

print("G-")
print("Informacion de Flash y Star-Lord :")
info_superheroes(superheroes, nombres_superheroes)

#H-
def listar_superheroes(superheroes, letras):
    for heroe in superheroes:
        if heroe["nombre"][0].upper() in letras:
            print(heroe["nombre"])
letras = ["B", "M", "S"]

print("H-")
print("Superheroes que empiezan con B-M-S :")
listar_superheroes(superheroes, letras)

#I-
def contar_superheroes_por_casa(superheroes):
    conteo = {}
    for heroe in superheroes:
        casa = heroe["casa_comic"]
        if casa in conteo:
            conteo[casa] += 1
        else:
            conteo[casa] = 1
    return conteo

print("I-")
print("superheroes que hay en cada casa  de comics :")
conteo_superheroes = contar_superheroes_por_casa(superheroes)
for casa, cantidad in conteo_superheroes.items():
    print(f"{casa}: {cantidad}")