# 4.- Escribir un programa que solicite un número positivo,
# acto seguido debe calcular la suma de
# todos los números pares comprendidos entre 0 y el numero solicitado.

def calculaPares(num):
    suma = 0
    for i in range(2, num, 2):
        suma += i
    return suma
# suma = sum(list(range(2, num, 2))) Crea una lista de esos párametros    


print("Introduce un número positivo")
num = int(input())
suma = list(range(num))
# print(f"La suma de los pares es{calculaPares(num)}")
y = suma[0::2]
print(y)
