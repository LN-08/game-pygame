import pygame 
import copy
from paquete_datos import *
from paquete_func.manejo_preguntas import *
from paquete_func.preguntar_si_seguir import *
from paquete_func.calcular_posicion import *
from paquete_func.informar_posicion import *


def jugar_partida():
    """
    """

    lista_preguntas_copia = copy.deepcopy(preguntas)

    pregunta_y_respuestas = elegir_pregunta_aleatoria(lista_preguntas_copia)
    
    posicion = 15

    estado_feedback = ""
    tiempo_feedback = 0

    running = True
    
    while running:
    
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = evento.pos


                for rect, letra in botones_respuesta:
                    if rect.collidepoint(mouse_x, mouse_y):

                        if letra == pregunta_y_respuestas["respuesta_correcta"]:
                            estado_feedback = "Correcta"
                            respuesta_correcta = True

                        else:
                            estado_feedback = "Incorrecta" 
                            respuesta_correcta = False    


                        posicion_previa = posicion

                        posicion = calcular_nueva_posicion(posicion, respuesta_correcta, tablero_valores)

                        mensaje_movimiento = informar_posicion(posicion_previa, posicion)

                    
                        tiempo_feedback = pygame.time.get_ticks()

                        break  # ya hizo clic, salimos del for

                          
            
        pantalla.fill(COLOR_FONDO_JUEGO)
        

        pregunta_rect = pygame.Rect(50, 20, pantalla.get_width() - 200, 150)
        pygame.draw.rect(pantalla, COLOR_NEGRO, pregunta_rect, border_radius = 10)

        texto_pregunta = fuente_pregunta_juego.render(pregunta_y_respuestas['pregunta'], True, COLOR_BLANCO)
        pantalla.blit(texto_pregunta, (pregunta_rect.x + 20, pregunta_rect.y + 20)) 


        # area de opciones (abajo de la pregunta)
        respuestas = [
            ("a", pregunta_y_respuestas["respuesta_a"]),
            ("b", pregunta_y_respuestas["respuesta_b"]),
            ("c", pregunta_y_respuestas["respuesta_c"]),
        ]

        botones_respuesta = [] # lista para incluir rects de las respuestas

        for i in range(len(respuestas)):
            letra, texto_respuesta = respuestas[i]

            # calculo posicion vertical
            y_boton_opcion = y_primera_opcion + i * (alto_boton + espacio_entre_botones) 
            # i = 0 primero, 1 despues, despues 2
            #i = 0: 200 + 0   = 200
            #i = 1: 200 + 70  = 270
            #i = 2: 200 + 140 = 340

            # creo el rect del boton
            rect_opciones = pygame.Rect(x_boton_opcion, y_boton_opcion, ancho_boton, alto_boton)

            # guardo el rectangulo en botones_respuesta
            botones_respuesta.append((rect_opciones, letra))


            pygame.draw.rect(pantalla, COLOR_NEGRO, rect_opciones, border_radius = 8)
            
            texto_opcion = fuente_pregunta_juego.render(texto_respuesta, True, COLOR_BLANCO)

            pantalla.blit(texto_opcion, (rect_opciones.x + 15, rect_opciones.y + 15))




        if estado_feedback != "":

            tiempo_actual = pygame.time.get_ticks()

            if tiempo_actual - tiempo_feedback < 1000:
                # mostrar cartel por 1 seg
                if estado_feedback == "Correcta":
                    texto_feedback = "Correcto! "
                    color_feedback = COLOR_VERDE

                else:
                    texto_feedback = "Incorrecto!"
                    color_feedback = COLOR_ROJO

                rect_feedback = pygame.Rect(x_boton_opcion + ancho_boton + 10, y_primera_opcion, 300, 110)
                pygame.draw.rect(pantalla, color_feedback, rect_feedback, border_radius = 5)


                # mensaje de correcto/incorrecto
                texto_render = fuente_feedback.render(texto_feedback, True, COLOR_BLANCO)
                pantalla.blit(texto_render, (rect_feedback.x + 10, rect_feedback.y + 15))

                # mensaje de movimiento 
                texto_casillas_extra = fuente_feedback.render(mensaje_movimiento, True, COLOR_BLANCO)
                pantalla.blit(texto_casillas_extra, (rect_feedback.x + 10, rect_feedback.y + 50))
            
            else:
               
                if pregunta_y_respuestas in lista_preguntas_copia:
                    lista_preguntas_copia.remove(pregunta_y_respuestas)  
                
                if len(lista_preguntas_copia) == 0:
                    running = False

                else:
                    seguir = preguntar_si_seguir()

                    if seguir:
                        pregunta_y_respuestas = elegir_pregunta_aleatoria(lista_preguntas_copia)
                        
                    else:
                        running = False

                estado_feedback = ""

        pygame.display.flip()
    

    pantalla.fill(COLOR_FONDO_JUEGO)

    texto = fuente_despedida.render('Gracias por jugar! Volviendo al menu ...', True, COLOR_BLANCO)

    pantalla.blit(texto, (ANCHO_VENTANA // 2 - texto.get_width() // 2, ALTO_VENTANA // 2 - texto.get_height() // 2))
    pygame.display.flip()

    # espera unos segundos antes de volver al menu
    pygame.time.delay(3000)
    
    return # vuelve al menu