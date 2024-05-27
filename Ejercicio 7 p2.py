def dondeAparece (lista, blanco):
    for i in range (len(lista)):
        if lista[i] == blanco:
            return i
    return -1

##Programa Principal
lista = [1, 2, 3, 4, 5, 2]
blanco = int(input ("Ingresar un valor de lista"))
print("El primer índice donde aparece", blanco, "en la lista es:", dondeAparece(lista, blanco))
