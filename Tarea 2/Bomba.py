# Autor: Sosa Hernandez Saul Waldemar
# Estructura de datos
# Tarea 2: Recursividad

def cuenta(seg):
    if seg == 0:
        print("BOOMMMMM !!!")
    else:
        print(seg)
        cuenta(seg - 1)

seg = int(input("La cuenta regresiva inicia en:\n"))
cuenta(seg)
