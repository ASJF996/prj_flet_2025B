import pygame
from modelo import ModeloJuego

class ControladorJuego:
    def __init__(self, modelo):
        self.modelo = modelo
        self.corriendo = True
        self.tiempo_ultimo_disparo = 0
        self.tiempo_entre_disparos = 300

    def manejar_eventos(self):
        dx = dy = 0
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.corriendo = False

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            dx = -1
        elif teclas[pygame.K_RIGHT]:
            dx = 1
        if teclas[pygame.K_UP]:
            dy = -1
        elif teclas[pygame.K_DOWN]:
            dy = 1

        if not self.modelo.game_over:
            self.modelo.jugador.mover(dx, dy)

            # Disparo
            tiempo_actual = pygame.time.get_ticks()
            if teclas[pygame.K_SPACE] and (tiempo_actual - self.tiempo_ultimo_disparo > self.tiempo_entre_disparos):
                self.modelo.disparar()
                self.tiempo_ultimo_disparo = tiempo_actual

            # Cambiar escenario
            if teclas[pygame.K_e]:
                self.modelo.cambiar_escenario()
                pygame.time.wait(200)  # Evita múltiples cambios rápidos
        else:
            if teclas[pygame.K_r]:
                self.modelo.__init__()
