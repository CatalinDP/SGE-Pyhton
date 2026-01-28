# 5.- Escribe un programa que dado un número, muestre todos los múltiplos
# de 11 desde el cero
# hasta el número.

def multiplosOnce(num):
    numeroBase = 0
    while numeroBase < num:
        print(numeroBase)
        numeroBase += 11


print("Introduzca un número")
multiplosOnce(int(input()))
