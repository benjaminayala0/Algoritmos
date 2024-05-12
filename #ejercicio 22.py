#ejercicio 22
def usar_la_fuerza(mochila):
    #Caso:si la mochila esta vacía, devuelve -1
    if not mochila:
        print("no hay mas objetos en la mochila")
        return -1

    #sacar un objeto de la mochila
    objeto = mochila.pop()

    #si el objeto es un sable de luz, devuelve el numero de objetos sacados
    if objeto == "sable de luz":
        print("¡encontraste el sable de luz!")
        return len(mochila)
    else:
        return usar_la_fuerza(mochila)

#prueba de funcion
mochila = [""] #vector
print(f"se necesitaron {usar_la_fuerza(mochila)} objetos para encontrar el sable de luz")
