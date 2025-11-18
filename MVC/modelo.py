import pygame
import random
import time
import os
from dao import UsuarioDAO

class Entidad:
    def __init__(self, x, y, ancho, alto, velocidad=0, imagen=None):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.velocidad = velocidad
        self.imagen = imagen

    def rect(self):
        return pygame.Rect(self.x, self.y, self.ancho, self.alto)

    def dibujar(self, pantalla):
        if self.imagen:
            pantalla.blit(self.imagen, (self.x, self.y))
        else:
            pygame.draw.rect(pantalla, (255,0,0), self.rect())

    def mover(self, dx=0, dy=0, ancho_pantalla=800, alto_pantalla=600):
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
    def __init__(self, x, y, velocidad=8, imagen=None):
        super().__init__(x, y, 5, 10, velocidad=velocidad, imagen=imagen)

    def mover(self):
        self.y -= self.velocidad

class Login:
    def __init__(self, dao: UsuarioDAO):
        self.dao = dao
        self.usuario_ingresado = ""
        self.contraseña_ingresada = ""
        self.escribiendo_usuario = True
        self.login_exitoso = False

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
    def __init__(self, pantalla, ancho=800, alto=600, usuario_logeado=None):
        self.pantalla = pantalla
        self.ancho = ancho
        self.alto = alto
        self.dao = UsuarioDAO()
        self.login = Login(self.dao)
        if usuario_logeado:
            self.login.usuario_ingresado = usuario_logeado
            self.login.login_exitoso = True

        self.escenarios = ["andromeda.jpg","planetas.jpg","saturno.jpg"]
        self.nivel_actual = 0
        self.fondos = {}
        for fondo in self.escenarios:
            path = os.path.join("assets", fondo)
            self.fondos[fondo] = pygame.image.load(path).convert()
        jugador_img = pygame.image.load(os.path.join("assets","jugador.png")).convert_alpha()
        self.jugador = Jugador(ancho//2, alto-60, jugador_img)
        self.enemigos = []
        self.proyectiles = []
        self.enemigos_proyectiles = []
        self.ultimo_spawn = time.time()
        self.spawn_delay = 1.0
        self.game_over = False
        self.puntaje = 0

    def crear_enemigo(self):
        enemigo_img = pygame.image.load(os.path.join("assets","enemigo.png")).convert_alpha()
        velocidad = 2 + self.nivel_actual
        x = random.randint(0, self.ancho-40)
        y = random.randint(-100, -40)
        self.enemigos.append(Enemigo(x, y, enemigo_img, velocidad))

    def disparar(self):
        p = Proyectil(self.jugador.x + self.jugador.ancho//2 -2, self.jugador.y)
        self.proyectiles.append(p)

    def enemigo_disparo(self, enemigo):
        p = Proyectil(enemigo.x + enemigo.ancho//2 -2, enemigo.y + enemigo.alto, velocidad=-5)
        self.enemigos_proyectiles.append(p)

    def actualizar(self):
        # Spawn continuo
        if time.time() - self.ultimo_spawn > self.spawn_delay:
            self.crear_enemigo()
            self.ultimo_spawn = time.time()

        # Mover enemigos
        for e in self.enemigos[:]:
            e.mover()
            # Enemigo dispara aleatoriamente
            if random.random() < 0.01:
                self.enemigo_disparo(e)
            if e.y > self.alto:
                self.enemigos.remove(e)

        # Mover proyectiles jugador
        for p in self.proyectiles:
            p.mover()
        self.proyectiles = [p for p in self.proyectiles if p.y > -p.alto]

        # Mover proyectiles enemigos
        for p in self.enemigos_proyectiles:
            p.y += -p.velocidad  # invierte dirección
        self.enemigos_proyectiles = [p for p in self.enemigos_proyectiles if p.y < self.alto]

        # Colisiones proyectil-enemigo
        for p in self.proyectiles[:]:
            for e in self.enemigos[:]:
                if p.rect().colliderect(e.rect()):
                    self.enemigos.remove(e)
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
        for p in self.enemigos_proyectiles[:]:
            if self.jugador.rect().colliderect(p.rect()):
                self.jugador.vidas -=1
                self.enemigos_proyectiles.remove(p)
                if self.jugador.vidas <=0:
                    self.game_over = True

        # Subir nivel
        if self.puntaje >= (self.nivel_actual+1)*50:
            self.nivel_actual = min(self.nivel_actual+1,len(self.escenarios)-1)
            self.jugador.x = self.ancho//2
            self.jugador.y = self.alto-60
            self.spawn_delay = max(0.3,self.spawn_delay-0.2)

    def reiniciar(self):
        self.jugador.vidas = 3
        self.puntaje = 0
        self.nivel_actual = 0
        self.jugador.x = self.ancho//2
        self.jugador.y = self.alto-60
        self.enemigos = []
        self.proyectiles = []
        self.enemigos_proyectiles = []
        self.spawn_delay = 1.0
        self.game_over = False
