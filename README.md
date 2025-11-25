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

## Arquitectura del sistema
Se emplearon únicamente dos patrones de diseño: MVC y DAO. Que tuvieron una destacada influencia en la estructuración y lógica del código.
[comentario]: # Aquí voy a poner una imagen que represente la estructura del Modelo Vista Controlador y el Data Access Object
### (MVC) Modelo Vista Controlador
- Modelo: Gestiona el estado y lógica del juego (Modelos/)
- Vista: Maneja la representación visual (Vista/)
- Controlador: Coordina la interacción entre ambos (Controlador/)
### (DAO) Data Access Object
- usuarios_dao.py: Gestiona usuarios y contraseñas
- puntaje_dao.py: Maneja los puntajes máximos por usuario
- Persistencia: Archivos JSON para almacenamiento simple

## Diagramación del proyecto
Aquí se muestran los diagramas tanto de clase como de casos de uso que se bosquejaron para el desarrollo de este proyecto.
### Diagrama de clases
-- Pendiente
### Diagrama de casos de uso
-- Pendiente

## Características principales del proyecto
Este proyecto posee características que vale la pena mencionar en aspectos tanto de funcionalidad, gestión, diseño, lógica, etc., que se presentan a continuación:
### 1. Sistema de autenticación
Posee un sistema de login **flet_login.py** que lanza el juego principal **main.py** pasando al usuario como argumento.
### 2. Utilización de clases genéricas
Dentro de la parte del modelo existe un uso notorio e importante de clase genéricas, concretamente dentro del archivo **Modeloentidades.py** donde existe una clase genérica llamada **Entidad**
### 3. Persistencia de datos
Utiliza archivos json para almacenar usuarios con sus respectivas contraseñas y puntuaciones. Y aquí el DAO (Data Access Object) se encarga de abstraer el acceso a estos archivos.
### 4. Control de estados bien definido
El juego posee tres estados claros y bien definidos: login, gameplay y game over. Y el controlador se encarga de manejar la transición entre estados.
### 5. HUD (Head Up Display)
Durante el gameplay se muestra en la parte superior izquierda información en tiempo real. Se muestran tus vidas, tu puntaje y el nivel actual.

## Estructura del proyecto
El proyecto se compone de los siguientes archivos, scripts, imágenes, etc. Que en su conjunto crean toda la funcionalidad del videojuego. Se muestra una breve descripción de cada uno:
```
prj_flet_2025B/
├── Controlador/              # Lógica de control
│   ├── controlador.py        # Coordinador principal MVC
│   └── __init__.py
├── Modelos/                  # Capa de datos y lógica
│   ├── Modeloentidades.py    # Entidades genéricas del juego
│   ├── Modelojuego.py        # Lógica principal del juego
│   ├── modelologin.py        # Sistema de login (PyGame)
│   ├── puntaje_dao.py        # DAO para gestión de puntajes
│   ├── usuarios_dao.py       # DAO para gestión de usuarios
│   └── __init__.py
├── Vista/                    # Capa de presentación
│   ├── vista.py              # Renderizado PyGame
│   ├── flet_login.py         # Interfaz de autenticación Flet
│   ├── main.py               # Punto de entrada del juego
│   ├── assets/               # Recursos gráficos
│   │   ├── jugador.png       # Sprite del jugador
│   │   ├── enemigo.png       # Sprite de enemigos
│   │   ├── andromeda.jpg     # Fondo nivel 1
│   │   ├── planetas.jpg      # Fondo nivel 2
│   │   └── saturno.jpg       # Fondo nivel 3
│   └── __init__.py
├── Diagramas/                # Diagramas de arquitectura
├── imagenes_doc/             # Imágenes para documentación
├── usuarios.json             # Base de datos de usuarios
├── puntajes.json             # Base de datos de puntuaciones
└── README.md                 # Documentación del proyecto
```

