# Lista inicial
animales = ['elefante', 'jirafa', 'mono']

# Pedir al usuario que ingrese un nuevo animal
nuevo_animal = input("Ingresa el nombre de otro animal: ")

# Agregar el nuevo animal a la lista
animales.append(nuevo_animal)

# Imprimir todos los animales de la lista
print("Lista de animales:")
for animal in animales:
    print(animal)

# Imprimir el cuarto animal de la lista
if len(animales) >= 4:
    cuarto_animal = animales[3]
    print("El cuarto animal de la lista es:", cuarto_animal)
else:
    print("La lista no tiene suficientes animales para mostrar el cuarto.")