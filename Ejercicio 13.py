def frecuencia(s, n):
    """
    Devuelve la cantidad de veces que aparece el entero n en la lista s.

    Argumentos:
    s: Una lista de enteros.
    n: El entero a buscar en la lista s.

    Retorna:
    La cantidad de veces que aparece el entero n en la lista s.
    """
    # Utilizamos el método count() para contar la cantidad de veces que aparece n en la lista s
    cantidad = s.count(n)
    return cantidad

# Ejemplo de uso
numeros = [1, 2, 3, 4, 2, 2, 5, 2]
n = 2
print("El número", n, "aparece", frecuencia(numeros, n), "veces en la lista.")
