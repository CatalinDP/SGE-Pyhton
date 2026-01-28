import random


def generarCiudad(filas, columnas):
    n = random.randint(0, filas-1)
    r = random.randint(0, columnas-1)
    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            if n == i and r == j:
                matriz[i].append("I-0")
            else:
                matriz[i].append("SANO")
    return matriz


def mostrarMatriz(matriz, dia):
    print("Mostrando matriz dia: ", dia)
    filas = len(matriz)
    columnas = len(matriz[0])
    for i in range(filas):
        for j in range(columnas):
            print(matriz[i][j], end="\t")
        print()


def contagiar(matriz):
    dia = 0
    filas = len(matriz)
    columnas = len(matriz[0])
    seguir = True
    mostrarMatriz(matriz, dia)
    while seguir:
        seguir = False
        dia += 1
        matrizInfectada = [fila[:] for fila in matriz]
        for i in range(filas):
            for j in range(columnas):
                if matriz[i][j] != "SANO":
                    if i > 0 and matriz[i-1][j] == "SANO":
                        matrizInfectada[i-1][j] = f"I-{dia}"
                        seguir = True
                    if j > 0 and matriz[i][j-1] == "SANO":
                        matrizInfectada[i][j-1] = f"I-{dia}"
                        seguir = True
                    if j < columnas-1 and matriz[i][j+1] == "SANO":
                        matrizInfectada[i][j+1] = f"I-{dia}"
                        seguir = True
                    if i < filas-1 and matriz[i+1][j] == "SANO":
                        matrizInfectada[i+1][j] = f"I-{dia}"
                        seguir = True
        matriz = matrizInfectada
        mostrarMatriz(matriz, dia)
    return matriz


filas = int(input("Filas: "))
columnas = int(input("Columnas: "))
matriz = generarCiudad(filas, columnas)

contagiar(matriz)
