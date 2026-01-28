# 1.- Programa que lee un número y muestra la tabla de multiplicar de
# dicho número.
# Hacer el ejercicio de dos formas, con bucle while y con bucle for.

def tablaFor(num):
    for i in range(11):
        print(f"{num} x {i} = {num * i}")


def tablaWhile(num):
    i = 0
    while i <= 10:
        print(f"{num} x {i} = {num * i}")
        i += 1


print("Tabla for ----")
tablaFor(5)
print("Tabla while ----")
tablaWhile(5)
