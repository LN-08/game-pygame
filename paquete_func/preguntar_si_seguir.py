import pygame
from paquete_datos import *

def preguntar_si_seguir():
    pregunta = fuente_seguir.render("¿Queres seguir jugando?", True, COLOR_BLANCO)

    ancho_boton = 120
    alto_boton = 50
    espacio_entre_botones = 40

    # calcular posicion centrada de los botones
    ancho_total_botones = ancho_boton * 2 + espacio_entre_botones
    x_inicio_botones = (ANCHO_VENTANA - ancho_total_botones) // 2
    y_boton = 300

    boton_si = pygame.Rect(x_inicio_botones, y_boton, ancho_boton, alto_boton)
    boton_no = pygame.Rect(x_inicio_botones + ancho_boton + espacio_entre_botones, y_boton, ancho_boton, alto_boton)

    texto_si = fuente_seguir.render("SI", True, COLOR_BLANCO)
    texto_no = fuente_seguir.render("NO", True, COLOR_BLANCO)


    respuesta = None

    running = True

    while running:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = evento.pos

                if boton_si.collidepoint(mouse_x, mouse_y):
                    respuesta = True
                    running = False

                elif boton_no.collidepoint(mouse_x, mouse_y):
                    respuesta = False
                    running = False

        pantalla.fill(COLOR_FONDO_JUEGO)


        pantalla.blit(pregunta, (ANCHO_VENTANA // 2 - pregunta.get_width() // 2, 200))

        pygame.draw.rect(pantalla, COLOR_VERDE, boton_si, border_radius = 8)
        texto_si_rect = texto_si.get_rect(center=boton_si.center)
        pantalla.blit(texto_si, texto_si_rect)

        pygame.draw.rect(pantalla, COLOR_ROJO, boton_no, border_radius = 8)
        texto_no_rect = texto_no.get_rect(center=boton_no.center)
        pantalla.blit(texto_no, texto_no_rect)

        pygame.display.flip()
    
    return respuesta 
