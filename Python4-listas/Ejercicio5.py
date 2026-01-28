monedas = {500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}
importe = int(input("Dime una cantidad de dinero "))

# Calcular billetes
for moneda in monedas:
    monedas[moneda] = importe // moneda
    importe = importe % moneda

# Mostrar resultado
for moneda in monedas:
    if monedas[moneda] > 0:
        print(
            f"{monedas[moneda]} "
            f"{"billete" if moneda > 2 else "moneda"} "
            f"{"s" if monedas[moneda] > 1 else ""} de {moneda}"
        )
