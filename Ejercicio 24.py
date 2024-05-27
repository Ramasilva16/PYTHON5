def cobertura(cliente):
    # Simulamos la función cobertura
    if cliente == "123456":
        return "Oro"
    else:
        return "Plata"

def usados(cliente):
    # Simulamos la función usados
    if cliente == "123456":
        return 2
    else:
        return 6

def radioDeCobertura(cliente, localidad):
    # Simulamos la función radioDeCobertura
    if cliente == "123456" and localidad == "Buenos Aires":
        return True
    else:
        return False

def pagara(cliente, localidad):
    tipo_cobertura = cobertura(cliente)
    usos_cliente = usados(cliente)
    esta_en_radio_cobertura = radioDeCobertura(cliente, localidad)

    if tipo_cobertura == "Oro" or (tipo_cobertura == "Plata" and usos_cliente < 5 and esta_en_radio_cobertura):
        costo_servicio = 0
    elif tipo_cobertura == "Plata" and usos_cliente >= 5 and esta_en_radio_cobertura:
        costo_servicio = 50
    else:
        costo_servicio = 30

    return costo_servicio

# Ejemplo de uso
cliente = "123456"
localidad = "Buenos Aires"
costo = pagara(cliente, localidad)
print(f"El costo del servicio para el cliente {cliente} en la localidad {localidad} es de ${costo}.")
