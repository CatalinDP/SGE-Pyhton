matriz = list()
size = 5
for i in range(1, size+1):
    fila = input(f"Introduzca fila {i}: ")
    filaList = fila.split()
    matriz.append(filaList)
print(matriz)

# Suma de columnas
sumaColumnas = [0] * size
for i in range(size):
    for j in range(size):
        sumaColumnas[i] += int(matriz[j][i])

print("Columnas: ", sumaColumnas)

# Suma de filas
sumaFilas = [0] * size
for i in range(size):
    for j in range(size):
        sumaFilas[i] += int(matriz[i][j])

print("Filas: ", sumaFilas)
