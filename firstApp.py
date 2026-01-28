# Catalin Dumitru Posedaru
# 31/10/2025
# Enunciado

s = input("Introduce los segundos")
m = input("Introduce los minutos")
h = input("Introduce las horas")
if s == 60:
    s = 0
    m += 1
else:
    s += 1
    if m == 60:
        m = 0
        h += 1
    else:
        m += 1
        if h == 23:
            h = 0
        else:
            h += 1

ss = (s+1) % 60
ms = ((m + ((s+1) // 60))) % 60
