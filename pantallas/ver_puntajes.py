import pygame
from paquete_datos import *


def ver_puntajes():
    """
    # realiza: Pantalla para ver los 10 mejores puntajes

    # args: -

    """
    lista_scores = []

    with open("paquete_datos/Score.csv", "r", encoding = "utf-8") as archivo:
        for linea in archivo: 
            # Ej de linea: linea = "assasa, 17", cada linea se difiere si hay un salto de renglon
            partes = linea.strip().split(",") 
            #Ej luego de strip y split: partes = ["assasa", " 17"]

            # strip  elimina espacios en blanco al inifcio y final
            # slipt divide las cadenas cada vez que encuentra una
            # evita error por coma en nombre

            if len(partes) == 2:
                nombre = partes[0]

                try:
                    puntaje = int(partes[1])
                    lista_scores.append([nombre, puntaje]) 

                except:
                    pass  # si no es numero, pasa

    
    for i in range(len(lista_scores) - 1):
        for j in range(i + 1, len(lista_scores)):
            if lista_scores[j][1] > lista_scores[i][1]:
                aux = lista_scores[i]
                lista_scores[i] = lista_scores[j]
                lista_scores[j] = aux


    top10 = lista_scores[:10] # 10 primeros

    running = True

    while running:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False
                exit()

            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if boton_volver.collidepoint(evento.pos):
                    running = False 


        pantalla.fill(COLOR_FONDO_JUEGO)

        titulo = fuente_despedida.render("Top 10 Puntajes", True, COLOR_BLANCO)
        pantalla.blit(titulo, (ANCHO_VENTANA // 2 - titulo.get_width() // 2, 40))



        y__inicial_texto_ver_puntaje = 120
    
        for i in range(len(top10)):
            nombre = top10[i][0]
            puntaje = top10[i][1]
            texto = fuente_feedback.render(f"{i + 1}. {nombre} - {puntaje}", True, COLOR_BLANCO)
            pantalla.blit(texto, (100,  y__inicial_texto_ver_puntaje))
            y__inicial_texto_ver_puntaje += 40

        
        pygame.draw.rect(pantalla, COLOR_ROJO, boton_volver, border_radius = 10)
        texto_volver = fuente_feedback.render("Volver al menu", True, COLOR_BLANCO)
        x_texto_volver_al_menu = boton_volver.x + (boton_volver.width - texto_volver.get_width()) // 2
        y_texto_volver_al_menu = boton_volver.y + (boton_volver.height - texto_volver.get_height()) // 2
        pantalla.blit(texto_volver, (x_texto_volver_al_menu, y_texto_volver_al_menu))

        pygame.display.flip()
