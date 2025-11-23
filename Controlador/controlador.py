import pygame
from Modelos.Modelojuego import ModeloJuego
from Vista.vista import Vista
from Modelos.modelologin import Login 

class Controlador:
    def __init__(self, pantalla, usuario=None):
        self.pantalla = pantalla
        self.modelo = ModeloJuego(pantalla)
        if usuario:
            self.modelo.usuario_actual = usuario
            self.modelo.login.login_exitoso = True
            self.modelo.login.usuario_logueado = usuario
        self.vista = Vista(self.modelo)

    def iniciar(self):
        reloj = pygame.time.Clock()
        corriendo = True

        while corriendo:
            self.vista.dibujar()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    corriendo = False

                elif evento.type == pygame.KEYDOWN:

                    if evento.key == pygame.K_ESCAPE:
                        corriendo = False

                    if not self.modelo.login.login_exitoso:
                        self.modelo.login.procesar_tecla(evento.key)

                    else:
                        if evento.key == pygame.K_SPACE:
                            self.modelo.disparar()

                        elif evento.key == pygame.K_r and self.modelo.game_over:
                            self.modelo.reiniciar()

            if self.modelo.login.login_exitoso and not self.modelo.game_over:
                teclas = pygame.key.get_pressed()
                dx, dy = 0,0
                if teclas[pygame.K_LEFT]:
                    dx = -1
                if teclas[pygame.K_RIGHT]:
                    dx = 1
                if teclas[pygame.K_UP]:
                    dy = -1
                if teclas[pygame.K_DOWN]:
                    dy = 1
                self.modelo.jugador.mover(dx, dy, self.modelo.ancho, self.modelo.alto)
                self.modelo.actualizar()
            
            if self.modelo.game_over:
                self.vista.mostrar_game_over()

            reloj.tick(60)
