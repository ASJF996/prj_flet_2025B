import pygame

class Vista:
    def __init__(self, modelo):
        self.modelo = modelo

    def dibujar(self):
        pantalla = self.modelo.pantalla
        if self.modelo.login.login_exitoso:
            fondo = self.modelo.fondos[self.modelo.escenarios[self.modelo.nivel_actual]]
            pantalla.blit(fondo, (0,0))
            self.modelo.jugador.dibujar(pantalla)
            for e in self.modelo.enemigos:
                e.dibujar(pantalla)
            for p in self.modelo.proyectiles:
                p.dibujar(pantalla)
            for p in self.modelo.enemigos_proyectiles:
                p.dibujar(pantalla)
            fuente = pygame.font.Font(None, 30)
            texto = fuente.render(f"Vidas: {self.modelo.jugador.vidas}  Puntaje: {self.modelo.puntaje}  Nivel: {self.modelo.nivel_actual+1}", True, (255,255,255))
            pantalla.blit(texto, (10,10))
        else:
            pantalla.fill((0,0,0))
            fuente = pygame.font.Font(None, 40)
            titulo = fuente.render("LOGIN", True, (255,255,255))
            pantalla.blit(titulo, (self.modelo.ancho//2 - 50, 100))

        pygame.display.flip()

    def mostrar_game_over(self):
        pantalla = self.modelo.pantalla
        fuente = pygame.font.Font(None, 60)
        texto = fuente.render("GAME OVER", True, (255,0,0))
        pantalla.blit(texto, (self.modelo.ancho//2 - 150, self.modelo.alto//2 - 30))
        pygame.display.flip()
