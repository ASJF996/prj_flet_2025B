
import pygame
import random
import time
import os
from Modelos.usuarios_dao import UsuarioDAO
from Modelos.puntaje_dao import PuntajeDAO
from Modelos.modelologin import Login
from Modelos.Modeloentidades import Jugador
from Modelos.Modeloentidades import Enemigo
from Modelos.Modeloentidades import Proyectil

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

        self.escenarios = ["andromeda.jpg", "planetas.jpg", "saturno.jpg"]
        self.nivel_actual = 0
        self.fondos = {}

        for fondo in self.escenarios:
            ruta = os.path.join(os.path.dirname(__file__),  "..", "Vista", "assets", fondo)
            try:
                self.fondos[fondo] = pygame.image.load(ruta).convert()
            except Exception:
                    # fallback si faltan assets
                s = pygame.Surface((ancho, alto))
                s.fill((0, 0, 0))
                self.fondos[fondo] = s

        ruta_jugador = os.path.join(os.path.dirname(__file__), "..", "Vista", "assets", "jugador.png")

        try:
            jugador_img = pygame.image.load(ruta_jugador).convert_alpha()
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
        ruta_enemigo = os.path.join(os.path.dirname(__file__),  "..", "Vista", "assets", "enemigo.png")
        try:
            enemigo_img = pygame.image.load(os.path.join(ruta_enemigo)).convert_alpha()
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
