def union(lista1, lista2):
    """
    Devuelve una nueva lista que contiene los elementos de ambas listas sin repetidos.

    Argumentos:
    lista1: Primera lista sin elementos repetidos.
    lista2: Segunda lista sin elementos repetidos.

    Retorna:
    Una nueva lista que contiene los elementos de ambas listas sin repetidos.
    """
    # Convertimos las listas en conjuntos para eliminar los elementos repetidos
    set_union = set(lista1) | set(lista2)

    # Convertimos el conjunto de unión nuevamente en lista
    union_lista = list(set_union)

    return union_lista

# Ejemplo de uso
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
print("La unión de las listas es:", union(lista1, lista2))
