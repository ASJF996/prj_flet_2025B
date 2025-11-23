import pygame
import random
import time
import os
from dao import UsuarioDAO
from puntaje_dao import PuntajeDAO
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

class Enemigo:
    def __init__(self, x, y, imagen, velocidad_y=3):
        self.x = x
        self.y = y
        self.imagen = imagen
        self.ancho = imagen.get_width()
        self.alto = imagen.get_height()
        self.velocidad_y = velocidad_y

    def mover(self):
        self.y += self.velocidad_y

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, (self.x, self.y))

    def rect(self):
        return pygame.Rect(self.x, self.y, self.ancho, self.alto)

class Proyectil(Entidad):
    def __init__(self, x, y, velocidad=8, color=(255,255,0)):
        super().__init__(x, y, 5, 10, velocidad=velocidad)
        self.color = color

    def mover(self, hacia_arriba=True):
        self.y -= self.velocidad if hacia_arriba else -self.velocidad

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, self.rect())

class Login:
    def __init__(self, dao: UsuarioDAO):
        self.dao = dao
        self.usuario_ingresado = ""
        self.contraseña_ingresada = ""
        self.escribiendo_usuario = True
        self.login_exitoso = False
        self.usuario_logueado = ""  # nombre del usuario que quedó logueado

    def registrar_usuario(self, usuario, contraseña):
        try:
            self.dao.agregar_usuario(usuario, contraseña)
            return True
        except ValueError:
            return False

    def procesar_tecla(self, tecla):
        if self.login_exitoso:
            return
        if tecla == pygame.K_BACKSPACE:
            if self.escribiendo_usuario:
                self.usuario_ingresado = self.usuario_ingresado[:-1]
            else:
                self.contraseña_ingresada = self.contraseña_ingresada[:-1]
        elif tecla == pygame.K_RETURN:
            if self.escribiendo_usuario:
                self.escribiendo_usuario = False
            else:
                if self.dao.verificar_usuario(self.usuario_ingresado, self.contraseña_ingresada):
                    self.login_exitoso = True
                    self.usuario_logueado = self.usuario_ingresado
                else:
                    self.usuario_ingresado = ""
                    self.contraseña_ingresada = ""
                    self.escribiendo_usuario = True
        else:
            letra = pygame.key.name(tecla)
            if len(letra) == 1:
                if self.escribiendo_usuario:
                    self.usuario_ingresado += letra
                else:
                    self.contraseña_ingresada += letra

