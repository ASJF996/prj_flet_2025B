import pygame
import os

class VistaJuego:
    def __init__(self, modelo):
        self.modelo = modelo
        self.pantalla = pygame.display.set_mode((modelo.ancho, modelo.alto))
        pygame.display.set_caption("Juego MVC con Escenarios en JPG")
        self.fuente = pygame.font.SysFont(None, 36)

        # Cargar imágenes JPG de fondo
        base = os.path.join(os.path.dirname(__file__), "assets")

        # Se pueden nombrar igual que los escenarios definidos en modelo.escenarios
        self.fondos = {}
        for nombre in self.modelo.escenarios:
            ruta = os.path.join(base, f"fondo_{nombre}.jpg")
            if os.path.exists(ruta):
                imagen = pygame.image.load(ruta).convert()
                imagen = pygame.transform.scale(imagen, (self.modelo.ancho, self.modelo.alto))
                self.fondos[nombre] = imagen
            else:
                print(f"⚠️ No se encontró la imagen: {ruta}")

    def dibujar(self):
        escenario = self.modelo.escenarios[self.modelo.escenario_index]
        fondo = self.fondos.get(escenario)

        if fondo:
            self.pantalla.blit(fondo, (0, 0))
        else:
            self.pantalla.fill((0, 0, 0))  # color de respaldo si no hay imagen

        # Dibujar jugador
        jugador = self.modelo.jugador
        pygame.draw.rect(self.pantalla, jugador.color,
                         (jugador.x, jugador.y, jugador.ancho, jugador.alto))

        # Dibujar enemigos
        for enemigo in self.modelo.enemigos:
            pygame.draw.rect(self.pantalla, enemigo.color,
                             (enemigo.x, enemigo.y, enemigo.ancho, enemigo.alto))

        # Dibujar proyectiles
        for p in self.modelo.proyectiles:
            pygame.draw.rect(self.pantalla, p.color,
                             (p.x, p.y, p.ancho, p.alto))

        # Mostrar puntaje y escenario actual
        texto = self.fuente.render(f"Puntaje: {self.modelo.puntaje}", True, (255, 255, 255))
        self.pantalla.blit(texto, (10, 10))
        texto2 = self.fuente.render(f"Escenario: {escenario}", True, (255, 255, 255))
        self.pantalla.blit(texto2, (10, 40))

        # Mensaje de Game Over
        if self.modelo.game_over:
            fuente_grande = pygame.font.SysFont(None, 72)
            texto = fuente_grande.render("GAME OVER", True, (255, 0, 0))
            rect = texto.get_rect(center=(self.modelo.ancho // 2, self.modelo.alto // 2))
            self.pantalla.blit(texto, rect)
            texto2 = self.fuente.render("Presiona R para reiniciar", True, (255, 255, 255))
            rect2 = texto2.get_rect(center=(self.modelo.ancho // 2, self.modelo.alto // 2 + 50))
            self.pantalla.blit(texto2, rect2)

        pygame.display.flip()
