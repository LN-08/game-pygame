from paquete_func.manejo_csv import *
from paquete_func.limpiar_nombre import *

def guardar_si_no_se_hizo(flag:bool, user:str, pos:int) -> bool:
    """
    # realiza: 

    # args:
            -> flag: indica si ya se habia hecho un guardado
            -> user: nombre del usuario
            -> pos: posicion del usuario
    """
    flag_confirmado = False
    
    if not flag:
        user_limpio = limpiar_nombre(user)
        guardar_datos_csv("paquete_datos/Score.csv", [user_limpio, pos])
        flag_confirmado = True

    return flag_confirmado