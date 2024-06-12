def inverso_(lista):
    if not lista:
        return []
    else:
        return [lista[-1]] + inverso_(lista[:-1])
#uso
lista = [1,3,4,5,6,7,8]
resultado = inverso_(lista)
if not resultado:
    print("No hay elementos") #Retorna un mensaje , si la lista esta vacia
else:
    print(resultado)