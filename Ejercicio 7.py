def dondeAparece(lista, blanco):
    """
    Devuelve el primer índice donde aparece el número blanco en la lista, o -1 si no aparece.

    Argumentos:
    lista: Una lista de enteros.
    blanco: El entero a buscar en la lista.

    Retorna:
    El primer índice donde aparece blanco en la lista, o -1 si no aparece.
    """
    # Iteramos sobre los índices y valores de la lista
    for i, elemento in enumerate(lista):
        # Si encontramos el número blanco, devolvemos su índice
        if elemento == blanco:
            return i
    # Si llegamos hasta aquí, significa que no se encontró el número blanco en la lista
    return -1

# Ejemplo de uso
lista = [1, 2, 3, 4, 5, 2]
blanco = 2
print("El primer índice donde aparece", blanco, "en la lista es:", dondeAparece(lista, blanco))