# 8.- Escribir un programa que “dibuje” un mes del calendario.
# El programa recibirá como entrada el
# número de días del mes y el día de la semana del primer día del mes.

print("Introduce el número de días")
dias = int(input())
print("Primer día del mes 0 lunes - 6 domingo")
diaMes = int(input())
print("L\tM\tX\tJ\tV\tS\tD")

saltoDeLinea = "\t" * diaMes
print(end=saltoDeLinea)

for i in range(1, dias+1):
    print(i, end="\t")
    if (i+diaMes) % 7 == 0:
        print()
