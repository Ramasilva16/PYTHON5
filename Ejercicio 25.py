def darPatentes(ruta):
    # Simulamos la función darPatentes
    if ruta == "Ruta Nacional 8":
        return ["ABC123", "DEF456", "GHI789", "JKL012"]
    else:
        return []

def controlVelocidad(patente):
    # Simulamos la función controlVelocidad
    # Devolvemos una velocidad aleatoria entre 80 y 120 km/h
    import random
    return random.randint(80, 120)

def reincidente(patente):
    # Simulamos la función reincidente
    # Devolvemos True para algunas patentes aleatorias
    import random
    return random.choice([True, False])

def costoActual():
    # Simulamos la función costoActual
    # Devolvemos un costo fijo
    return 100

def enviarMulta(patente, costo):
    # Simulamos la función enviarMulta
    print(f"Se ha enviado una multa al domicilio del propietario del automóvil con la patente {patente}, por un monto de ${costo}.")

def controlVehicular(ruta):
    patentes = darPatentes(ruta)
    for patente in patentes:
        velocidad = controlVelocidad(patente)
        if velocidad > 100:
            costo = costoActual()
            if reincidente(patente):
                costo *= 2
            enviarMulta(patente, costo)

# Realizar el control vehicular en la Ruta Nacional 8
ruta = "Ruta Nacional 8"
controlVehicular(ruta)
