import pygame 
import copy
from paquete_datos import *
from paquete_func.manejo_preguntas import *
from paquete_func.calcular_posicion import *
from paquete_func.informar_posicion import *
from paquete_func.guardar_si_no_se_hizo import *
from paquete_func.procesar_respuestas import *
from paquete_func.mostrar_temporizador import *
from paquete_func.manejo_csv import *



def jugar_partida(nombre_del_usuario):
    """
    # realiza: pantalla de juego

    # args:
         -> nombre_del_usuario. Nombre que eligio la persona al inicio de la aplicacion

    # return: vuelve al menu principal 

    """
    lista_preguntas_copia = copy.deepcopy(preguntas)
    pregunta_y_respuestas = elegir_pregunta_aleatoria(lista_preguntas_copia)
    tiempo_inicio_pregunta = pygame.time.get_ticks()
    
    mensaje_final = f"Gracias por jugar, {nombre_del_usuario}."
    posicion = 15
    estado_feedback = ""
    tiempo_feedback = 0
    flag_puntaje_guardado = False
    running = True


    while running:

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                flag_puntaje_guardado = guardar_si_no_se_hizo(flag_puntaje_guardado, nombre_del_usuario, posicion)
                running = False
                exit()


            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:

                # evita que responda muchas veces la misma pregunta mientras muestro feedback
                if estado_feedback != "":
                    continue # salta el resto del codigo del mismo bucle y vuelve a iniciar la prox iteracion

                if boton_salir.collidepoint(evento.pos):
                    mensaje_final = f"Saliste del juego {nombre_del_usuario}, quedaste en la posicion {posicion}"

                    flag_puntaje_guardado = guardar_si_no_se_hizo(flag_puntaje_guardado, nombre_del_usuario, posicion)
                    running = False

                    break



                for rect, letra in botones_respuesta:

                    if rect.collidepoint(evento.pos):

                        if letra == pregunta_y_respuestas["respuesta_correcta"]:
                            valor = True
                            sonido = sonido_correcto
                        else:
                            valor = False
                            sonido = sonido_incorrecto
                        
                        procesar = procesar_respuesta_correcta
                        estado_feedback, respuesta_correcta = procesar(valor, sonido)

                        posicion_previa = posicion
                        posicion = calcular_nueva_posicion(posicion, respuesta_correcta, tablero_valores)
                        mensaje_movimiento = informar_posicion(posicion_previa, posicion)


                        if posicion == PRIMERA_POSICION:
                            mensaje_final = f"Lo siento {nombre_del_usuario}, perdiste!"
                            flag_puntaje_guardado = guardar_si_no_se_hizo(flag_puntaje_guardado, nombre_del_usuario, posicion)
                            running = False


                        elif posicion == ULTIMA_POSICION:
                            mensaje_final = f"Felicitaciones {nombre_del_usuario}, ganaste!"
                            flag_puntaje_guardado = guardar_si_no_se_hizo(flag_puntaje_guardado, nombre_del_usuario, posicion)
                            running = False

                
                        tiempo_feedback = pygame.time.get_ticks()

                        break  # ya hizo clic, salimos del for

        # redibuja cada frame                    
        pantalla.fill(COLOR_FONDO_JUEGO) 
        pantalla.blit(imagen_tablero, (x_tablero, y_tablero))


        x_personaje = COORDENADA_X_DE_CADA_CASILLERO[posicion]
        y_personaje = y_tablero - 50  
        pantalla.blit(personaje_img, (x_personaje - personaje_img.get_width() // 2, y_personaje))


        """
        BUSQUEDA DE CENTRO DE CASILLA 15 Y ANCHO DE CASILLAS: 
        prueba = pygame.Rect(616, 490, 39, 121)
        pygame.draw.rect(pantalla, COLOR_BLANCO, prueba)
        """


        boton_salir = pygame.Rect(x_boton_salir, y_boton_salir, ancho_boton_salir, alto_boton_salir)
        pygame.draw.rect(pantalla, COLOR_ROJO, boton_salir, border_radius = 8)

        texto_salir = fuente_feedback.render("Salir", True, COLOR_BLANCO)
        x_texto_salir = boton_salir.x + (boton_salir.width - texto_salir.get_width()) // 2
        y_texto_salir = boton_salir.y + (boton_salir.height - texto_salir.get_height()) // 2
        pantalla.blit(texto_salir, (x_texto_salir, y_texto_salir))

        
        
        pregunta_rect = pygame.Rect(50, 20, pantalla.get_width() - 200, 150)
        pygame.draw.rect(pantalla, COLOR_NEGRO, pregunta_rect, border_radius = 10)

        texto_pregunta = fuente_pregunta_juego.render(pregunta_y_respuestas['pregunta'], True, COLOR_BLANCO)
        pantalla.blit(texto_pregunta, (pregunta_rect.x + 20, pregunta_rect.y + 20)) 



        respuestas = [
            ("a", pregunta_y_respuestas["respuesta_a"]),
            ("b", pregunta_y_respuestas["respuesta_b"]),
            ("c", pregunta_y_respuestas["respuesta_c"]),
        ]

        botones_respuesta = [] # se incluiran los rects de las respuestas

        for i in range(len(respuestas)):
            letra, texto_respuesta = respuestas[i]

            # calculo posicion vertical
            y_boton_opcion = y_primera_opcion + i * (alto_boton + espacio_entre_botones) 
            # i = 0 primero, 1 despues, despues 2
            # i = 0: 200 + 0   = 200
            # i = 1: 200 + 70  = 270
            # i = 2: 200 + 140 = 340


            rect_opciones = pygame.Rect(x_boton_opcion, y_boton_opcion, ancho_boton, alto_boton)
            botones_respuesta.append((rect_opciones, letra)) # guardo el rectangulo en botones_respuesta
            pygame.draw.rect(pantalla, COLOR_NEGRO, rect_opciones, border_radius = 8)
            
            texto_opcion = fuente_pregunta_juego.render(texto_respuesta, True, COLOR_BLANCO)
            pantalla.blit(texto_opcion, (rect_opciones.x + 15, rect_opciones.y + 15))



        mostrar_temporizador(tiempo_inicio_pregunta)
        
 
        # chequea si se agoto el tiempo de respuesta
        if estado_feedback == "":

            tiempo_actual = pygame.time.get_ticks()

            if tiempo_actual - tiempo_inicio_pregunta >= TIEMPO_LIMITE_PREGUNTA: 
                estado_feedback = "Incorrecta"
                respuesta_correcta = False
                posicion_previa = posicion
                posicion = calcular_nueva_posicion(posicion, respuesta_correcta, tablero_valores)
                mensaje_movimiento = informar_posicion(posicion_previa, posicion)
                tiempo_feedback = pygame.time.get_ticks()




        if estado_feedback != "":

            tiempo_actual = pygame.time.get_ticks()

            if tiempo_actual - tiempo_feedback < 1000: # si paso menos de 1 seg
                if estado_feedback == "Correcta":
                    texto_feedback = "Correcto! "
                    color_feedback = COLOR_VERDE

                else:
                    texto_feedback = "Incorrecto!"
                    color_feedback = COLOR_ROJO

                rect_feedback = pygame.Rect(x_boton_opcion + ancho_boton + 10, y_primera_opcion, 300, 110)
                pygame.draw.rect(pantalla, color_feedback, rect_feedback, border_radius = 5)

                # mensaje de correcto/incorrecto
                texto_correcto_incorrecto_render = fuente_feedback.render(texto_feedback, True, COLOR_BLANCO)
                pantalla.blit(texto_correcto_incorrecto_render, (rect_feedback.x + 10, rect_feedback.y + 15))
                # mensaje de movimiento 
                texto_casillas_a_mover = fuente_feedback.render(mensaje_movimiento, True, COLOR_BLANCO)
                pantalla.blit(texto_casillas_a_mover, (rect_feedback.x + 10, rect_feedback.y + 50))
            

            else:
                if pregunta_y_respuestas in lista_preguntas_copia:
                    lista_preguntas_copia.remove(pregunta_y_respuestas)  
                
                if len(lista_preguntas_copia) == 0:
                    mensaje_final = f"No hay mas preguntas {nombre_del_usuario}, quedaste en la posicion {posicion}"
                    flag_puntaje_guardado = guardar_si_no_se_hizo(flag_puntaje_guardado, nombre_del_usuario, posicion)
                    running = False

                else:
                    pregunta_y_respuestas = elegir_pregunta_aleatoria(lista_preguntas_copia)
                    tiempo_inicio_pregunta = pygame.time.get_ticks()


                estado_feedback = ""


        pygame.display.flip() # actualiza la pantalla
    

    pantalla.fill(COLOR_FONDO_JUEGO)

    texto_despedida = fuente_despedida.render(mensaje_final, True, COLOR_BLANCO)
    pantalla.blit(texto_despedida, (ANCHO_VENTANA // 2 - texto_despedida.get_width() // 2, ALTO_VENTANA // 2 - texto_despedida.get_height() // 2))

    pygame.display.flip()
    pygame.time.delay(3000) # espera unos segundos antes de volver al menu

    flag_puntaje_guardado = guardar_si_no_se_hizo(flag_puntaje_guardado, nombre_del_usuario, posicion)

    return # vuelve al menu