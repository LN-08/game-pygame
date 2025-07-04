from .constantes import *

import pygame

pygame.init()


pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Serpientes y Escaleras")




# Fuentes --------------------------------------

# Pedir Nombre |||||||||||||||||||||||||
fuente_pedir_nombre = pygame.font.Font("fuentes/jJellycow.ttf", 120)
fuente_escribir_nombre = pygame.font.Font("fuentes/jJellycow.ttf", 80)

# Menu |||||||||||||||||||||||||
fuente_botones = pygame.font.Font("fuentes/FriendlyStranger.ttf", 25)
fuente_titulo_menu = pygame.font.Font("fuentes/FriendlyStranger.ttf", 50)

# Juego |||||||||||||||||||||||||
fuente_pregunta_juego = pygame.font.SysFont("fuentes/ToastyMilk.ttf", 35)
fuente_despedida = pygame.font.Font("fuentes/jJellycow.ttf", 50)
fuente_feedback = pygame.font.SysFont("fuentes/ToastyMilk.ttf", 30)
fuente_seguir = pygame.font.SysFont("fuentes/ToastyMilk.ttf", 35)





# Pantallas --------------------------------------

# Escribir nombre |||||||||||||||||||||||||
wallpaper_escribir_nombre = pygame.image.load("img/fondos/fondo_nombre_serpiente.jpg")
screen_escribir_nombre = pygame.transform.scale(wallpaper_escribir_nombre, (ANCHO_VENTANA, ALTO_VENTANA))


# Menu |||||||||||||||||||||||||
titulo_menu = fuente_titulo_menu.render("SERPIENTES Y ESCALERAS", True, COLOR_TITULO_MENU)
wallpaper_menu = pygame.image.load("img/fondos/fondo_menu.jpeg")
screen_menu = pygame.transform.scale(wallpaper_menu, (ANCHO_VENTANA, ALTO_VENTANA))







# Rects --------------------------------------------------------------------------------
# Menu |||||||||||||||||||||||||
# Botones del menu
rect_jugar = pygame.Rect(180, 250, 250, 60)
rect_boton_ver_puntaje = pygame.Rect(180, 350, 250, 60)
rect_exit = pygame.Rect(180, 450, 250, 60)

# Juego |||||||||||||||||||||||||
# Botones opciones
ancho_boton = pantalla.get_width() - 800
alto_boton = 60
espacio_entre_botones = 10
x_boton_opcion = 100
y_primera_opcion = 200

# Boton salir
ancho_boton_salir = 150
alto_boton_salir = 50
x_boton_salir = ANCHO_VENTANA - ancho_boton_salir - 180
y_boton_salir = 180



# Ver puntajes |||||||||||||||||||||||||
# Boton volver Ver puntajes
ancho_boton_volver = 200
alto_boton_volver = 50
x_boton_volver = ANCHO_VENTANA // 2 - ancho_boton // 2
y_boton_volver = ALTO_VENTANA - 100
boton_volver = pygame.Rect(x_boton_volver, y_boton_volver, ancho_boton, alto_boton)

# var en ver puntajes
y__inicial_texto_ver_puntaje = 120




# PANTALLA JUEGO --------------------------------------------------------------------------------
# tablero |||||||||||||||||||||||||
imagen_tablero = pygame.image.load("img/mapa/tablero.png")
tablero_img = pygame.transform.scale(imagen_tablero, (ANCHO_TABLERO, ALTO_TABLERO))

x_tablero = 0
y_tablero = ALTO_VENTANA - ALTO_TABLERO

pantalla.blit(tablero_img, (x_tablero, y_tablero))


# personaje |||||||||||||||||||||||||
personaje_img = pygame.image.load("img/personaje/flecha.png")
personaje_img = pygame.transform.scale(personaje_img, (45, 45))


# feedback |||||||||||||||||||||||||
estado_feedback = ""
tiempo_feedback = 0








# Timer --------------------------------------------------------------------------------
# Juego |||||||||||||||||||||||||
x_timer = pantalla.get_width() - 300
y_timer = 300
ancho_timer = 120
alto_timer = 50






# Sonidos --------------------------------------------------------------------------------
# Juego |||||||||||||||||||||||||
sonido_correcto = pygame.mixer.Sound("sonidos/respuesta_correcta.wav")
sonido_correcto.set_volume(0.2)

sonido_incorrecto = pygame.mixer.Sound("sonidos/respuesta_incorrecta.wav")
sonido_incorrecto.set_volume(0.2)



