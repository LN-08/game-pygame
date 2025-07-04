def guardar_datos_csv(ruta_archivo: str, datos: list) -> str:
    """
    # realiza: guarda los datos del user en el csv

    # args:
         -> ruta_archivo: Ruta del csv
         -> datos: Lista con nombre y puntaje

    # return: una cadena vacia si todo sale bien, y si hubo un error, el mensaje como texto
            
    """
    ret = ""

    try:
        with open(ruta_archivo, 'a', encoding = 'utf-8') as file:
            file.write(str(datos[0]) + ", " + str(datos[1]) + "\n")

    except Exception as exc:
        ret = str(exc)

    return ret