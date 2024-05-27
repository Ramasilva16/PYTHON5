def divisores(numero):
    """
    Devuelve la lista de divisores del número dado.

    Argumentos:
    numero: Un entero.

    Retorna:
    Una lista de enteros que son divisores de numero.
    """
    lista_divisores = []  # Inicializamos una lista vacía para almacenar los divisores

    # Iteramos desde 1 hasta el número (inclusive)
    for i in range(1, numero + 1):
        # Si el número es divisible por i, entonces i es un divisor
        if numero % i == 0:
            lista_divisores.append(i)  # Agregamos i a la lista de divisores

    return lista_divisores

# Ejemplo de uso
numero = 12
print("Los divisores de", numero, "son:", divisores(numero))