import random

def elegir_pregunta_aleatoria(lista_de_preguntas:list) -> dict:
    """
    # realiza: elige una pregunta random de la lista dada

    # args:
         -> lista_de_preguntas: lista

    # return: un diccionario, el cual es un elemento de la lista dada
            
    """
    if len(lista_de_preguntas) > 0:
        pregunta = random.choice(lista_de_preguntas)
    
    else:
        pregunta = "No quedan mas preguntas! D:"

    return pregunta
