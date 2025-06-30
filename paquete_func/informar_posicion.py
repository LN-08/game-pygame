def informar_posicion(posicion_inicial, posicion_final):
    """
    
    """
    diferencia = posicion_final - posicion_inicial
    mensaje = ""

    if diferencia > 1:
        mensaje = f"Subiste {diferencia} casilleros"

    elif diferencia == 1:
        mensaje = "Subiste 1 casillero"

    elif diferencia == 0:
        mensaje = "No te moviste"

    elif diferencia == -1:
        mensaje = "Bajaste 1 casillero"

    elif diferencia < -1:
        mensaje = f"Bajaste {diferencia * -1} casilleros"

    return mensaje
