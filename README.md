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
<<<<<<< HEAD
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


Este patrón se aplico únicamente en la interfaz de usuario, concretamente para verificar la existencia del mismo, o si no existe crearlo y darlo de alta en el archivo json
[comentario]: # Aquí voy a poner una captura del script dao.py


## Estructutura del proyecto
Esta sección es de crucial importancia, ya que se va a explicar detalladamente cada componente del proyecto, los assets, el archivo json, pero especialmente se discurrirá sobre el funcionamiento de los scripts, cómo se comunican entre ellos y el funcionamiento de todo el sistema.

[comentario]: # Aquí voy a poner una captura de pantalla de la estructura del sistema: la identación de las carpetas y los scripts.
### dao.py
Se realizó este script exclusivamente para la implementación de patrón DAO. Se encarga de gestionar el acceso de los usuarios (se comunica con la interfaz Flet), aplica las operaciones CRUD comunicandose con el archivo json.


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
#### Modelojuego.py
En la carpeta modelos se agregaron los modelos para diferetes funciones
El archivo Modelojuego.py es una parte escencial en el desarrollo del proyecto, en el se encuentra toda la logica del Juego, en esta parte del MVC se programó todas las reglas del juego. y las funciones que realizan las entidades dentro del proyecto, en esta parte del codigo tenemos todas las operaciones que se crean en el juego. 
Primero se importan todas las librerias necesarias, en este caso, se importó pygame,random,time,os y de los archivos creados se importó USUARIODAO del archivo dao.py y de puntaje_dao se importo PuntajeDAO, tambien de Modelosentidades se importaron jugador,proyectil y enemigo.
Dentro de nuestra clase Modelojuego tenemos un metodo especial __init__ que tiene los atributos de pantalla, este nos sirve para el login al juego, dentro del def, declaramos publicos los atributos.
En un ciclo  agregamos los fondos o escenarios asignando la ruta de donde se encuentran las imagenes en nuestro proyecto, y mediante el metodo Surface de pygame le damos el formato de fondo.
luego se creo el metodo crear_enemigo, que crea la imagen del enemigo y mediante randit posiciona la imagen en diferentes  lugares de la pantalla, mediante un excep busca la ruta de la imagen que se le da si no se encuentra obtiene una de pygame.

Despues se agregaron metodos disparar para el jugador principal y dosparar_enemigo para la entidad enemigo.

tambien se creo un metodo para actualizar, que genera entidades enemigo constantemente.

Mediante ciclos se desarrollaron las funciones sobre los proyectiles, para que estos puedan colisionar con las entidades y restar vidas en  caso del jugar, para el caso del enemigo desaparece el enemigo.
Dentro de una condicion se estable que si el puntaje llega a 50 se pase al siguiente nivel y asi cada 50 puntos se sube un nivel hasta el nivel 3.
tambien en una condición se agrego una escepción para guardar el puntaje del usuario.
Tambien se agrego un metodo que al reiniciar el juego mande los parametros tal como se declaraban inicialmente.

### Modeloentidades.py
Se creó una clase Entidad del tipo generico donde los atributos del objeto son ancho, alto, velocidad, posiciones x,y y.
Tambien se creó la clase jugador, que hereda de La clase generica Entidad los atributos, ademas se añade un atributo de objeto llamado vidas, que contabiliza las vidas que tiene el usuario.La entidad enemigo, hereda tambien de la clase Entidad los atributos y solo hereda el metodo mover. Otra clase llamada proyectil se creó bajo el mismo principio en el que la clase hereda de entidad los atributos y ésta solo hereda el metodo mover y dibujar
#### Modelologin.py

Se creo una clase Login para ingresar al juego, en el constructor se definieron publicos los atributos y se paso el parametro UsuarioDAO desde usuarios.dao.

Este modelo contiene metodos para registrar, el cual recibe parametros usuario y contraseña y los agrega al metodo agregar usuario del archivo dao para usuarios

Se creo otro metodo para verificar si al intentar iniciar sesion, que existan los valores de usuario y contraseña, y muestra mensajes de bienvenido o de usuario no registado, si es que existe o no los valores.
### Puntaje_dao.py
Se creo un modelo para guardar el puntaje del usuario.
En este archivo se creo una clase PuntajeDAO que inicializa un archivo  llamado puntajes.json, en caso de que no se encuntre dentro dl proyecto se cea con withopen .
la clase contiene metodos para cargar los puntajes, guardar nuevos puntajes, actualizar puntajes, y obtener puntajes por usuario y totales.
la actualizacion de puntajes se hace para guardar puntajes mayores, que el anterior registrado. obtener puntaje devuelve el puntaje, este metodo se utiliza en el proyecto para mostrar en el juego cual es elpuntaje mas alto del usuario que se ha registrado.

#### usuarios_dao.py
Este arhivo contienen una clase UsuarioDAO que inicializa un archivo json usuarios.json,en caso de que no exista lo crea y si existe lo abre.
esta clase contiene metodos para cargar usuarios, registrar nuevos usuarios, guardar y verificar que existan, estos metodos son escenciales al momento de logearse en el juego. Cuando se intenta agregar un usuario se verifica si ya existe , en dado caso muestra un mensaje de alerta, para verificar se llama entre metodos a cargar usuarios, que lee el archivo json de usuarios, y carga los datos.


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
Aqui se muestra, como es necesario loguearse si el usuario ya se encuentra en el archivo json en su defecto se registra.
![image alt](https://github.com/ASJF996/prj_flet_2025B/blob/main/imagenes_doc/login.png)

El primer ecenario se muestra a continuacion
![image alt](https://github.com/ASJF996/prj_flet_2025B/blob/main/imagenes_doc/escenario1.png)

En la siguiente imagen se muestra la interfaz del juego, cuando se ha perdigo la partida, se muestra el puntaje obtenido y el mayor puntaje que ha obtenido el usuario.
![image alt](https://github.com/ASJF996/prj_flet_2025B/blob/main/imagenes_doc/juego_puntaje.png)
