from paquete_datos import * # busca init dentro de paquete_datos
from paquete_func.configurar_musica import *
from pantallas.pantalla_ingreso_nombre import *
from pantallas.jugar_partida import *
from pantallas.ver_puntajes import *

import pygame

pygame.init()

configurar_musica()

nombre_usuario = pantalla_ingreso_nombre()

running_prog = True
 
while running_prog:
    lista_eventos = pygame.event.get()

    pantalla.blit(screen_menu, (0, 0))
    pantalla.blit(titulo_menu, (100, 80)) 

    # rects de botones
    pygame.draw.rect(pantalla, COLOR_BOTONES , rect_jugar)
    texto_jugar = fuente_botones.render("JUGAR", True, COLOR_BLANCO)
    pantalla.blit(texto_jugar, texto_jugar.get_rect(center = rect_jugar.center))

    pygame.draw.rect(pantalla, COLOR_BOTONES , rect_boton_ver_puntaje)
    texto_puntaje = fuente_botones.render("VER PUNTAJE", True, COLOR_BLANCO)
    pantalla.blit(texto_puntaje, texto_puntaje.get_rect(center = rect_boton_ver_puntaje.center))

    pygame.draw.rect(pantalla, COLOR_BOTONES , rect_exit)
    texto_exit = fuente_botones.render("EXIT", True, COLOR_BLANCO)
    pantalla.blit(texto_exit, texto_exit.get_rect(center = rect_exit.center))


    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 :
            # rect_jugar, rec_boton_ver_puntaje y rect_exit estan creados en libreria
            
            if pygame.Rect.collidepoint(rect_jugar, evento.pos): #evento.pos = tupla de mi mouse en este momento
                jugar_partida(nombre_usuario)

            elif pygame.Rect.collidepoint(rect_boton_ver_puntaje, evento.pos):
                ver_puntajes()

            elif pygame.Rect.collidepoint(rect_exit, evento.pos):
                running_prog = False
                        

    pygame.display.flip()