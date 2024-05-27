def diferencia(lista1, lista2):
    """
    Devuelve una nueva lista que contiene los elementos de la primera lista que no están en la segunda lista.

    Argumentos:
    lista1: Primera lista sin elementos repetidos.
    lista2: Segunda lista sin elementos repetidos.

    Retorna:
    Una nueva lista que contiene los elementos de la primera lista que no están en la segunda lista.
    """
    # Utilizamos la función set() para convertir ambas listas en conjuntos
    set_lista1 = set(lista1)
    set_lista2 = set(lista2)

    # Calculamos la diferencia entre los conjuntos
    diferencia_set = set_lista1 - set_lista2

    # Convertimos el conjunto de diferencia en lista
    diferencia_lista = list(diferencia_set)

    return diferencia_lista

# Ejemplo de uso
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
print("La diferencia entre las listas es:", diferencia(lista1, lista2))
