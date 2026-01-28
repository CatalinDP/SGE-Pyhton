def comprobarNif(cadena) -> bool:
    L = (
        "T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J",
        "Z", "S", "Q", "V", "H", "L", "C", "K", "E")
    if len(cadena) == 9:
        numeros = cadena[:-1]
        if numeros.isnumeric():
            numeros = int(numeros)
            if L[numeros % 23] == cadena[-1]:
                return True
            else:
                print("Letra incorrecta")
                return False
        else:
            print("Introduzca 8 numeros y una letra!")
            return False
    else:
        print("Longitud del NIF incorrecto")
        return False


def generarLetraNif(numero) -> str:
    L = (
        "T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J",
        "Z", "S", "Q", "V", "H", "L", "C", "K", "E")
    if numero.isnumeric() and len(numero) == 8:
        numero = int(numero)
        return L[numero % 23]
    else:
        return "Longitud incorrecta"


userInput = ""


while userInput != 1:
    userInput = int(input(
        "1.- Salir\n2.- Comprobar NIF\n3 .-Generar letra NIF\n"
        ))

    if userInput == 1:
        print("Hasta luego!")
    elif userInput == 2:
        nif = input("Introduzca el nif a comprobar")
        if comprobarNif(nif):
            print("El NIF es correcto")
        else:
            print("Es incorrecto")
    elif userInput == 3:
        nif = input("Introduce el NIF sin letra")
        letra = generarLetraNif(nif)
        if len(letra) > 1:
            print(letra)
        else:
            print(f"La letra correspondiente a tu NIF es {letra}")
    else:
        print(
            "Por favor introduzca un número",
            "correspondiente al menú anterior"
            )
