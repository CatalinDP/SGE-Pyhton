import random


def generarNumeros() -> list:
    numeros = []
    for i in range(27):
        n = random.randint(1, 90)
        while n in numeros:
            n = random.randint(1, 90)
        numeros.append(n)
    return numeros


def mostrarBingo(lista):
    for i in range(len(lista)):
        print(lista[i], end="  ")
        if (i+1) % 9 == 0 and not i == 0:
            print()


lista = generarNumeros()
mostrarBingo(lista)
