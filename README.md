# Videojuego en Python
Este proyecto conjunto consiste en un videojuego similar al clásico de arcade: Gálaga. Recordar que la mecánica del juego es de disparos, el protagonista del juego es una navecita espacial que se desplaza únicamente en dos direcciones: izquierda y derecha. Y se deben esquivar los disparos y las colisiones de naves enemigas que igualmente nos lanzan proyectiles.
El objetivo general del juego es básicamente obtener el mayor puntaje posible, siguiendo la mecánica descrita anteriormente.
El videojuego está desarrollado completamente en Python, con tecnologías inherentes al mismo, estas tecnologías son la librería pygame y Flet, en las que se ahondará a continuación:
### pygame
Es una librería gratuita, multiplataforma y de código abierto para crear aplicaciones multimedia de manera sencilla. Y se eligió para este proyecto porque es una excelente opción para el desarrollo de videojuegos en 2D, lo cúal es el caso.

Se puede instalar fácilmente con pip desde la terminal o el Bash ingresando el siguiente comando:
```
pip install pygame
```
### Flet
Flet es un framework de Python que permite crear aplicaciones web, móviles y de escritorio de manera sencilla, usando la potencia de Flutter pero sin la necesidad de escribir código en Dart ni tener experiencia previa en el desarrollo de frontend.

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
### Sistema de autenticación

### Gestión de usuarios

### Sistema de puntuaciones

### API y endpoints

## Estructura del proyecto
El proyecto se compone de los siguientes archivos, scripts, imágenes, etc. Que en su conjunto crean toda la funcionalidad del videojuego:
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
├── flet_login.py # Sistema de autenticación externo (Flet)
├── usuarios.json # Base de datos de usuarios
├── puntajes.json # Base de datos de puntuaciones
└── README.md # Documentación del proyecto
```


