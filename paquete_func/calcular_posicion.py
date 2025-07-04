def calcular_nueva_posicion(posicion_actual:int, es_respuesta_correcta:bool, tablero_valores:list) -> int:
    """
    # realiza: calcula la nueva posicion del jugador

    # args:
         -> posicion_actual: describe la posicion previa a los movimientos correspondientes
         -> es_respuesta_correcta: describe si la respuesta es correcta
         -> tablero_valores: una lista que describe los saltos extras en el tablero

    # return: la nueva posicion luego de los movimientos correspondientes         
    """

    if es_respuesta_correcta:
        direccion = 1
    else:
        direccion = -1

    nueva_pos = posicion_actual + direccion

    while nueva_pos >= 0 and nueva_pos <= 30 and tablero_valores[nueva_pos] > 0:
        rebote = tablero_valores[nueva_pos]
        nueva_pos = nueva_pos + (rebote * direccion)

    return nueva_pos
