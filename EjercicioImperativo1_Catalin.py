# Parte 1 - Catalin P
import random as rd


def generaMatriz(filas, columnas):
    matriz = []
    casillas = filas * columnas
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            numRandom = rd.randint(0, casillas)
            while any(numRandom in fila for fila in matriz):
                numRandom = rd.randint(0, casillas)
            matriz[i].append(numRandom)
    return matriz


filas = int(input("Escribe el número de filas: "))
columnas = int(input("Escribe el número de columnas: "))

matriz = generaMatriz(filas, columnas)

# Parte 2


def sumarVecinos(coordenadas, matriz):
    fila = coordenadas.get("filas") - 1
    columna = coordenadas.get("columnas") - 1
    suma = 0
    if (fila-1) > 0 and (fila+1) < len(matriz):
        if (columna-1) > 0 and (columna+1) < len(matriz[0]):
            for i in range(-1, 2):
                for j in range(-1, 2):
                    suma += matriz[fila+i][columna+j]
        elif (columna-1) > 0 and (columna+1) >= len(matriz[0]):
            for i in range(-1, 2):
                for j in range(-1, 1):
                    suma += matriz[fila+i][columna+j]
        else:
            for i in range(-1, 2):
                for j in range(0, 2):
                    suma += matriz[fila+i][columna+j]
    elif (fila-1) > 0 and (fila+1) >= len(matriz):
        if (columna-1) > 0 and (columna+1) < len(matriz[0]):
            for i in range(-1, 2):
                for j in range(-1, 2):
                    suma += matriz[fila+i][columna+j]

        elif (columna-1) > 0 and (columna+1) >= len(matriz[0]):
            for i in range(-1, 1):
                for j in range(-1, 1):
                    suma += matriz[fila+i][columna+j]
        else:
            for i in range(0, 2):
                for j in range(0, 2):
                    suma += matriz[fila+i][columna+j]
    else:
        if (columna-1) > 0 and (columna+1) < len(matriz[0]):
            for i in range(0, 2):
                for j in range(-1, 2):
                    suma += matriz[fila+i][columna+j]
        elif (columna-1) > 0 and (columna+1) >= len(matriz[0]):
            for i in range(0, 2):
                for j in range(-1, 1):
                    suma += matriz[fila+i][columna+j]
        else:
            for i in range(0, 2):
                for j in range(0, 2):
                    suma += matriz[fila+i][columna+j]
    return suma


filas2 = -1
while 5 < filas2 or filas2 < 0:
    filas2 = int(input("Introduce una fila que este en los 'rangos' matriz: "))

columnas2 = -1
while 4 < columnas2 or columnas2 < 0:
    columnas2 = int(input(
        "Introduce una columna "
        "que este en los 'rangos' matriz: ")
        )

coordenadas = {"filas": filas2, "columnas": columnas2}
print(matriz)
suma = sumarVecinos(coordenadas, matriz)
print("Suma vecinos", suma)
