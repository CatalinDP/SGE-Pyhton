class Persona:
    def __init__(self, nombre, dni, edad=18):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad

    def iniciales(self):
        cadena = ""
        for c in self.nombre:
            if c >= 'A' and c <= 'Z':
                cadena += c + "."
        return cadena

    def __str__(self):
        return self.nombre


P = Persona("Catalin A B C", 2222)
print(P.edad)
print(P.iniciales())
print(P)
