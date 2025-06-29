from paquete_datos import * # busca init dentro de paquete_datos
from pantallas import *
from pantallas.pantalla_ingreso_nombre import *
from pantallas.jugar_partida import *

import pygame

pygame.init()

nombre_usuario = pantalla_ingreso_nombre()

running_prog = True
 
while running_prog:
    lista_eventos = pygame.event.get()
    mouse_pos = pygame.mouse.get_pos()

    pantalla.blit(screen_menu, (0, 0))
    # dibuja la imagen desde la esquina superior izquierda

    pantalla.blit(titulo_menu, (100, 100)) 
    # Muestro el titulo

    # Muestro los botones
    pantalla.blit(boton_jugar, (200, 250)) 
    pantalla.blit(boton_ver_puntaje, (200, 350))
    pantalla.blit(boton_exit, (200, 450))

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 :
            # rect_jugar, rec_boton_ver_puntaje y rect_exit estan creados en libreria
            
            if pygame.Rect.collidepoint(rect_jugar, evento.pos): #evento.pos = tupla de mi mouse en este momento
                jugar_partida()

            elif pygame.Rect.collidepoint(rect_boton_ver_puntaje, evento.pos):
                print("puntaje")

            elif pygame.Rect.collidepoint(rect_exit, evento.pos):
                running_prog = False
                        

    pygame.display.flip()