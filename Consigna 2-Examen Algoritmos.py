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

dinosaurios = [
    {
      "nombre": "Tyrannosaurus Rex",
      "especie": "Theropoda",
      "peso": "7000 kg",
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1902
    },
    {
      "nombre": "Triceratops",
      "especie": "Ceratopsidae",
      "peso": "6000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1889
    },
    {
      "nombre": "Velociraptor",
      "especie": "Dromaeosauridae",
      "peso": "15 kg",
      "descubridor": "Henry Fairfield Osborn",
      "ano_descubrimiento": 1924
    },
    {
      "nombre": "Brachiosaurus",
      "especie": "Sauropoda",
      "peso": "56000 kg",
      "descubridor": "Elmer S. Riggs",
      "ano_descubrimiento": 1903
    },
    {
      "nombre": "Stegosaurus",
      "especie": "Stegosauridae",
      "peso": "5000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Spinosaurus",
      "especie": "Spinosauridae",
      "peso": "10000 kg",
      "descubridor": "Ernst Stromer",
      "ano_descubrimiento": 1912
    },
    {
      "nombre": "Allosaurus",
      "especie": "Theropoda",
      "peso": "2000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Apatosaurus",
      "especie": "Sauropoda",
      "peso": "23000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Diplodocus",
      "especie": "Sauropoda",
      "peso": "15000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1878
    },
    {
      "nombre": "Ankylosaurus",
      "especie": "Ankylosauridae",
      "peso": "6000 kg",
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1908
    },
    {
      "nombre": "Parasaurolophus",
      "especie": "Hadrosauridae",
      "peso": "2500 kg",
      "descubridor": "William Parks",
      "ano_descubrimiento": 1922
    },
    {
      "nombre": "Carnotaurus",
      "especie": "Theropoda",
      "peso": "1500 kg",
      "descubridor": "José Bonaparte",
      "ano_descubrimiento": 1985
    },
    {
      "nombre": "Styracosaurus",
      "especie": "Ceratopsidae",
      "peso": "2700 kg",
      "descubridor": "Lawrence Lambe",
      "ano_descubrimiento": 1913
    },
    {
      "nombre": "Therizinosaurus",
      "especie": "Therizinosauridae",
      "peso": "5000 kg",
      "descubridor": "Evgeny Maleev",
      "ano_descubrimiento": 1954
    },
    {
      "nombre": "Pteranodon",
      "especie": "Pterosauria",
      "peso": "25 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1876
    },
    {
      "nombre": "Quetzalcoatlus",
      "especie": "Pterosauria",
      "peso": "200 kg",
      "descubridor": "Douglas A. Lawson",
      "ano_descubrimiento": 1971
    },
    {
      "nombre": "Plesiosaurus",
      "especie": "Plesiosauria",
      "peso": "450 kg",
      "descubridor": "Mary Anning",
      "ano_descubrimiento": 1824
    },
    {
      "nombre": "Mosasaurus",
      "especie": "Mosasauridae",
      "peso": "15000 kg",
      "descubridor": "William Conybeare",
      "ano_descubrimiento": 1829
    },
  ]

def contar_especies(dinosaurios):
    pila_especies = Stack()
    especies_vistas = set()
    for dino in dinosaurios:
        if dino["especie"] not in especies_vistas:
            pila_especies.push(dino["especie"])
            especies_vistas.add(dino["especie"])
    return pila_especies.size()


def contar_descubridores(dinosaurios):
    pila_descubridores = Stack()
    descubridores_vistos = set() 
    for dino in dinosaurios:
        if dino["descubridor"] not in descubridores_vistos:
            pila_descubridores.push(dino["descubridor"])
            descubridores_vistos.add(dino["descubridor"])
    return pila_descubridores.size()


def dino_con_t(dinosaurios):
    pila_dino_t = Stack()
    for dino in dinosaurios:
        if dino["nombre"].startswith("T"):
            pila_dino_t.push(dino)
    return pila_dino_t

def dino_menosde_275kg(dinosaurios):
    pila_dino_livianos = Stack()
    for dino in dinosaurios:
        if int(dino["peso"].split()[0]) < 275:
            pila_dino_livianos.push(dino)
    return pila_dino_livianos

def dino_con_a_q_s(dinosaurios):
    pila_dino_aqs = Stack()
    for dino in dinosaurios:
        if dino["nombre"].startswith(("A", "Q", "S")):
            pila_dino_aqs.push(dino)
    return pila_dino_aqs

def print_dino(stack):
    while stack.size() > 0:
        dino = stack.pop()
        print(f"Nombre: {dino['nombre']}, especie: {dino['especie']}, peso: {dino['peso']}, descubridor: {dino['descubridor']}, año de descubrimiento: {dino['ano_descubrimiento']}")

#respuestas
print("A-) Cantidad de especies que hay:", contar_especies(dinosaurios))
print("B-) Cantidad de descubridores diferentes:", contar_descubridores(dinosaurios))

print("C-) Dinosaurios que empiezan con T:")
dinos_t = dino_con_t(dinosaurios)
print_dino(dinos_t)

print("D-) Dinosaurios que pesan menos de 275 kg:")
dinos_ligeros = dino_menosde_275kg(dinosaurios)
print_dino(dinos_ligeros)

print("E-) Dinosaurios que empiezan con A-Q-S:")
dinos_aqs = dino_con_a_q_s(dinosaurios)
print_dino(dinos_aqs)