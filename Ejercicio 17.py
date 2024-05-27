def mcd(a, b):
    """
    Calcula el máximo común divisor (MCD) de dos enteros positivos utilizando el algoritmo de Euclides.

    Argumentos:
    a: Un entero positivo.
    b: Un entero positivo.

    Retorna:
    El máximo común divisor (MCD) de a y b.
    """
    # Algoritmo de Euclides para calcular el MCD
    while b != 0:
        # Calculamos el residuo de la división de a entre b
        residuo = a % b
        # Ahora hacemos b igual a a y a igual a residuo
        a = b
        b = residuo

    # Cuando b sea cero, el MCD estará en a
    return a

# Ejemplo de uso
num1 = 48
num2 = 36
print("El máximo común divisor (MCD) de", num1, "y", num2, "es:", mcd(num1, num2))
