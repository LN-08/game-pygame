def calcular_nueva_posicion(posicion_actual, es_respuesta_correcta, tablero_valores):
    """

    """

    if es_respuesta_correcta:
        direccion = 1
    else:
        direccion = -1

    nueva_pos = posicion_actual + direccion


    while nueva_pos >= 0 and nueva_pos <= 30 and tablero_valores[nueva_pos] > 0:
        rebote = tablero_valores[nueva_pos]
        nueva_pos = nueva_pos + (rebote * direccion)


    if nueva_pos < 0:
        nueva_pos = 0
    elif nueva_pos > 30:
        nueva_pos = 30

    return nueva_pos
