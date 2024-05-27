#Si la lista s siempre está ordenada de mayor a menor, podemos hacer menos iteraciones ya que en cuanto encontremos un elemento mayor o igual que x
#sabremos que los elementos restantes también serán mayores o iguales a x.
#Entonces, podemos modificar la función para que cuando encuentre el primer elemento mayor o igual que x
#Detenga el bucle y devuelva el contador en ese momento:

def contar_menores_que_ordenada(s, x):
    """
    Cuenta la cantidad de elementos de s que son menores que x, asumiendo que s está ordenada de mayor a menor.

    Argumentos:
    s: Una lista de números ordenada de mayor a menor.
    x: Un número decimal.

    Retorna:
    La cantidad de elementos de s que son menores que x.
    """
    contador = 0  # Inicializamos el contador de elementos menores que x

    # Iteramos sobre cada elemento de s
    for elemento in s:
        if elemento < x:
            contador += 1  # Incrementamos el contador si el elemento es menor que x
        else:
            break  # Detenemos el bucle si encontramos un elemento mayor o igual que x

    return contador

# Ejemplo de uso
numeros_ordenados = [5, 4, 3, 2, 1]
x = 3.5
print("La cantidad de elementos de la lista ordenada menores que", x, "es:", contar_menores_que_ordenada(numeros_ordenados, x))
