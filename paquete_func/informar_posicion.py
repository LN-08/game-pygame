def informar_posicion(posicion_inicial: int, posicion_final:int) -> str:
    """
    # realiza: Informa cuantos casilleros se movio

    # args:
            -> posicion_inicial: indica la posicion previa al movimiento
            -> posicio_final: indica la posicion leugo del movimiento
    
    # return:
            un string indicando cuantos casilleros se movio
    """
    diferencia = posicion_final - posicion_inicial
    mensaje = ""

    if diferencia > 1:
        mensaje = f"Subiste {diferencia} casilleros"

    elif diferencia == 1:
        mensaje = "Subiste 1 casillero"

    elif diferencia == -1:
        mensaje = "Bajaste 1 casillero"

    elif diferencia < -1:
        mensaje = f"Bajaste {diferencia * -1} casilleros"

    return mensaje
