def laMasCorta(lista1, lista2):
    """
    Devuelve la lista que tenga menos elementos. Si tienen igual cantidad, devuelve la primera.

    Argumentos:
    lista1: Primera lista.
    lista2: Segunda lista.

    Retorna:
    La lista que tenga menos elementos. Si tienen igual cantidad, devuelve la primera.
    """
    if len(lista1) <= len(lista2):
        return lista1
    else:
        return lista2

# Ejemplo de uso
lista1 = [1, 2, 3]
lista2 = [4, 5]
print("La lista más corta es:", laMasCorta(lista1, lista2))