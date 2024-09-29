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

    def show_queue(self):
        return self.__elements.copy()

#a
def caract_planeta(queue, planets):
    temp_queue = Queue()  
    ver_caract = []

    while queue.size() > 0:
        character = queue.attention()
        nombre, planet = character
        if planet in planets:
            ver_caract.append(character)
        temp_queue.arrive(character)

    while temp_queue.size() > 0:
        queue.arrive(temp_queue.attention())
    
    return ver_caract
#b
def planeta_natal(queue, nombres):
    temp_queue = Queue()
    planeta_info = {}

    while queue.size() > 0:
        character = queue.attention()
        nombre, planets = character
        if nombre in nombres:
            planeta_info[nombre] = planets
        temp_queue.arrive(character)

    while temp_queue.size() > 0:
        queue.arrive(temp_queue.attention())

    return planeta_info

#c
def insert_before_character(queue, new_character, before_name):
    temp_queue = Queue()
    inserted = False

    while queue.size() > 0:
        character = queue.attention()
        nombre, planeta = character

        if nombre == before_name and not inserted:
            temp_queue.arrive(new_character)  # Inserta nuevo personaje
            inserted = True

        temp_queue.arrive(character)

    while temp_queue.size() > 0:
        queue.arrive(temp_queue.attention())

#d
def remove_after_jar_jar(queue):
    temp_queue = Queue()
    skip_next = False  #variable para saltar al personaje despues de Jar Jar Binks

    while queue.size() > 0:
        character = queue.attention()
        nombre, planeta = character

        if skip_next:
            skip_next = False  #saltar el siguiente personaje
        else:
            temp_queue.arrive(character)

        if nombre == "Jar Jar Binks":
            skip_next = True  #marcar para saltar el siguiente personaje

    while temp_queue.size() > 0:
        queue.arrive(temp_queue.attention())

#Uso:
queue = Queue()
queue.arrive(("Luke Skywalker", "Tatooine"))
queue.arrive(("Han Solo", "Corellia"))
queue.arrive(("Leia Organa", "Alderaan"))
queue.arrive(("Ahsoka Tano", "Shili"))
queue.arrive(("Yoda", "Dagobah"))
queue.arrive(("Wicket", "Endor"))
queue.arrive(("Jar Jar Binks", "Naboo"))
queue.arrive(("R2-D2", "Tatooine"))

planets = ["Alderaan", "Endor", "Tatooine"]
ver_caract = caract_planeta(queue, planets)
print("A- Personajes de los planetas Alderaan, Endor, Tatooine:", ver_caract)


nombres = ["Luke Skywalker", "Han Solo"]
caract_de_planetas = planeta_natal(queue, nombres)
print("B- Planetas de:", caract_de_planetas)

new_character = ("Ahsoka Tano", "Shili")
insert_before_character(queue, new_character, "Yoda")
print("C- Lista de personajes despues de ingresar un personaje nuevo antes del maestro Yoda:")
print(queue.show_queue())

print("D- Lista de personajes antes de eliminar al personaje despues de Jar Jar Binks:")
print(queue.show_queue())
remove_after_jar_jar(queue)
print(" * Lista de personajes despues de eliminar al personaje que sigue a Jar Jar Binks:")
print(queue.show_queue())