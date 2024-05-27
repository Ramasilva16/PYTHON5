def intercambiar(s, a, b):
    """
    Intercambia los elementos ubicados en las posiciones a y b de la lista s.

    Argumentos:
    s: Una lista de números.
    a: Un entero positivo que representa la primera posición a intercambiar.
    b: Un entero positivo que representa la segunda posición a intercambiar.

    Retorna:
    Esta función no devuelve nada explícitamente, ya que modifica la lista s directamente.
    """
    # Verificamos si los índices a y b son válidos
    if a < 0 or b < 0 or a >= len(s) or b >= len(s):
        print("Los índices a y b deben ser positivos y menores que la longitud de la lista.")
        return

    # Intercambiamos los elementos ubicados en las posiciones a y b
    s[a], s[b] = s[b], s[a]

# Ejemplo de uso
numeros = [1, 2, 3, 4, 5]
a = 1
b = 3
print("Lista original:", numeros)
intercambiar(numeros, a, b)
print("Lista después del intercambio:", numeros)

