# Videojuego en Python
Este proyecto es un videojuego similar al clásico de arcade: Gálaga. Desarrollado en Python además de la implementación de otras tecnologías y patrones de diseño, así como una fuerte utilización del paradigma de programación orientada a objetos. 
<<<<<<< HEAD
El modo de juego de este proyecto es acerca de  disparar y esquivar ataques de enemigos, que hacen lo mismo. Se presentan múltiples niveles con fondos dirferentes, enemigos que nos atacan, así como un sistema de vida y puntuación.
=======
El modo de juego de este proyecto es basicamente disparar y esquivar ataques de enemigos, que hacen lo mismo. Se presentan múltiples niveles con fondos diferentes, enemigos que nos atacan, así como un sistema de vida y puntuación.
[comentario]: # Aquí voy a poner una imagen de Gálaga
>>>>>>> 2a8e21ccf9e60e8117005455b9381e417369a937

## Software utilizado
Como se mencionó anteriormente, se empleó el lenguaje de programación Python en la totalidad del proyecto, así como componentes inherentes al mismo tales como la librería pygame y flet, que se explican a continuación:

### pygame
Es una librería de Python, gratuita y de código abierto para el desarrolló de aplicaciones multimedia, especialmente videojuegos en 2D. Ésta fue de suma importancia en este proyecto para el manejo de los gráficos y el input del usuario a través del teclado para realizar las acciones como desplazarse y disparar, así como para reiniciar la partida una vez perdido el juego. 
<<<<<<< HEAD

Instalacion de pygame
Para la instalacion de las librerias  de pygame  se ejecuto el comando pip install pygame en la terminal de comandos de python.
=======
[comentario]: # Aquí voy a poner el logo de pygame
>>>>>>> 2a8e21ccf9e60e8117005455b9381e417369a937
### Flet
Flet es un framework muy conocido de Python para interfaz de usuario enriquecido, que permite crear de manera rápida y sencilla aplicaciones web, de escritorio y/o móviles interactivas; ésto sin la necesidad de poseer conocimientos previos de HTML, JavaScript o estilos CSS.
[comentario]: # Aquí voy a poner el logo de Flet
Para este proyecto en concreto se utilizó para el desarrollo de la interfaz de usuario en la que el jugador (usuario) tiene que loguearse, o registrarse en su defecto.
<<<<<<< HEAD
Para el desarrollo de este proyecto, se implemento flet para la interfaz que nos permite loguear un usuario, en esta interfaz se introduce el nombre del usuario y contraseña, esta se conecta con una base de datos.

Para la instalacion de flet, en la terminal de comandos insertamos pip install flet.
=======
[comentario]: # Aquí voy a poner una captura de la interfaz de usuario
>>>>>>> 2a8e21ccf9e60e8117005455b9381e417369a937

## Características principales
A continuación se muestran carácterísticas destacables del proyecto.
### Arquitectura Modelo Vista Controlador
Este fue un factor clave en el desarrollo, permitió separar de manera clara las funcionalidades de las partes principales del código. Más adelante se ahondará en las clases que componen cada una de las funcionalidades mencionadas anteriormente.
### Guardado de usuarios y login
Para esto se utilizó una interfaz de Flet, desde la que se pueda registrar un usuario o iniciar sesión según sea el caso.
### Persistecia de datos
Para esto se implemento un archivo json para guardar los registros del sistema de login, ademas del puntaje obtenido por un usuario y el nombre de usuario.

## Patrones de diseño aplicados
Se emplearon únicamente dos patrones de diseño: MVC y DAO. Que tuvieron una destacada influencia en la estructuración y lógica del código.
[comentario]: # Aquí voy a poner una imagen que represente la estructura del Modelo Vista Controlador y el Data Access Object
### (MVC) Modelo Vista Controlador
El modelo realiza la representación del estado y los datos del juego; contiene las entidades, la lógica y el negocio del juego.
La vista se encarga exclusivamente de representar visualmente el juego, solo recibe datos del usuario y los muestra.
Y por último el controlador se ocupa de manejar el input de usuario y actualizar los datos del modelo en consecuencia, así como de coordinar la actualización de la vista.
[comentario]: # Aquí voy a poner una captura de pantalla en la que se vean los scripts, mas no voy a mostrar el código por ahora
### (DAO) Data Access Object
<<<<<<< HEAD
Se desarrollaron dos archivos.py para el DAO, uno se utilizo para guardar los usuarios, mediante un nombre de usuario y una contraseña, todos estos se guardan mediante diccionarios en un archivo.json en la misma carpeta en la que se encuentran los archivos.py

