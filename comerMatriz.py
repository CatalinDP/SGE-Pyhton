def comerMatriz(matriz):
    leng = len(matriz)
    seguir = True
    while (seguir):
        seguir = False
        for i in range(leng):
            for j in range(leng):
                print(f"I-> {i} --- J-> {j}")
                if j > 0 and j < leng-1:
                    if matriz[i][j-1] == matriz[i][j+1]:
                        if matriz[i][j] != matriz[i][j+1]:
                            seguir = True
                            matriz[i][j] = matriz[i][j+1]
                if i > 0 and i < leng-1:
                    if matriz[i-1][j] == matriz[i+1][j]:
                        if matriz[i][j] != matriz[i+1][j]:
                            seguir = True
                            matriz[i][j] = matriz[i+1][j]
                if j == 0 and i == 0:
                    if matriz[i+1][j] == matriz[i][j+1]:
                        if matriz[i][j] != matriz[i+1][j]:
                            seguir = True
                            matriz[i][j] = matriz[i+1][j]
                if j == 0 and i == 0:
                    if matriz[i+1][j] == matriz[i][j+1]:
                        if matriz[i][j] != matriz[i+1][j]:
                            seguir = True
                            matriz[i][j] = matriz[i+1][j]
                if j == leng-1 and i == 0:
                    if matriz[i+1][j] == matriz[i][j-1]:
                        if matriz[i][j] != matriz[i+1][j]:
                            seguir = True
                            matriz[i][j] = matriz[i+1][j]
                if j == 0 and i == leng-1:
                    if matriz[i-1][j] == matriz[i][j+1]:
                        if matriz[i][j] != matriz[i-1][j]:
                            seguir = True
                            matriz[i][j] = matriz[i+1][j]
                if j == leng-1 and i == leng-1:
                    if matriz[i-1][j] == matriz[i][j-1]:
                        if matriz[i][j] != matriz[i-1][j]:
                            seguir = True
                            matriz[i][j] = matriz[i-1][j]
                print(matriz)


def comerMatrizProf(matriz):
    leng = len(matriz)
    cambio = True
    while cambio:
        cambio = False
        for i in range(leng):
            for j in range(leng):
                vecinos = []
                CV = False
                if i > 0 and matriz[i][j] != matriz[i-1][j]:
                    vecinos.append(matriz[i-1][j])
                if j < leng-1 and matriz[i][j] != matriz[i][j+1]:
                    if matriz[i][j+1] in vecinos:
                        cambio = True
                        CV = True
                        matriz[i][j] = matriz[i][j+1]
                    else:
                        vecinos.append(matriz[i][j+1])
                if i < leng-1 and not CV and matriz[i][j] != matriz[i+1][j]:
                    if matriz[i+1][j] in vecinos:
                        cambio = True
                        CV = True
                        matriz[i][j] = matriz[i+1][j]
                    else:
                        vecinos.append(matriz[i+1][j])
                if j > 0 and not CV and matriz[i][j] != matriz[i][j-1]:
                    if matriz[i][j-1] in vecinos:
                        cambio = True
                        CV = True
                        matriz[i][j] = matriz[i][j-1]
                    else:
                        vecinos.append(matriz[i][j-1])
    print(matriz)


matriz = [
    ['Maria', 'Juan', 'Maria'],
    ['Juan', 'Pepe', 'Maria'],
    ['Pepe', 'Maria', 'Juan']
]

comerMatrizProf(matriz)
