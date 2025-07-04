from paquete_datos import *

import pygame

pygame.init()


def pantalla_ingreso_nombre() -> str:
    """
    # realiza: carga la pantalla para ingresar tu nombre

    # args: -
         
    # return: el nombre de usuario
    """
    nombre_usuario = ""
    running = True

    while running:
        lista_eventos = pygame.event.get()

        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    running = False

                elif evento.key == pygame.K_BACKSPACE:
                    nombre_usuario = nombre_usuario[:-1]

                else:
                    nombre_usuario += evento.unicode

        pantalla.blit(screen_escribir_nombre, (0, 0))


        titulo = fuente_pedir_nombre.render("Ingresa tu nombre:", True, COLOR_BLANCO)
        pantalla.blit(titulo, (100, 100))

        # muestra lo q va escribiendo
        texto_nombre = fuente_escribir_nombre.render(nombre_usuario, True, COLOR_BLANCO)
        pantalla.blit(texto_nombre, (100, 300))

        pygame.display.flip()

    return nombre_usuario
