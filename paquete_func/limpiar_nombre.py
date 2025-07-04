def limpiar_nombre(nombre: str) -> str:
    """"
    # realiza: Elimina caracteres que puede poner en peligro el correcto funcionamiento del csv

    # args:
            -> nombre: nombre del usuario
    
    # return:
            el nombre de usuario dado, pero reemplazando los (, ; |) por guiones bajo
    """
    nombre = nombre.replace(",", "_").replace(";", "_").replace("|", "_")
    
    return nombre