class ModeloJuego:
    def __init__(self, pantalla, ancho=800, alto=600):
        self.pantalla = pantalla
        self.ancho = ancho
        self.alto = alto
        self.dao = UsuarioDAO()
        self.login = Login(self.dao)

        # DAO de puntajes (archivo puntajes.json)
        self.puntaje_dao = PuntajeDAO(archivo="puntajes.json")
        self.usuario_actual = None  # se setea desde controlador/main si se desea

        self.escenarios = ["andromeda.jpg","planetas.jpg","saturno.jpg"]
        self.nivel_actual = 0
        self.fondos = {}
        for fondo in self.escenarios:
            path = os.path.join("assets", fondo)
            try:
                self.fondos[fondo] = pygame.image.load(path).convert()
            except Exception:
                # fallback si faltan assets
                s = pygame.Surface((ancho, alto))
                s.fill((0,0,0))
                self.fondos[fondo] = s

        try:
            jugador_img = pygame.image.load(os.path.join("assets","jugador.png")).convert_alpha()
        except Exception:
            jugador_img = pygame.Surface((40, 40), pygame.SRCALPHA)
            pygame.draw.polygon(jugador_img, (0,255,0), [(0,40),(20,0),(40,40)])

        self.jugador = Jugador(ancho//2, alto-60, jugador_img)
        self.enemigos = []
        self.proyectiles = []
        self.proyectiles_enemigos = []
        self.ultimo_spawn = time.time()
        self.spawn_delay = 1.0
        self.game_over = False
        self.puntaje = 0

        # flag para guardar puntaje solo 1 vez
        self.score_saved = False

    def crear_enemigo(self):
        try:
            enemigo_img = pygame.image.load(os.path.join("assets","enemigo.png")).convert_alpha()
        except Exception:
            enemigo_img = pygame.Surface((40, 30), pygame.SRCALPHA)
            enemigo_img.fill((255,0,0))
        velocidad = 2 + self.nivel_actual
        x = random.randint(0, self.ancho-40)
        y = random.randint(-100, -40)
        self.enemigos.append(Enemigo(x, y, enemigo_img, velocidad))

    def disparar(self):
        p = Proyectil(self.jugador.x + self.jugador.ancho//2 -2, self.jugador.y)
        self.proyectiles.append(p)

    def disparar_enemigo(self, enemigo):
        p = Proyectil(enemigo.x + enemigo.ancho//2 -2, enemigo.y + enemigo.alto, velocidad=5, color=(255,0,0))
        self.proyectiles_enemigos.append(p)

    def actualizar(self):
        # Spawn continuo de enemigos
        if time.time() - self.ultimo_spawn > self.spawn_delay:
            self.crear_enemigo()
            self.ultimo_spawn = time.time()

        # Mover enemigos
        for e in self.enemigos[:]:
            e.mover()
            if random.random() < 0.01 + self.nivel_actual*0.005:  # probabilidad de disparo
                self.disparar_enemigo(e)
            if e.y > self.alto:
                self.enemigos.remove(e)

        # Mover proyectiles del jugador
        for p in self.proyectiles:
            p.mover()
        self.proyectiles = [p for p in self.proyectiles if p.y > -p.alto]

        # Mover proyectiles de enemigos
        for p in self.proyectiles_enemigos:
            p.mover(hacia_arriba=False)
        self.proyectiles_enemigos = [p for p in self.proyectiles_enemigos if p.y < self.alto+p.alto]

        # Colisiones proyectil-enemigo
        for p in self.proyectiles[:]:
            for e in self.enemigos[:]:
                if p.rect().colliderect(e.rect()):
                    self.enemigos.remove(e)
                    if p in self.proyectiles:
                        self.proyectiles.remove(p)
                    self.puntaje += 10
                    break

        # Colisiones enemigo-jugador
        for e in self.enemigos[:]:
            if self.jugador.rect().colliderect(e.rect()):
                self.jugador.vidas -=1
                self.enemigos.remove(e)
                if self.jugador.vidas <=0:
                    self.game_over = True

        # Colisiones proyectiles enemigos-jugador
        for p in self.proyectiles_enemigos[:]:
            if self.jugador.rect().colliderect(p.rect()):
                self.jugador.vidas -=1
                if p in self.proyectiles_enemigos:
                    self.proyectiles_enemigos.remove(p)
                if self.jugador.vidas <=0:
                    self.game_over = True

        # Subir nivel
        if self.puntaje >= (self.nivel_actual+1)*50:
            self.nivel_actual = min(self.nivel_actual+1,len(self.escenarios)-1)
            self.spawn_delay = max(0.3,self.spawn_delay-0.2)

        # Si terminó el juego, guardar puntaje (solo una vez)
        if self.game_over and not self.score_saved:
            usuario = self.usuario_actual or getattr(self.login, "usuario_logueado", "") or getattr(self.login, "usuario_ingresado", "")
            try:
                if usuario:
                    self.puntaje_dao.actualizar_puntaje(usuario, self.puntaje)
            except Exception as e:
                print("Error guardando puntaje:", e)
            self.score_saved = True

    def reiniciar(self):
        self.jugador.vidas = 3
        self.puntaje = 0
        self.nivel_actual = 0
        self.jugador.x = self.ancho//2
        self.jugador.y = self.alto-60
        self.enemigos = []
        self.proyectiles = []
        self.proyectiles_enemigos = []
        self.spawn_delay = 1.0
        self.game_over = False
        self.score_saved = False
