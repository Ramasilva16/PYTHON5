def mostrarEnUnaLinea(lista):
    """
    Muestra todos los elementos de la lista en una línea separados por espacios.

    Argumentos:
    lista: Lista de enteros.
    """
    # Usar un bucle para recorrer la lista e imprimir cada elemento
    for elemento in lista:
        print(elemento, end=" ")  # Usar end=" " para imprimir un espacio en lugar de una nueva línea al final

# Ejemplo de uso
numeros = [1, 2, 3, 4, 5]
print("Lista de números:")
mostrarEnUnaLinea(numeros)