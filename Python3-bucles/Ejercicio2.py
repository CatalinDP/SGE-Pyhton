# 2.- Escribir un programa que imprima las 10 tablas de multiplicar.

for i in range(11):
    for j in range(11):
        print(f"{j} x {i} = {j * i}")
    print("---------------------")
