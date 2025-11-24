# Videojuego en Python
Este proyecto conjunto consiste en un videojuego similar al clásico de arcade: Gálaga. Recordar que la mecánica del juego es de disparos, el protagonista del juego es una navecita espacial que se desplaza únicamente en dos direcciones: izquierda y derecha. Y se deben esquivar los disparos y las colisiones de naves enemigas que igualmente nos lanzan proyectiles.
El objetivo general del juego es básicamente obtener el mayor puntaje posible, siguiendo la mecánica descrita anteriormente.
El videojuego está desarrollado completamente en Python, con tecnologías inherentes al mismo, estas tecnologías son la librería pygame y Flet, en las que se ahondará a continuación:
### pygame
Es una librería gratuita, multiplataforma y de código abierto para crear aplicaciones multimedia de manera sencilla. Y se eligió para este proyecto porque es una excelente opción para el desarrollo de videojuegos en 2D, lo cúal es el caso.

![image alt](https://github.com/ASJF996/prj_flet_2025B/blob/a9d0168e0be73266a90e28e39e186165594b4737/imagenes_doc/pygame_logo.png)



Se puede instalar fácilmente con pip desde la terminal o el Bash ingresando el siguiente comando:
```
pip install pygame
```
### Flet
Flet es un framework de Python que permite crear aplicaciones web, móviles y de escritorio de manera sencilla, usando la potencia de Flutter pero sin la necesidad de escribir código en Dart ni tener experiencia previa en el desarrollo de frontend.
![image alt](https://github.com/ASJF996/prj_flet_2025B/blob/42d3b157e363725ac8cd763d621b56af475f0be7/imagenes_doc/flet_logo.png)


Se puede instalar fácilmente con pip desde la terminal o el Bash ingresando el siguiente comando:
```
pip install flet
```

## Diagramación del proyecto
Aquí se muestran los diagramas tanto de clase como de casos de uso que se bosquejaron para el desarrollo de este proyecto.
### Diagrama de clases
-- Pendiente
### Diagrama de casos de uso
-- Pendiente

## Características principales del proyecto
Este proyecto posee características que vale la pena mencionar en aspectos tanto de funcionalidad, gestión, diseño, lógica, etc., que se presentan a continuación:
### * Sistema de autenticación
Posee un sistema de login **flet_login.py** que lanza el juego principal **main.py** pasando al usuario como argumento.
### * Utilización de clases genéricas
Dentro de la parte del modelo existe un uso notorio e importante de clase genéricas, concretamente dentro del archivo **Modeloentidades.py** donde existe una clase genérica llamada **Entidad**
### * Persistencia de datos
Utiliza archivos json para almacenar usuarios con sus respectivas contraseñas y puntuaciones. Y aquí el DAO (Data Access Object) se encarga de abstraer el acceso a estos archivos.
### * Control de estados bien definido
El juego posee tres estados claros y bien definidos: login, gameplay y game over. Y el controlador se encarga de manejar la transición entre estados.
### * HUD (Head Up Display)
Durante el gameplay se muestra en la parte superior izquierda información en tiempo real. Se muestran tus vidas, tu puntaje y el nivel actual.

## Estructura del proyecto
El proyecto se compone de los siguientes archivos, scripts, imágenes, etc. Que en su conjunto crean toda la funcionalidad del videojuego. Se muestra una breve descripción de cada uno:
```
prj_flet_2025B/
├── Controlador/ # Lógica de control y coordinación
│ ├── controlador.py # Coordina modelo y vista
│ └── init.py
├── Modelos/ # Capa de datos y lógica de negocio
│ ├── Modeloentidades.py # Entidades del juego (Jugador, Enemigo, Proyectil)
│ ├── Modelojuego.py # Lógica principal del juego
│ ├── modelologin.py # Sistema de login integrado (Pygame)
│ ├── puntaje_dao.py # Data Access Object para puntajes
│ ├── usuarios_dao.py # Data Access Object para usuarios
│ └── init.py
├── Vista/ # Capa de presentación e interfaz
│ ├── vista.py # Renderizado principal
│ ├── assets/ # Recursos gráficos (fondos, sprites)
│ └── init.py
├── Diagramas/ # Diagramas de arquitectura, como clases y casos de uso
├── main.py # Punto de entrada del juego (Pygame)
├── flet_login.py # Sistema de autenticación externo (Flet) Es de aquí desde dónde se ejecuta el programa
├── usuarios.json # Base de datos de usuarios
├── puntajes.json # Base de datos de puntuaciones
└── README.md # Documentación del proyecto
```

## Módulos y componentes del Modelo Vista Controlador
Esta es quizá la sección más importante, pues el proyecto sigue fielmente (y de manera muy notoria) este patrón de diseño. Como se mostró en la sección anterior, se creó una carpeta para cada elemento de este modelo, y es en esta sección que se profundizará sobre la funcionalidad de cada una.
### Modelo
Se encarga de los datos y la lógica del proyecto, se encarga de las reglas del juego, los cálculos físicos como disparos y colisiones, así como de la validación del negocio. También en esta parte del proyecto es que se implementó el patrón de diseño DAO (Data Access Object), aunque en menor medida.
Se compone de los siguientes elementos:
#### Modeloentidades.py

#### Modelojuego.py

#### modelologin.py

#### puntaje_dao.py

#### usuarios_dao.py

### Vista
En esta carpeta se encuentran los componentes visuales del proyecto, en otras palabras de la presentación. 
Se compone de los suguientes elementos:
#### vista.py
Este script se encarga de renderizar los gráficos, mostrar la información (de manera visual obviamente) del modelo, la pantalla de visualización frontal y, por supuesto de gestionar los assets (elementos multimedia).
```
import pygame

class Vista:
    def __init__(self, modelo):
        self.modelo = modelo
        # fuente base (puedes cambiar)
        self.fuente = pygame.font.Font(None, 30)

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

        # Mostrar puntaje actual y highscore si hay usuario
        fuente2 = pygame.font.Font(None, 30)
        texto_puntaje = fuente2.render(f"Puntaje: {self.modelo.puntaje}", True, (255,255,255))
        pantalla.blit(texto_puntaje, (self.modelo.ancho//2 - texto_puntaje.get_width()//2, self.modelo.alto//2 + 40))

        usuario = self.modelo.usuario_actual or getattr(self.modelo.login, "usuario_logueado", "") or getattr(self.modelo.login, "usuario_ingresado", "")
        if usuario:
            high = self.modelo.puntaje_dao.obtener_puntaje(usuario)
            texto_high = fuente2.render(f"Mejor puntaje ({usuario}): {high}", True, (255,255,0))
            pantalla.blit(texto_high, (self.modelo.ancho//2 - texto_high.get_width()//2, self.modelo.alto//2 + 80))

        pygame.display.flip()
```
#### assets/
Esta carpeta contiene todos lo elementos multimedia del juego, en este caso solo contiene imágenes porque no se implementó sonido o video.


![image alt](https://github.com/ASJF996/prj_flet_2025B/blob/ea1236a1ba5a50dfb15561530efb8309bfc00a91/imagenes_doc/assets.png)




### Controlador
Es un intermediario entre el modelo y la vista, mejor dicho es quién coordina ambos. No contiene lógica de negocio ni lógica visual.
Se compone únicamente del siguiente script:
#### controlador.py
Este script se encarga de manejar los datos de entrada, controlar el flujo de la aplicación y controlar el bucle principal del juego.
```
import pygame
from Modelos.Modelojuego import ModeloJuego
from Vista.vista import Vista
from Modelos.modelologin import Login 

class Controlador:
    def __init__(self, pantalla, usuario=None):
        self.pantalla = pantalla
        self.modelo = ModeloJuego(pantalla)
        if usuario:
            self.modelo.usuario_actual = usuario
            self.modelo.login.login_exitoso = True
            self.modelo.login.usuario_logueado = usuario
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

                    if evento.key == pygame.K_ESCAPE:
                        corriendo = False

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
## Flujo del programa


## Ejecución del Programa
Como se mencionó anteroirmente, se ejecuta desde el archivo **flet_login.py**, al ejecutar nos desplegará la interfaz de flet. Y tendremos que loguearnos
