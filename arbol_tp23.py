from arbol_avl23 import BinaryTree

criaturas = [
    {
        "nombre": "Ceto",
        "derrotado": None
    },
    {
        "nombre": "Tifon",
        "derrotado": "Zeuz"
    },
    {
        "nombre": "Equidna",
        "derrotado": "Argos Panoptes"
    },
    {
        "nombre": "Dino",
        "derrotado": None
    },
    {
        "nombre": "Pefredo",
        "derrotado": None
    },
    {
        "nombre": "Enio",
        "derrotado": None
    },
    {
        "nombre": "Escila",
        "derrotado": None
    },
    {
        "nombre": "Caribdis",
        "derrotado": None
    },
    {
        "nombre": "Euriale",
        "derrotado": None
    },
    {
        "nombre": "Esteno",
        "derrotado": None
    },
    {
        "nombre": "Medusa",
        "derrotado": "Perseo"
    },
    {
        "nombre": "Ladon",
        "derrotado": "Heracles"
    },
    {
        "nombre": "Aguila del Caucaso",
        "derrotado": None
    },
    {
        "nombre": "Quimera",
        "derrotado": "Belerofonte"
    },
    {
        "nombre": "Hidra de Lerna",
        "derrotado": "Heracles"
    },
    {
        "nombre": "Leon de Nemea",
        "derrotado": "Heracles"
    },
    {
        "nombre": "Esfinge",
        "derrotado": "Edipo"
    },
    {
        "nombre": "Dragon de la Colquida",
        "derrotado": None
    },
    {
        "nombre": "Cerbero",
        "derrotado": None
    },
    {
        "nombre": "Cerdo de Cromion",
        "derrotado": "Teseo"
    },
    {
        "nombre": "Ortro",
        "derrotado": "Heracles"
    },
    {
        "nombre": "Toro de Creta",
        "derrotado": "Teseo"
    },
    {
        "nombre": "Jabali de Calidon",
        "derrotado": "Atalanta"
    },
    {
        "nombre": "Carcinos",
        "derrotado": None
    },
    {
        "nombre": "Gerion",
        "derrotado": "Heracles"
    },
    {
        "nombre": "Cloto",
        "derrotado": None
    },
    {
        "nombre": "Laquesis",
        "derrotado": None
    },
    {
        "nombre": "Artropos",
        "derrotado": None
    },
    {
        "nombre": "Minotauro de Creta",
        "derrotado": "Teseo"
    },
    {
        "nombre": "Harpias",
        "derrotado": None
    },
    {
        "nombre": "Argos Panoptes",
        "derrotado": "Hermes"
    },
    {
        "nombre": "Aves de Estinfalo",
        "derrotado": None
    },
    {
        "nombre": "Talos",
        "derrotado": "Medea"
    },
    {
        "nombre": "Sirenas",
        "derrotado": None
    },
    {
        "nombre": "Piton",
        "derrotado": "Apolo"
    },
    {
        "nombre": "Cierva de Cerinea",
        "derrotado": None
    },
    {
        "nombre": "Basilisco",
        "derrotado": None
    },
    {
        "nombre": "Jabali de Erimanto",
        "derrotado": None
    }
]

print()
arbol = BinaryTree()

for criatura in criaturas:
    arbol.insert_node(criatura["nombre"], {"derrotado": criatura["derrotado"]})
    #print(f'{criatura["nombre"]} se inerto correctamente')

print()
# a)
arbol.inorden_con_derrotas()

print()
# b)
info=input ("ingrese la informacion de ceto: ")
info2=input ("ingrese la informacion de Medusa: ")
arbol.cargar_descripcion("Ceto",info)
arbol.cargar_descripcion("Medusa", info2)
#solo cargue 2 pero se puede cargar con todos si cambiamos el nombre, tambien podria cargar todos sin necesidad
#de cambiar el nombre pero tardaria mucho tiempo en escrbir por cada 1 la informacion , asique lo deje con 2

print()
# c)
print("\nMostrar Informacion de Talos")
nodo_talos=arbol.search("Talos")
if nodo_talos:
   print(f'Talos fue derrotado por {nodo_talos.other_value.get('derrotado','Nadie')}')

print()
# d)
arbol.top_heroes()

print()
# e)
arbol.criaturas_derrotadas_por("Heracles")

print()
# f)
arbol.criaturas_sin_derrotar()

print()
#punto g) y h)
arbol.modificarCapturas('Cerbero', 'Heracles')
arbol.modificarCapturas('Toro de Creta', 'Heracles')
arbol.modificarCapturas('Cierva de Cerinea', 'Heracles')
arbol.modificarCapturas('Jabali de Erimanto', 'Heracles')

print()
#punto i)
arbol.proximity_search('Ce')

print()
#punto j)
arbol.eliminarCriaturas('Basilisco')
arbol.eliminarCriaturas('Sirenas')

print()
#punto k)
arbol.modificarCriatura('Aves de Estinfalo','Heracles derroto a varias Aves del Estinfalo')

print()
#punto l)
arbol.modificar_nombre('Ladon', 'Dragon Ladon')

print()
#punto m)
arbol.by_level()
arbol.por_nivel_perso()

print()
#punto n)
arbol.criaturas_capturadas_por_in("Heracles")