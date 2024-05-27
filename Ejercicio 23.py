def contar_letras(cadena):
    # Creamos un diccionario para almacenar la cantidad de veces que aparece cada letra
    contador_letras = {}

    # Recorremos cada letra en la cadena
    for letra in cadena:
        # Ignoramos los espacios en blanco
        if letra != ' ':
            # Añadimos la letra al diccionario si no está presente y establecemos su contador a 0
            contador_letras.setdefault(letra, 0)
            # Incrementamos el contador de la letra actual
            contador_letras[letra] += 1

    # Mostramos el resultado visualmente con asteriscos
    print("Cantidad de veces que aparece cada letra:")
    for letra, cantidad in contador_letras.items():
        print(f"{letra} :", '*' * cantidad)


# Pedimos al usuario que ingrese una cadena
cadena = input("Por favor, ingresa una cadena: ")

# Llamamos a la función contar_letras con la cadena ingresada
contar_letras(cadena)