el otro archivo que se creo en el proyecto es un DAO que guarda los puntajes mas altos con el nombre de usuario, y se actualizan cada vez que el jugador alcanza un nuevo puntaje mayor al registrado previamente 

=======
Este patrón se aplico únicamente en la interfaz de usuario, concretamente para verificar la existencia del mismo, o si no existe crearlo y darlo de alta en el archivo json
[comentario]: # Aquí voy a poner una captura del script dao.py
>>>>>>> 2a8e21ccf9e60e8117005455b9381e417369a937

## Estructutura del proyecto
Esta sección es de crucial importancia, ya que se va a explicar detalladamente cada componente del proyecto, los assets, el archivo json, pero especialmente se discurrirá sobre el funcionamiento de los scripts, cómo se comunican entre ellos y el funcionamiento de todo el sistema.
[comentario]: # Aquí voy a poner una captura de pantalla de la estructura del sistema: la identación de las carpetas y los scripts.
### dao.py
Se realizó este script exclusivamente para la implementación de patrón DAO. Se encarga de gestionar el acceso de los usuarios (se comunica con la interfaz Flet), aplica las operaciones CRUD comunicandose con el archivo json.
```
import json
import os

class UsuarioDAO:
    def __init__(self, archivo="usuarios.json"):
        self.archivo = archivo
        if not os.path.exists(self.archivo):
            with open(self.archivo, "w") as f:
                json.dump({}, f)

    def cargar_usuarios(self):
        with open(self.archivo, "r") as f:
            return json.load(f)

    def guardar_usuarios(self, usuarios):
        with open(self.archivo, "w") as f:
            json.dump(usuarios, f, indent=4)

    def agregar_usuario(self, usuario, contraseña):
        usuarios = self.cargar_usuarios()
        if usuario in usuarios:
            raise ValueError("Usuario ya existe")
        usuarios[usuario] = contraseña
        self.guardar_usuarios(usuarios)

    def verificar_usuario(self, usuario, contraseña):
        usuarios = self.cargar_usuarios()
        return usuarios.get(usuario) == contraseña
```
### flet_login.py
Este es el script de la interfaz con Flet, es un sistema de registro y de login independiente; es una interfaz bastante amigable y fácil de entender para el usuario.
Se muestra a continuación el código:
```
import flet as ft
import subprocess
from dao import UsuarioDAO

def generar_login(page: ft.Page):
    dao = UsuarioDAO()

    # Configuración general de la página
    page.title = "Login - Juego MVC"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20
    page.bgcolor = "#E3F2FD"

    # Campos de usuario y contraseña
    username = ft.TextField(label="Usuario", width=300, autofocus=True)
    password = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300)
    mensaje = ft.Text(value="", color="red", size=16)

    # Función para registrar usuario
    def registrar(e):
        try:
            dao.agregar_usuario(username.value, password.value)
            mensaje.value = "Usuario registrado correctamente."
            mensaje.color = "green"
        except ValueError:
            mensaje.value = "Nombre de usuario ya existe."
            mensaje.color = "red"
        page.update()

    # Función para iniciar el juego
    def iniciar_juego(e):
        if dao.verificar_usuario(username.value, password.value):
            mensaje.value = f"Bienvenido, {username.value}"
            mensaje.color = "green"
            page.update()
            page.window_minimized = True
            # Abrir Pygame pasando el usuario
            subprocess.Popen(["python", "main.py", username.value])
        else:
            mensaje.value = "Usuario o contraseña incorrectos"
            mensaje.color = "red"
            page.update()

    login_button = ft.ElevatedButton(
        "Login",
        on_click=iniciar_juego,
        bgcolor="#1976D2",
        color="white",
        width=120
    )
    register_button = ft.ElevatedButton(
        "Registrar",
        on_click=registrar,
        bgcolor="#388E3C",
        color="white",
        width=120
    )

    page.add(
        ft.Column(
            [
                ft.Container(
                    ft.Text("Juego MVC - Login", size=28, weight=ft.FontWeight.BOLD, color="#0D47A1"),
                    padding=ft.padding.all(10),
                    bgcolor="#BBDEFB",
                    border_radius=10,
                    alignment=ft.alignment.center
                ),
                ft.Container(height=20),
                username,
                password,
                ft.Row([login_button, register_button], alignment=ft.MainAxisAlignment.SPACE_EVENLY, spacing=20),
                mensaje
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        )
    )

def main():
    ft.app(target=generar_login)

if __name__ == "__main__":
    main()
```
Y la interfaz del proyecto se visualiza de la siguiente manera:
[comentario]: # Aquí voy a poner una captura de pantalla de la interfaz.
### usuarios.json
Como se mencionó anteriormente, este archivo sirve como almacén de los usuarios, tiene la única función de guardar los registros; pues recordar que todo el código para manipular la información de los mismos se encuentra en dao.py.
Se muestra a continuación el archivo:
```
```
### modelo.py

