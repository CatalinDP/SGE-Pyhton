class Diccionario:
    def __init__(self, nombre, editorial="Sant", nivel="1"):
        self.nombre = nombre
        self.editorial = editorial
        self.nivel = nivel
        self.dicc = dict()

    def introducirPalabra(self, palabra):
        resultado = "Ya existe"
        if palabra not in self.dicc:
            self.dicc[palabra] = list()
            resultado = "Palabra introducida"

        return resultado

    def introducirAcepciones(self, acepcion, palabra):
        resultado = f"No existe la palabra: {palabra}"
        if palabra in self.dicc:
            self.dicc[palabra].append(acepcion)
            resultado = f"Acepción introducida a {palabra}"
        return resultado
    
    def consultarPalabras(self, L):
        r = ""
        r = (
            f"Nombre: {self.nombre}\nEditorial: {self.editorial}"
            f"\nNivel: {self.nivel}\nDiccionario: {self.dicc}"
        )
        LP = list(self.dicc.keys())
        LP.sort()
        i = 0
        while i < len(LP) and LP[i][0] < L:
            i += 1
        
        while i < len(LP) and LP[i][0] == L:
            r += f"{LP[i]}: \n"
            for a in self.dicc[LP[i]]:
                r += f"\t- {a}\n"
            i += 1
        return r

    def __str__(self):
        r = (
            f"Nombre: {self.nombre}\nEditorial: {self.editorial}"
            f"\nNivel: {self.nivel}\nDiccionario: {self.dicc}"
        )
        LP = list(self.dicc.keys())
        LP.sort()
        for k in LP:
            r += f"{k}:\n"
            for a in self.dicc[k]:
                r += f"- {a}\n"
        return r


userInput = 8
while userInput != 0:
    print("-----------------------------------------")
    print("0 - Salir")
    print("1 - Crear diccionario")
    print("2 - Introducir palabra")
    print("3 - Introducir acepción")
    print("4 - Mostrar diccionario")
    print("-----------------------------------------")
    userInput = int(input("Introduzca una de las opciones anteriores: "))
    if userInput == 1:
        nombre = input("Nombre del diccionario: ")
        MiDic = Diccionario(nombre)
        print(MiDic.dicc)
    elif userInput == 2:
        palabra = input("Introduce la palabra a añadir: ")
        print(MiDic.introducirPalabra(palabra))
        print(MiDic.dicc)
    elif userInput == 3:
        palabra = input("Introduce la palabra clave: ")
        acepcion = input(f"Introduce la acepcion a {palabra}: ")
        print(MiDic.introducirAcepciones(acepcion, palabra))
        print(MiDic.dicc)
    elif userInput == 4:
        print(MiDic)
