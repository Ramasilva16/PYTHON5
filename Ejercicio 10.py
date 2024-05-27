def maximoIndice(lista):
    """
    Devuelve el índice del máximo elemento en una lista de números.

    Argumentos:
    lista: Una lista de números.

    Retorna:
    El índice del máximo elemento en la lista. Si hay varios elementos con el mismo valor máximo, devuelve el índice del primero encontrado.
    """
    # Verificamos si la lista está vacía
    if not lista:
        return None  # Si la lista está vacía, no hay máximo

    # Utilizamos la función max() para encontrar el máximo elemento en la lista
    maximo_valor = max(lista)

    # Utilizamos el método index() para encontrar el índice del primer elemento con el valor máximo
    indice_maximo = lista.index(maximo_valor)

    return indice_maximo

# Ejemplo de uso
numeros = [1, 5, 3, 9, 2, 7]
print("El índice del máximo elemento en la lista es:", maximoIndice(numeros))
