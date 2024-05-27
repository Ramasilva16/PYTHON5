def maximoEntre(lista, a, b):
    """
    Devuelve el índice del máximo elemento en una lista de números, considerando solo los elementos entre los índices a y b.

    Argumentos:
    lista: Una lista de números.
    a: Un entero que representa el índice de inicio (inclusive).
    b: Un entero que representa el índice de fin (inclusive).

    Retorna:
    El índice del máximo elemento entre los índices a y b en la lista. Si no hay elementos entre a y b, o si a y b son mayores o iguales a la longitud de la lista, devuelve None.
    """
    # Verificamos si los índices a y b son válidos
    if a < 0 or b < 0 or a >= len(lista) or b >= len(lista) or a > b:
        return None  # Índices inválidos

    # Utilizamos la función max() para encontrar el máximo elemento en el rango de índices especificado
    maximo_valor = max(lista[a:b+1])

    # Utilizamos el método index() para encontrar el índice del primer elemento con el valor máximo
    indice_maximo = lista.index(maximo_valor, a, b+1)

    return indice_maximo

# Ejemplo de uso
numeros = [1, 5, 3, 9, 2, 7]
a = 1
b = 4
print("El índice del máximo elemento entre los índices", a, "y", b, "en la lista es:", maximoEntre(numeros, a, b))
