def maximo(lista):
    """
    Devuelve el valor del máximo elemento en una lista de números.

    Argumentos:
    lista: Una lista de números.

    Retorna:
    El valor del máximo elemento en la lista.
    """
    # Verificamos si la lista está vacía
    if not lista:
        return None  # Si la lista está vacía, no hay máximo

    # Utilizamos la función max() para encontrar el máximo elemento en la lista
    maximo_valor = max(lista)

    return maximo_valor

# Ejemplo de uso
numeros = [1, 5, 3, 9, 2, 7]
print("El máximo elemento en la lista es:", maximo(numeros))
