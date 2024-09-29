from datetime import datetime

class HeapMin:
    def __init__(self):
        self.elements = []
    
    def add(self, value):
        self.elements.append(value)
        self.float(len(self.elements) - 1)

    def remove(self):
        if len(self.elements) > 0:
            self.interchange(0, len(self.elements) - 1)
            value = self.elements.pop()
            self.sink(0)
            return value
        else:
            return None

    def interchange(self, index_1, index_2):
        self.elements[index_1], self.elements[index_2] = self.elements[index_2], self.elements[index_1]

    def float(self, index):
        father = (index - 1) // 2
        while index > 0 and self.elements[index][0] < self.elements[father][0]:
            self.interchange(index, father)
            index = father
            father = (index - 1) // 2

    def sink(self, index):
        left_child = (index * 2) + 1
        control = True
        while control and left_child < len(self.elements):
            right_child = (index * 2) + 2
            min = left_child
            if right_child < len(self.elements):
                if self.elements[right_child][0] < self.elements[left_child][0]:
                    min = right_child
            if self.elements[index][0] > self.elements[min][0]:
                self.interchange(index, min)
                index = min
                left_child = (index * 2) + 1
            else:
                control = False

    def arrive(self, priority, encargado, descripcion, hora, stormtroopers=None):
        self.add([priority, {"encargado": encargado, "descripcion": descripcion, "hora": hora, "stormtroopers": stormtroopers}])

    def attention(self):
        return self.remove()

cola_operaciones = HeapMin()
cola_operaciones.arrive(3, "Kylo Ren", "Revision de sistemas de defensa", "10:00")
cola_operaciones.arrive(3, "Snoke", "Supervision de construccion de armas", "11:00")
cola_operaciones.arrive(2, "Capitan Phasma", "Entrenamiento de Stormtroopers", "09:30", 50)
cola_operaciones.arrive(2, "Capitán Phasma", "Inspeccion de hangar", "12:00")
cola_operaciones.arrive(1, "General Hux", "Revision de informes", "08:00")
cola_operaciones.arrive(1, "General Hux", "Monitoreo de comunicaciones", "08:30")
cola_operaciones.arrive(1, "General de la base", "Mantenimiento de sistemas", "09:00")
cola_operaciones.arrive(1, "General de la base", "Supervision de patrullas", "09:15")

def atender_operaciones(cola, n):
    for i in range(n):
        operacion = cola.attention()
        print(f"Atendiendo operación {i+1}: {operacion[1]['descripcion']} por {operacion[1]['encargado']} a las {operacion[1]['hora']}")
        if operacion[1].get("stormtroopers"):
            print(f"Se requieren {operacion[1]['stormtroopers']} Stormtroopers.")
        print(f"Prioridad de la operación: {operacion[0]}")
        print("---")

atender_operaciones(cola_operaciones, 5)

print("Añadiendo operacion despues de la quinta atencion: 'Revision de intrusos en el hangar B7' solicitada por Capitán Phasma.")
cola_operaciones.arrive(2, "Capitan Phasma", "Revision de intrusos en el hangar B7", "13:00", 25)
atender_operaciones(cola_operaciones, 1)
print("Añadiendo operacion despues de la sexta atencion: 'Destruccion del planeta Takodana' solicitada por Snoke.")
cola_operaciones.arrive(3, "Snoke", "Destruccion del planeta Takodana", "14:00")
atender_operaciones(cola_operaciones, len(cola_operaciones.elements))