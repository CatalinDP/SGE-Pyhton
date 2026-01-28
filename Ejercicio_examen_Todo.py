import random

# Función Se piden los nombres
# de personas hasta pulsar enter y devuelve lista


def Generar_Lista_Nombre():
    L = []
    nombre = input("Nombre: ")
    while nombre != "":
        L.append(nombre)
        nombre = input("Nombre: ")
    return L

# Función que genera una matriz cuadrada según el
# número de personas y coloca aleatoriamente los
# nombres de las personas y la devuelve la matriz


def Matriz_Personas(L):
    M = list()
    for i in range(0, len(L)):
        M.append([])
        for j in range(0, len(L)):
            M[i].append(random.choice(L))
    return M


# Función mostrar matriz

def MostrarMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end="\t")
        print()


def ObtenerCoordenadas(nombres, matriz):
    diccionario = {}
    for nombre in nombres:
        diccionario[nombre] = []
    for fila in range(0, len(matriz)):
        for columna in range(0, len(matriz)):
            coordenada = (fila, columna)
            diccionario[matriz[fila][columna]].append(coordenada)
    return diccionario


def mostrarDiccionario(DC):
    for p in DC:
        print(f"{p}: ", end="")
        cadena = ""
        for c in DC[p]:
            cadena += str(c) + ", "
        print(cadena[0:-2])


def estaEnDc(DC):
    noEstan = "No existe: "
    for p in DC:
        if DC[p] == []:
            noEstan += p + ", "
    print(noEstan[:-2])


def infoPersonas(dicc, longitud):
    dc = {}
    i = 1
    for p in dicc:
        print(f"{p} - {i}")
        dc[i] = p
        i += 1

    userIn = int(input("Introduce el número de la persona que quieras ver: "))
    while userIn <= 0 or userIn > longitud:
        userIn = int(
            input("Introduce el número de la persona que quieras ver: ")
            )

    lista = list(dicc[dc[userIn]])
    for i in range(longitud):
        for j in range(longitud):
            if ((i, j) in lista):
                print(f"{dc[userIn]}", end="\t")
            else:
                print("----", end="\t")
        print()


def comerMatriz(matriz):
    pass
########


print("0.- Salir")
print("1.- Generar Lista Nombres")
print("2.- Cuadrada")
print("3.- Mostrar Matriz")
print("4.- ObtenerCoordenadas")
print("5.- Mostrar diccionario")
print("6.- Comprobar quienes estan")
print("7.- Información de personas")
print("8.- Comer personas")

opcion = int(input("Opcion: "))
LNombre = list()
while opcion != 0:
    if opcion == 1:
        # LNombre = Generar_Lista_Nombre()
        # print(LNombre)
        LNombre = ['Pepe', 'María', 'Juan']
    elif opcion == 2:
        M = Matriz_Personas(LNombre)
        print(M)
    elif opcion == 3:
        MostrarMatriz(M)
    elif opcion == 4:
        DC = ObtenerCoordenadas(LNombre, M)
        print(DC)
    elif opcion == 5:
        mostrarDiccionario(DC)
    elif opcion == 6:
        estaEnDc(DC)
    elif opcion == 7:
        infoPersonas(DC, len(LNombre))
    elif opcion == 8:
        comerMatriz(M)


    opcion = int(input("Opcion: "))
