    def factores_primos(n):
    """
    Encuentra los factores primos de un número n.

    Argumento:
    n: Un entero positivo.

    Retorna:
    Una lista que contiene los factores primos de n.
    """
    factores = []  # Lista para almacenar los factores primos

    # Iteramos desde 2 hasta la raíz cuadrada de n
    for i in range(2, int(n**0.5) + 1):
        # Dividimos n repetidamente por i mientras sea divisible
        while n % i == 0:
            factores.append(i)  # Agregamos i como factor primo
            n //= i  # Actualizamos n dividiéndolo por i

    # Si al final de las iteraciones n es mayor que 1, significa que es un primo mayor que la raíz cuadrada de n
    if n > 1:
        factores.append(n)

    return factores

# Ejemplo de uso
numero = 24
print("Los factores primos de", numero, "son:", factores_primos(numero))
