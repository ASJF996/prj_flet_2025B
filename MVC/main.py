import pygame
from controlador import Controlador
import sys

def main(usuario=None):
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Juego MVC")
    controlador = Controlador(pantalla, usuario=usuario)
    controlador.iniciar()
    pygame.quit()

if __name__ == "__main__":
    usuario = None
    if len(sys.argv) > 1:
        usuario = sys.argv[1]  # recibe el usuario desde Flet si se quiere
    main(usuario)
