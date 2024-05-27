def tieneRepetidos(lista):
    """
    Devuelve True si la lista tiene al menos un elemento repetido, False en caso contrario.

    Argumentos:
    lista: Una lista de elementos.

    Retorna:
    True si la lista tiene al menos un elemento repetido, False en caso contrario.
    """
    # Creamos un conjunto vacío para almacenar los elementos únicos que hemos visto
    elementos_vistos = set()

    # Iteramos sobre cada elemento en la lista
    for elemento in lista:
        # Si el elemento ya está en el conjunto, significa que es un duplicado
        if elemento in elementos_vistos:
            return True
        # Si no está en el conjunto, lo agregamos
        else:
            elementos_vistos.add(elemento)

    # Si llegamos hasta aquí, significa que no hay elementos repetidos en la lista
    return False

# Ejemplo de uso
lista1 = [1, 2, 3, 4, 5]
lista2 = [1, 2, 3, 3, 4, 5]
print("¿La lista 1 tiene elementos repetidos?:", tieneRepetidos(lista1))
print("¿La lista 2 tiene elementos repetidos?:", tieneRepetidos(lista2))