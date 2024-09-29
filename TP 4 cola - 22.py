class Queue:
    def __init__(self):
        self.__elements = []

    def arrive(self, element):
        self.__elements.append(element)

    def attention(self):
        if len(self.__elements) > 0:
            return self.__elements.pop(0)
        else:
            return None
    
    def size(self):
        return len(self.__elements)

    def on_front(self):
        if len(self.__elements) > 0:
            return self.__elements[0]
        else:
            return None
    
    def move_to_end(self):
        element = self.attention()
        if element is not None:
            self.arrive(element)

cola_personajes = Queue()
cola_personajes.arrive({"nombre_personaje": "Tony Stark", "superheroe": "Iron Man", "genero": "M"})
cola_personajes.arrive({"nombre_personaje": "Steve Rogers", "superheroe": "Capitán América", "genero": "M"})
cola_personajes.arrive({"nombre_personaje": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"})
cola_personajes.arrive({"nombre_personaje": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"})
cola_personajes.arrive({"nombre_personaje": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"})
cola_personajes.arrive({"nombre_personaje": "Sam Wilson", "superheroe": "Falcon", "genero": "M"})

def obtener_personaje_capitana_marvel(cola):
    for _ in range(cola.size()):
        personaje = cola.attention()
        if personaje["superheroe"] == "Capitana Marvel":
            return personaje["nombre_personaje"]
        cola.arrive(personaje)  #Regresa a la cola si no es, el que buscamos
    return None

def superheroinas(cola):
    femeninos = []
    for _ in range(cola.size()):
        personaje = cola.attention()
        if personaje["genero"] == "F":
            femeninos.append(personaje["superheroe"])
        cola.arrive(personaje)  #regresa a la cola
    return femeninos

def personajes_masculinos(cola):
    masculinos = []
    for _ in range(cola.size()):
        personaje = cola.attention()
        if personaje["genero"] == "M":
            masculinos.append(personaje["nombre_personaje"])
        cola.arrive(personaje)  #vuelve a cola
    return masculinos

def obtener_superheroe_scott_lang(cola):
    for _ in range(cola.size()):
        personaje = cola.attention()
        if personaje["nombre_personaje"] == "Scott Lang":
            return personaje["superheroe"]
        cola.arrive(personaje)  #vuelve a cola
    return None

def personajes_con_s(cola):
    personajes_s = []
    for _ in range(cola.size()):
        personaje = cola.attention()
        if personaje["nombre_personaje"].startswith("S") or personaje["superheroe"].startswith("S"):
            personajes_s.append(personaje)
        cola.arrive(personaje)  #vuelve a cola
    return personajes_s

def encontrar_carol_danvers(cola):
    for _ in range(cola.size()):
        personaje = cola.attention()
        if personaje["nombre_personaje"] == "Carol Danvers" :
            return personaje["superheroe"]
        cola.arrive(personaje)  #vuelve a cola
    return None

#clonar la cola (sin modificar la original)
def clonar_cola(cola):
    clon = Queue()
    for _ in range(cola.size()):
        personaje = cola.attention()
        clon.arrive(personaje)  #se clona el personaje en la nueva cola
        cola.arrive(personaje)  #Regresa el personaje a la cola original
    return clon

#Uso : 
print("A- El nombre del personaje de Capitana Marvel es:", obtener_personaje_capitana_marvel(clonar_cola(cola_personajes)))
print("B- Superheroes femeninos:", superheroinas(clonar_cola(cola_personajes)))
print("C- Personajes masculinos:", personajes_masculinos(clonar_cola(cola_personajes)))
print("D- El superheroe de Scott Lang es:", obtener_superheroe_scott_lang(clonar_cola(cola_personajes)))
print("E- Personajes o superheroes cuyos nombres comienzan con 'S':", personajes_con_s(clonar_cola(cola_personajes)))
print("F- Carol Danvers esta en la cola y su superheroe es:", encontrar_carol_danvers(clonar_cola(cola_personajes)))