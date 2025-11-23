import pygame

from typing import Generic, TypeVar, Optional


T = TypeVar('T')  # Tipo genérico para la imagen u otro dato asociado

class Entidad(Generic[T]):
    def __init__(self, x: int, y: int, ancho: int, alto: int, velocidad: int = 0, imagen: Optional[T] = None):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.velocidad = velocidad
        self.imagen: Optional[T] = imagen

    def rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.ancho, self.alto)

    def dibujar(self, pantalla):
        if isinstance(self.imagen, pygame.Surface):
            pantalla.blit(self.imagen, (self.x, self.y))
        else:
            pygame.draw.rect(pantalla, (255, 0, 0), self.rect())

    def mover(self, dx: int = 0, dy: int = 0, ancho_pantalla: int = 800, alto_pantalla: int = 600):
        self.x += dx * self.velocidad
        self.y += dy * self.velocidad
        self.x = max(0, min(self.x, ancho_pantalla - self.ancho))
        self.y = max(0, min(self.y, alto_pantalla - self.alto))

class Jugador(Entidad):
    def __init__(self, x, y, imagen):
        super().__init__(x, y, imagen.get_width(), imagen.get_height(), velocidad=5, imagen=imagen)
        self.vidas = 3

class Enemigo(Entidad):
    def __init__(self, x, y, imagen, velocidad_y=3):
        ancho = imagen.get_width()
        alto = imagen.get_height()

        # Llamamos al constructor de Entidad
        super().__init__(x, y, ancho, alto, velocidad=velocidad_y, imagen=imagen)

    def mover(self):
        # Solo movimiento vertical (enemigos caen)
        self.y += self.velocidad

class Proyectil(Entidad):
    def __init__(self, x, y, velocidad=8, color=(255,255,0)):
        super().__init__(x, y, 5, 10, velocidad=velocidad)
        self.color = color

    def mover(self, hacia_arriba=True):
        self.y -= self.velocidad if hacia_arriba else -self.velocidad

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, self.rect())

