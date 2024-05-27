def primeros_n_primos(n):
    """
    Encuentra los primeros n números primos utilizando el algoritmo de la criba de Eratóstenes.

    Argumento:
    n: Un entero positivo que representa la cantidad de números primos que se desean encontrar.

    Retorna:
    Una lista que contiene los primeros n números primos.
    """
    # Creamos una lista de booleanos para representar si un número es primo o no
    es_primo = [True] * (n * 10)  # Inicializamos con True para todos los números desde 0 hasta n*10

    # Inicializamos la lista de primos
    primos = []

    # Iteramos desde 2 hasta la raíz cuadrada de n*10
    for i in range(2, int(n**0.5) + 1):
        # Si es_primo[i] es True, entonces i es primo
        if es_primo[i]:
            # Agregamos i a la lista de primos
            primos.append(i)
            # Marcamos como no primo todos los múltiplos de i
            for j in range(i*i, n*10, i):
                es_primo[j] = False

    # Iteramos sobre los números desde el último primo encontrado hasta n*10 y agregamos los siguientes primos
    for i in range(primos[-1]+1, n*10):
        if es_primo[i]:
            primos.append(i)
            if len(primos) == n:
                break

    return primos[:n]

# Ejemplo de uso
n = 10
print("Los primeros", n, "números primos son:", primeros_n_primos(n))
