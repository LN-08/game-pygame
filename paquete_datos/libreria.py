from .constantes import *

import pygame

pygame.init()

# Fuentes --------------------------------------

# Pedir Nombre
fuente_pedir_nombre = pygame.font.Font("fuentes/jJellycow.ttf", 170)
fuente_escribir_nombre = pygame.font.Font("fuentes/jJellycow.ttf", 100)

# Menu
fuente_titulo = pygame.font.SysFont("Century Gothic", 50)
fuente_botones = pygame.font.SysFont("Century Gothic", 25)
fuente_titulo_menu = pygame.font.Font("fuentes/FriendlyStranger.ttf", 40)


# Juego
fuente_pregunta_juego = pygame.font.SysFont("fuentes/ToastyMilk.ttf", 35)
fuente_despedida = pygame.font.Font("fuentes/jJellycow.ttf", 60)
fuente_feedback = pygame.font.SysFont("fuentes/ToastyMilk.ttf", 30)

fuente_seguir = pygame.font.SysFont("fuentes/ToastyMilk.ttf", 35)



# Pantallas --------------------------------------

pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

# titulo
pygame.display.set_caption("Serpientes y Escaleras")

wallpaper_escribir_nombre = pygame.image.load("img/fondos/fondo_nombre.jpg")
screen_escribir_nombre = pygame.transform.scale(wallpaper_escribir_nombre, (ANCHO_VENTANA, ALTO_VENTANA))

wallpaper_menu = pygame.image.load("img/fondos/fondo_menu.jpeg")
screen_menu = pygame.transform.scale(wallpaper_menu, (ANCHO_VENTANA, ALTO_VENTANA))


boton_jugar = pygame.image.load("img/botones_menu/jugar.png")
boton_ver_puntaje = pygame.image.load("img/botones_menu/ver_puntaje.png")
boton_exit = pygame.image.load("img/botones_menu/exit.png")

titulo_menu = fuente_titulo_menu.render("SERPIENTES Y ESCALERAS", True, COLOR_NEGRO)



# Rects ---------------
# Menu
rect_jugar = boton_jugar.get_rect(topleft = (200, 250)) # creo su rect invisible

rect_boton_ver_puntaje = boton_ver_puntaje.get_rect(topleft = (200, 350))

rect_exit = boton_exit.get_rect(topleft = (200, 450))



# Juego
# Botones opciones
ancho_boton = pantalla.get_width() - 800
alto_boton = 60
espacio_entre_botones = 10
x_boton_opcion = 100
y_primera_opcion = 200


