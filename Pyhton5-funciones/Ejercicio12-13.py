import random as rd


def generarMatriz():
    matriz = list()
    for i in range(2):
        L = list()
        for i in range(0, rd.randint(2, 6)):
            L.append(rd.randint(0, 100))
        matriz.append(L)
    print(matriz)
    return matriz


def sumarCuadrado(matriz):
    if len(matriz[0]) == len(matriz[1]):
        M = list()
        


userInput = ""
matriz = list()
while userInput != 1:
    userInput = int(input(
        "1.- Salir\n2.- Generar matriz\n3.- Sumar cuadrado\n"
        ))

    if userInput == 1:
        print("Hasta luego!")
    elif userInput == 2:
        matriz = generarMatriz()
    elif userInput == 3:
        sumarCuadrado(matriz)
    else:
        print(
            "Por favor introduzca un número",
            "correspondiente al menú anterior"
            )
