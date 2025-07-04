def procesar_respuesta_correcta(valor:bool, sonido:any):
    """
    # realiza: devuelve Correcto o Incorrecto segun cosrresponda, y un sonido

    # args:
         -> valor: valor de la respuesta, True si fue correcta, False si no lo fue
         -> sonido: un sonido para una respuesta correcta o incorrecta

    # return: un string y un booleano que indica si la respuesta fue correcta

    """
    if valor:
        str = "Correcta"
    else:
        str = "Incorrecta"

    sonido.play()
    return str, valor
