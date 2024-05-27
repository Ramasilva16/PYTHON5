def interseccion(lista1, lista2):
    """
    Devuelve una nueva lista que contiene los elementos que están en ambas listas.

    Argumentos:
    lista1: Primera lista sin elementos repetidos.
    lista2: Segunda lista sin elementos repetidos.

    Retorna:
    Una nueva lista que contiene los elementos que están en ambas listas.
    """
    # Utilizamos la función set() para convertir las listas en conjuntos y luego aplicamos la operación de intersección (&)
    interseccion_set = set(lista1) & set(lista2)

    # Convertimos el conjunto de intersección nuevamente en lista
    interseccion_lista = list(interseccion_set)

    return interseccion_lista

# Ejemplo de uso
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
print("La intersección de las listas es:", interseccion(lista1, lista2))
