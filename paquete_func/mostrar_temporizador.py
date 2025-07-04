import pygame
from paquete_datos import *

def mostrar_temporizador(tiempo_inicio_pregunta: int):
    """
    # realiza: Muestra el tiempo restante para responder las preguntas

    # args:
            -> tiempo_inicio_pregunta: momento donde se mostro la pregunta
    """
    tiempo_actual = pygame.time.get_ticks()
    tiempo_restante_ms = TIEMPO_LIMITE_PREGUNTA - (tiempo_actual - tiempo_inicio_pregunta)
                                                # (tiempo que ya paso desde que se mostro la pregunta)
    tiempo_restante = tiempo_restante_ms // 1000

    if tiempo_restante < 0:
        tiempo_restante = 0


    rect_timer = pygame.Rect(x_timer, y_timer, ancho_timer, alto_timer)
    pygame.draw.rect(pantalla, COLOR_NEGRO, rect_timer, border_radius = 10)

    # pas a color rojo si quedan menos de 5s
    if tiempo_restante <= 5:
        color_timer = COLOR_ROJO
    else:
        color_timer = COLOR_VERDE

    texto_timer = fuente_feedback.render(f"Tiempo: {tiempo_restante}", True, color_timer)

    # centrado de texto 
    texto_x = rect_timer.x + (rect_timer.width - texto_timer.get_width()) // 2
    texto_y = rect_timer.y + (rect_timer.height - texto_timer.get_height()) // 2

    pantalla.blit(texto_timer, (texto_x, texto_y))