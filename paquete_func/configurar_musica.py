import pygame

def configurar_musica():
    """
    # realiza: hace las configuraciones de musica

    # args: -     
    """
    pygame.mixer.music.load("sonidos/background.mp3")
    pygame.mixer.music.set_volume(0.1)  # volumen entre 0.0 y 1.0
    pygame.mixer.music.play(-1)  # -1 para que se repita indefinidamente
