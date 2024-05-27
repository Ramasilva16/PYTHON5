def contar_menores_que(s, x):
    """
    Cuenta la cantidad de elementos de s que son menores que x.

    Argumentos:
    s: Una lista de números.
    x: Un número decimal.

    Retorna:
    La cantidad de elementos de s que son menores que x.
    """
    contador = 0  # Inicializamos el contador de elementos menores que x

    # Iteramos sobre cada elemento de s
    for elemento in s:
        if elemento < x:
            contador += 1  # Incrementamos el contador si el elemento es menor que x

    return contador

# Ejemplo de uso
numeros = [1, 2, 3, 4, 5]
x = 3.5
print("La cantidad de elementos de la lista menores que", x, "es:", contar_menores_que(numeros, x))
