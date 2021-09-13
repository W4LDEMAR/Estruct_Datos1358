# Autor: Sosa Hernandez Saul Waldemar
# Estructura de datos
# Tarea 2: Recursividad

def suma(len):
    if len > 0:
        resultado = 0 + lista_nums[len - 1]
        lista_nums.pop(len)
        suma(len - 1)
    return resultado

lista_nums = [1, 2, 3]
len = int(len(lista_nums))
resultado = suma(len)
print(f"La suma de todos los datos de la lista es:\n {resultado}")