def cambiar_menores_que_x_por_cero(s, x):
    """
    Cambia todos los elementos menores que x por 0 en la lista s.

    Argumentos:
    s: Una lista de números.
    x: Un número decimal.

    Retorna:
    Esta función no devuelve nada explícitamente, ya que modifica la lista s directamente.
    """
    # Iteramos sobre cada elemento de la lista s
    for i in range(len(s)):
        if s[i] < x:
            s[i] = 0  # Cambiamos el elemento por 0 si es menor que x

# Ejemplo de uso
s = [1, 4.1, 6.3, 2, 3.2, 8]
x = 3
print("Lista original:", s)
cambiar_menores_que_x_por_cero(s, x)
print("Lista después del cambio:", s)
