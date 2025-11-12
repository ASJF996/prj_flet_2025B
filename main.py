import pygame
from modelo import ModeloJuego
from vista import VistaJuego
from controlador import ControladorJuego

def main():
    pygame.init()
    modelo = ModeloJuego()
    vista = VistaJuego(modelo)
    controlador = ControladorJuego(modelo)
    reloj = pygame.time.Clock()

    while controlador.corriendo:
        controlador.manejar_eventos()
        modelo.actualizar()
        vista.dibujar()
        reloj.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
