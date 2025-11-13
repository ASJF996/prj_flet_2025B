import pygame
import os

class VistaJuego:
    def __init__(self, modelo):
        self.modelo = modelo
        self.pantalla = pygame.display.set_mode((modelo.ancho, modelo.alto))
        pygame.display.set_caption("Juego MVC con Naves 🚀")
        self.fuente = pygame.font.SysFont(None, 36)

        base = os.path.join(os.path.dirname(__file__), "assets")

        # Cargar imágenes de fondo
        self.fondos = {}
        for nombre in self.modelo.escenarios:
            ruta = os.path.join(base, f"fondo_{nombre}.jpg")
            if os.path.exists(ruta):
                imagen = pygame.image.load(ruta).convert()
                imagen = pygame.transform.scale(imagen, (self.modelo.ancho, self.modelo.alto))
                self.fondos[nombre] = imagen
            else:
                print(f"⚠️ No se encontró: {ruta}")

        # 🔹 Cargar imágenes de las naves
        self.img_jugador = pygame.image.load(os.path.join(base, "nave_jugador.png")).convert_alpha()
        self.img_enemigo = pygame.image.load(os.path.join(base, "nave_enemigo.png")).convert_alpha()

    def dibujar(self):
        escenario = self.modelo.escenarios[self.modelo.escenario_index]
        fondo = self.fondos.get(escenario)
        if fondo:
            self.pantalla.blit(fondo, (0, 0))
        else:
            self.pantalla.fill((0, 0, 0))

        # 🔹 Dibujar jugador (con imagen)
        jugador = self.modelo.jugador
        self.pantalla.blit(self.img_jugador, (jugador.x, jugador.y))

        # 🔹 Dibujar enemigos (con imagen)
        for enemigo in self.modelo.enemigos:
            self.pantalla.blit(self.img_enemigo, (enemigo.x, enemigo.y))

        # 🔹 Dibujar proyectiles (puedes mantenerlos como rectángulos)
        for p in self.modelo.proyectiles:
            pygame.draw.rect(self.pantalla, p.color, (p.x, p.y, p.ancho, p.alto))

        # Texto HUD
        texto = self.fuente.render(f"Puntaje: {self.modelo.puntaje}", True, (255, 255, 255))
        self.pantalla.blit(texto, (10, 10))
        texto2 = self.fuente.render(f"Escenario: {escenario}", True, (255, 255, 255))
        self.pantalla.blit(texto2, (10, 40))

        # Game Over
        if self.modelo.game_over:
            fuente_grande = pygame.font.SysFont(None, 72)
            texto = fuente_grande.render("GAME OVER", True, (255, 0, 0))
            rect = texto.get_rect(center=(self.modelo.ancho // 2, self.modelo.alto // 2))
            self.pantalla.blit(texto, rect)
            texto2 = self.fuente.render("Presiona R para reiniciar", True, (255, 255, 255))
            rect2 = texto2.get_rect(center=(self.modelo.ancho // 2, self.modelo.alto // 2 + 50))
            self.pantalla.blit(texto2, rect2)

        pygame.display.flip()
