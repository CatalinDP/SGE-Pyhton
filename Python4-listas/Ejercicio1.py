# Programa que cuente las vocales de una frase
print("Di una frase y te contaré las vocales")
frase = list(input())
vocales = ["a", "o", "u", "e", "i"]
cantidad = [0, 0, 0, 0, 0]

for letra in frase:
    if letra in vocales:
        cantidad[vocales.index(letra)] += 1

print(vocales, "\n", cantidad)

# for letra in frase:
#    if letra in vocales:
#        vocales[letra] += 1