### vista.py
Este script se encarga única y exclusivamente de la representación visual del juego, renderiza los elementos del juego, el HUD y las pantallas de estado. 
Se muestra a continuación el código:
```
import pygame

class Vista:
    def __init__(self, modelo):
        self.modelo = modelo

    def dibujar(self):
        pantalla = self.modelo.pantalla
        if self.modelo.login.login_exitoso:
            # Fondo
            fondo = self.modelo.fondos[self.modelo.escenarios[self.modelo.nivel_actual]]
            pantalla.blit(fondo, (0,0))
            # Jugador
            self.modelo.jugador.dibujar(pantalla)
            # Enemigos
            for e in self.modelo.enemigos:
                e.dibujar(pantalla)
            # Proyectiles
            for p in self.modelo.proyectiles:
                p.dibujar(pantalla)
            # Proyectiles enemigos
            for p in self.modelo.proyectiles_enemigos:
                p.dibujar(pantalla)
            # HUD
            fuente = pygame.font.Font(None, 30)
            texto = fuente.render(f"Vidas: {self.modelo.jugador.vidas}  Puntaje: {self.modelo.puntaje}  Nivel: {self.modelo.nivel_actual+1}", True, (255,255,255))
            pantalla.blit(texto, (10,10))
        else:
            # Pantalla de login
            pantalla.fill((0,0,0))
            fuente = pygame.font.Font(None, 40)
            titulo = fuente.render("LOGIN", True, (255,255,255))
            pantalla.blit(titulo, (self.modelo.ancho//2 - 50, 100))
            fuente_input = pygame.font.Font(None, 30)
            user = fuente_input.render(f"Usuario: {self.modelo.login.usuario_ingresado}", True, (255,255,255))
            pantalla.blit(user, (self.modelo.ancho//2 - 100, 200))
            contra = fuente_input.render(f"Contraseña: {'*'*len(self.modelo.login.contraseña_ingresada)}", True, (255,255,255))
            pantalla.blit(contra, (self.modelo.ancho//2 - 100, 250))
            instr = fuente_input.render("Presiona ENTER para cambiar campo / validar", True, (255,255,255))
            pantalla.blit(instr, (self.modelo.ancho//2 - 200, 300))

        pygame.display.flip()

    def mostrar_game_over(self):
        pantalla = self.modelo.pantalla
        fuente = pygame.font.Font(None, 60)
        texto = fuente.render("GAME OVER", True, (255,0,0))
        pantalla.blit(texto, (self.modelo.ancho//2 - 150, self.modelo.alto//2 - 30))
        pygame.display.flip()
```
### controlador.py
Es el intermediario y corrdinador entre el usuario y la vista (del patrón de diseño MVC). Se encarga de gestionar el flujo principal del juego, procesar eventos del input, así como de manejar estados del juego como login, el juego en sí y el game over. 
Se muestra a continuación el código:
```
import pygame
from modelo import ModeloJuego
from vista import Vista

class Controlador:
    def __init__(self, pantalla, usuario=None):
        self.pantalla = pantalla
        self.modelo = ModeloJuego(pantalla)
        if usuario:
            self.modelo.login.login_exitoso = True
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
```
### main.py
Este es el punto de entrada principal del juego, se encarga de inicalizar pygame y el controlador, también de manejar argumentos de la línea de comandos para el usuario.
```
import pygame
from controlador import Controlador
import sys

def main(usuario=None):
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Juego MVC")
    controlador = Controlador(pantalla, usuario=usuario)
    controlador.iniciar()
    pygame.quit()

if __name__ == "__main__":
    usuario = None
    if len(sys.argv) > 1:
        usuario = sys.argv[1]  # recibe el usuario desde Flet si se quiere
    main(usuario)
```