## Módulos y componentes del Modelo Vista Controlador
Esta es quizá la sección más importante, pues el proyecto sigue fielmente (y de manera muy notoria) este patrón de diseño. Como se mostró en la sección anterior, se creó una carpeta para cada elemento de este modelo, y es en esta sección que se profundizará sobre la funcionalidad de cada una.
### Modelo
Esta carpeta conformadad de varios scripts se encarga completamente de gestionar los estados del juego y la lógica.
#### Modelojuego.py
El archivo Modelojuego.py es una parte escencial en el desarrollo del proyecto, en el se encuentra toda la logica del Juego, en esta parte del MVC se programó todas las reglas del juego. y las funciones que realizan las entidades dentro del proyecto, en esta parte del codigo tenemos todas las operaciones que se crean en el juego. 
Primero se importan todas las librerias necesarias, en este caso, se importó pygame,random,time,os y de los archivos creados se importó USUARIODAO del archivo dao.py y de puntaje_dao se importo PuntajeDAO, tambien de Modelosentidades se importaron jugador,proyectil y enemigo.
Dentro de nuestra clase Modelojuego tenemos un metodo especial __init__ que tiene los atributos de pantalla, este nos sirve para el login al juego, dentro del def, declaramos publicos los atributos.
En un ciclo  agregamos los fondos o escenarios asignando la ruta de donde se encuentran las imagenes en nuestro proyecto, y mediante el metodo Surface de pygame le damos el formato de fondo.
luego se creo el metodo crear_enemigo, que crea la imagen del enemigo y mediante randit posiciona la imagen en diferentes  lugares de la pantalla, mediante un excep busca la ruta de la imagen que se le da si no se encuentra obtiene una de pygame.
Despues se agregaron metodos disparar para el jugador principal y dosparar_enemigo para la entidad enemigo, así como tambien se creo un metodo para actualizar, que genera entidades enemigo constantemente.
Mediante ciclos se desarrollaron las funciones sobre los proyectiles, para que estos puedan colisionar con las entidades y restar vidas en  caso del jugar, para el caso del enemigo desaparece el enemigo.
Dentro de una condicion se estable que si el puntaje llega a 50 se pase al siguiente nivel y asi cada 50 puntos se sube un nivel hasta el nivel 3.
tambien en una condición se agrego una escepción para guardar el puntaje del usuario.
Tambien se agrego un metodo que al reiniciar el juego mande los parametros tal como se declaraban inicialmente.
#### Modeloentidades.py
Se creó una clase Entidad del tipo generico donde los atributos del objeto son ancho, alto, velocidad, posiciones x,y y.
Tambien se creó la clase jugador, que hereda de La clase generica Entidad los atributos, ademas se añade un atributo de objeto llamado vidas, que contabiliza las vidas que tiene el usuario.La entidad enemigo, hereda tambien de la clase Entidad los atributos y solo hereda el metodo mover. Otra clase llamada proyectil se creó bajo el mismo principio en el que la clase hereda de entidad los atributos y ésta solo hereda el metodo mover y dibujar
#### Modelologin.py
Se creo una clase Login para ingresar al juego, en el constructor se definieron publicos los atributos y se paso el parametro UsuarioDAO desde usuarios.dao.
Este modelo contiene metodos para registrar, el cual recibe parametros usuario y contraseña y los agrega al metodo agregar usuario del archivo dao para usuarios
Se creo otro metodo para verificar si al intentar iniciar sesion, que existan los valores de usuario y contraseña, y muestra mensajes de bienvenido o de usuario no registado, si es que existe o no los valores.
#### Puntaje_dao.py
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
Sen encarga las pantallas y los elementos graficos que existen en ella, se van actualizando con ciclos, los enemigos, los proyectiles el puntaje, todo se va actualizando y vista se encarga de mostrar esas actualizaciones
#### assets/
Esta carpeta contiene todos lo elementos multimedia del juego, contiene las imágenes de las navecitas y los fondos.


![image alt](https://github.com/ASJF996/prj_flet_2025B/blob/ea1236a1ba5a50dfb15561530efb8309bfc00a91/imagenes_doc/assets.png)




### Controlador
Es un intermediario entre el modelo y la vista, mejor dicho es quién coordina ambos. No contiene lógica de negocio ni lógica visual.
Se compone únicamente del siguiente script:
#### controlador.py
Este script se encarga de manejar los datos de entrada, controlar el flujo de la aplicación y controlar el bucle principal del juego.
Practicamente esta parte del programa se ocupa de recibir las entradas al programa hechas por el usuario, posteriormente se las manda al modelo y este  se encarga de procesar la logica, una vez realizada las acciones correspondientes,el controlador , se conecta con vista y le dice que deberia mostrar.

## Flujo del programa
El funcionamiento del videojuego se divide en tres grandes bloques: autenticación, transición al juego y ejecución del juego.
### 1. Autenticación 
```
Ejecutar flet_login.py
    ↓
Interfaz Flet muestra formulario
    ↓
Usuario se registra o inicia sesión
    ↓
Validación contra usuarios.json
    ↓
```
[ÉXITO] → Lanza main.py con usuario como argumento
[ERROR] → Muestra mensaje de error
### 2. Transición al juego
```
Flet minimiza su ventana
    ↓
subprocess.Popen ejecuta main.py
    ↓
Paso de usuario como argumento
    ↓
Controlador inicia con usuario pre-autenticado
    ↓
```
Saltea pantalla de login de PyGame
### 3. Ejecución del juego
```
Bucle principal a 60 FPS
    ↓
Actualización continua del modelo
    ↓
Renderizado mediante vista PyGame
    ↓
Detección de colisiones y eventos
    ↓
Persistencia automática de puntajes al game over
```
## Ejecución del Programa
Como se mencionó anteroirmente, se ejecuta desde el archivo **flet_login.py**, al ejecutar nos desplegará la interfaz de flet. Y tendremos que loguearnos.
Aqui se muestra, como es necesario loguearse si el usuario ya se encuentra en el archivo json en su defecto se registra.
![image alt](https://github.com/ASJF996/prj_flet_2025B/blob/main/imagenes_doc/login.png)

El primer ecenario se muestra a continuacion
![image alt](https://github.com/ASJF996/prj_flet_2025B/blob/main/imagenes_doc/escenario1.png)

En la siguiente imagen se muestra la interfaz del juego, cuando se ha perdigo la partida, se muestra el puntaje obtenido y el mayor puntaje que ha obtenido el usuario.
![image alt](https://github.com/ASJF996/prj_flet_2025B/blob/main/imagenes_doc/juego_puntaje.png)
