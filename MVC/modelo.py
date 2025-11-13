from __future__ import annotations
import pygame
import random
from typing import TypeVar, Generic, List, Tuple


T = TypeVar("T", bound="Entidad")


class Entidad(Generic[T]):
    """Clase base para cualquier objeto del juego con posición, tamaño y color o imagen."""

    def __init__(self, x: int, y: int, ancho: int, alto: int, color: Tuple[int, int, int],
                 velocidad: int = 0, imagen: pygame.Surface | None = None):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.color = color
        self.velocidad = velocidad
        self.imagen = imagen  # 🔹 Nueva propiedad

    def rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.ancho, self.alto)



    def dibujar(self, pantalla: pygame.Surface) -> None:
        """Dibuja el objeto en la pantalla."""
        pygame.draw.rect(pantalla, self.color, self.rect())

    def mover(self, *args, **kwargs) -> None:
        """Método genérico que pueden sobreescribir las subclases."""
        pass




class Jugador(Entidad["Jugador"]):
    def __init__(self, x: int, y: int, velocidad: int = 5):
        super().__init__(x, y, 50, 50, (0, 255, 0), velocidad)

    def mover(self, dx: int, dy: int, ancho_pantalla: int, alto_pantalla: int) -> None:
        """Movimiento controlado del jugador dentro de los límites de la pantalla."""
        self.x += dx * self.velocidad
        self.y += dy * self.velocidad
        self.x = max(0, min(self.x, ancho_pantalla - self.ancho))
        self.y = max(0, min(self.y, alto_pantalla - self.alto))


class Enemigo(Entidad["Enemigo"]):
    def __init__(self, x: int, y: int, velocidad: int = 3):
        super().__init__(x, y, 40, 40, (255, 0, 0), velocidad)

    def mover(self, ancho_pantalla: int, alto_pantalla: int) -> None:
        """Movimiento descendente del enemigo con reposición aleatoria."""
        self.y += self.velocidad
        if self.y > alto_pantalla:
            self.y = random.randint(-100, -40)
            self.x = random.randint(0, ancho_pantalla - self.ancho)


class Proyectil(Entidad["Proyectil"]):
    def __init__(self, x: int, y: int, velocidad: int = 8):
        super().__init__(x, y, 5, 10, (255, 255, 0), velocidad)

    def mover(self) -> None:
        """Movimiento vertical ascendente del proyectil."""
        self.y -= self.velocidad




class ModeloJuego:
    """Contiene toda la lógica del juego (modelo del patrón MVC)."""

    def __init__(self, ancho: int = 800, alto: int = 600, num_enemigos: int = 5):
        self.ancho = ancho
        self.alto = alto
        self.jugador = Jugador(ancho // 2, alto - 60)
        self.enemigos: List[Enemigo] = [
            Enemigo(random.randint(0, ancho - 40), random.randint(-200, -40))
            for _ in range(num_enemigos)
        ]
        self.proyectiles: List[Proyectil] = []
        self.game_over: bool = False
        self.puntaje: int = 0
        self.escenario_index: int = 0
        self.escenarios: List[str] = ["espacio", "desierto", "ciudad"]

    def disparar(self) -> None:
        """Crea un nuevo proyectil desde la posición del jugador."""
        nuevo = Proyectil(self.jugador.x + self.jugador.ancho // 2 - 2, self.jugador.y)
        self.proyectiles.append(nuevo)

    def cambiar_escenario(self) -> None:
        """Cambia el escenario actual de forma cíclica."""
        self.escenario_index = (self.escenario_index + 1) % len(self.escenarios)

    def actualizar(self) -> None:
        """Actualiza el estado general del juego."""
        if self.game_over:
            return

        
        for enemigo in self.enemigos:
            enemigo.mover(self.ancho, self.alto)

        
        for p in self.proyectiles:
            p.mover()

        
        self.proyectiles = [p for p in self.proyectiles if p.y > -p.alto]

        
        for p in self.proyectiles[:]:
            for e in self.enemigos[:]:
                if p.rect().colliderect(e.rect()):
                    self.enemigos.remove(e)
                    self.proyectiles.remove(p)
                    self.puntaje += 10
                    
                    self.enemigos.append(
                        Enemigo(random.randint(0, self.ancho - 40), random.randint(-200, -40))
                    )
                    break

        
        for enemigo in self.enemigos:
            if self.jugador.rect().colliderect(enemigo.rect()):
                self.game_over = True
                break

    def reiniciar(self) -> None:
        """Reinicia el estado del juego sin recrear el objeto."""
        self.jugador = Jugador(self.ancho // 2, self.alto - 60)
        self.enemigos = [
            Enemigo(random.randint(0, self.ancho - 40), random.randint(-200, -40))
            for _ in range(5)
        ]
        self.proyectiles = []
        self.puntaje = 0
        self.game_over = False
        self.escenario_index = 0
