import pygame
import random

class Jugador:
    def __init__(self, x, y, velocidad=5):
        self.x = x
        self.y = y
        self.velocidad = velocidad
        self.ancho = 50
        self.alto = 50
        self.color = (0, 255, 0)

    def mover(self, dx, dy):
        self.x += dx * self.velocidad
        self.y += dy * self.velocidad
        self.x = max(0, min(self.x, 800 - self.ancho))
        self.y = max(0, min(self.y, 600 - self.alto))


class Enemigo:
    def __init__(self, x, y, velocidad=3):
        self.x = x
        self.y = y
        self.velocidad = velocidad
        self.ancho = 40
        self.alto = 40
        self.color = (255, 0, 0)

    def mover(self):
        self.y += self.velocidad
        if self.y > 600:
            self.y = random.randint(-100, -40)
            self.x = random.randint(0, 760)


class Proyectil:
    def __init__(self, x, y, velocidad=8):
        self.x = x
        self.y = y
        self.velocidad = velocidad
        self.ancho = 5
        self.alto = 10
        self.color = (255, 255, 0)

    def mover(self):
        self.y -= self.velocidad


class ModeloJuego:
    def __init__(self, ancho=800, alto=600, num_enemigos=5):
        self.ancho = ancho
        self.alto = alto
        self.jugador = Jugador(ancho // 2, alto - 60)
        self.enemigos = [Enemigo(random.randint(0, ancho - 40),
                                 random.randint(-200, -40))
                         for _ in range(num_enemigos)]
        self.proyectiles = []
        self.game_over = False
        self.puntaje = 0
        self.escenario_index = 0
        self.escenarios = ["espacio", "desierto", "ciudad"]

    def disparar(self):
        nuevo = Proyectil(self.jugador.x + self.jugador.ancho // 2 - 2, self.jugador.y)
        self.proyectiles.append(nuevo)

    def cambiar_escenario(self):
        self.escenario_index = (self.escenario_index + 1) % len(self.escenarios)

    def actualizar(self):
        if self.game_over:
            return

        for enemigo in self.enemigos:
            enemigo.mover()
        for proyectil in self.proyectiles:
            proyectil.mover()
        self.proyectiles = [p for p in self.proyectiles if p.y > -p.alto]

        # Colisiones proyectil-enemigo
        for p in self.proyectiles[:]:
            p_rect = pygame.Rect(p.x, p.y, p.ancho, p.alto)
            for e in self.enemigos[:]:
                e_rect = pygame.Rect(e.x, e.y, e.ancho, e.alto)
                if p_rect.colliderect(e_rect):
                    self.enemigos.remove(e)
                    self.proyectiles.remove(p)
                    self.puntaje += 10
                    self.enemigos.append(
                        Enemigo(random.randint(0, self.ancho - 40),
                                random.randint(-200, -40))
                    )
                    break

        # Colisiones jugador-enemigo
        jugador_rect = pygame.Rect(self.jugador.x, self.jugador.y, self.jugador.ancho, self.jugador.alto)
        for enemigo in self.enemigos:
            enemigo_rect = pygame.Rect(enemigo.x, enemigo.y, enemigo.ancho, enemigo.alto)
            if jugador_rect.colliderect(enemigo_rect):
                self.game_over = True
