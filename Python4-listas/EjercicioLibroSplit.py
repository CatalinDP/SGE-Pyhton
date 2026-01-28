cadena = input("Introduce una cadena de texto: ")

while cadena != " ":
    palabras = cadena.split()
    print("Palabras: ", len(palabras))

    cadena = input("Vuelva a introducirlo")
