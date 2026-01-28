numEmpleado = [1, 2, 3, 4]
nombre = ["Mario", "Luigi", "Wario", "Waluigi"]
categoria = ["A", "B", "B", "D"]
paisOrigen = ["España", "España", "Alemania", "Italia"]
contadorCategoria = [0, 0, 0, 0]
contadorPais = [0, 0, 0, 0]

for i in range(len(numEmpleado)):
    for cat in categoria:
        if cat == categoria[i]:
            contadorCategoria[i] += 1
    for pais in paisOrigen:
        if pais == paisOrigen[i]:
            contadorPais[i] += 1

maxPais = max(contadorPais)
index = -1
for i in range(len(paisOrigen)):
    print(f"En {paisOrigen[i]} hay {contadorPais[i]} empleados")
    print(f"En {categoria[i]} hay {contadorCategoria[i]} empleados")
    if paisOrigen[i] == maxPais:
        index = i

print(f"El pais con más empleados es {paisOrigen[index]} con",
      f"{maxPais} empleados")

empleados = {
    1: {
        "nombre": "Mario",
        "categoria": "A",
        "paisOrigen": "España"
    },
    2: {
        'nombre': 'Luigi',
        'categoria': 'B',
        'paisOrigen': 'España'
    },
    3: {
        'nombre': 'Wario',
        'categoria': 'B',
        'paisOrigen': 'Alemania'
    },
    4: {
        'nombre': 'Waluigi',
        'categoria': 'D',
        'paisOrigen': 'Italia'
    }
}
