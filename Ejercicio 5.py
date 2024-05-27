def sonFactores(n, lista):
    """
    Devuelve True si los números de la lista son factores de n.

    Argumentos:
    n: Un entero.
    lista: Una lista de enteros.

    Retorna:
    True si todos los números de la lista son factores de n, False en caso contrario.
    """
    for numero in lista:
        # Verificar si n no es divisible por alguno de los números de la lista
        if n % numero != 0:
            return False
    # Si no se encontró ningún número de la lista que no fuera factor de n, devolver True
    return True

# Ejemplo de uso
n = 12
factores = [1, 2, 3, 4, 6]
print("¿Los números de la lista son factores de", n, "?:", sonFactores(n, factores))