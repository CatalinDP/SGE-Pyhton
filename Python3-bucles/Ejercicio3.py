# Programa que lee notas de los alumnos y dice cuántos están
# aprobados y cuál es la nota
# media. El programa dejará de pedir notas, cuando se pulse la tecla ENTER.

def estaAprobado(notas: list):
    numAlumnos = len(notas)
    aprobados = 0
    suspensos = 0
    media = 0.0
    i = 1
    for nota in notas:
        parsedNota = float(nota)
        if parsedNota >= 5:
            print(f"Nota del alumno: {i} aprobado")
            aprobados += 1
        else:
            print(f"Nota del alumno: {i} no aprobado")
            suspensos += 1
        media += parsedNota
        i += 1
    print(
        f"Total de alumnos {numAlumnos}, aprobados: {aprobados}, suspensos:",
        f"{suspensos} y la media es de {media / numAlumnos}"
        )


print("Introduce las notas, pulsa ENTER para terminar")
notasInput = input()
notas = notasInput.split(" ")

estaAprobado(notas)
