# Videojuego en Python
Este proyecto es un videojuego similar al clásico de arcade: Gálaga. Desarrollado en Python además de la implementación de otras tecnologías y patrones de diseño, así como una fuerte utilización del paradigma de programación orientada a objetos. 
El modo de juego de este proyecto es basicamente disparar y esquivar ataques de enemigos, que hacen lo mismo. Se presentan múltiples niveles con fondos dirferentes, enemigos que nos atacan, así como un sistema de vida y puntuación.

## Software utilizado
Como se mencionó anteriormente, se empleó el lenguaje de programación Python en la totalidad del proyecto, así como componentes inherentes al mismo tales como la librería pygame y flet, que se explican a continuación:
### pygame
Es una librería de Python, gratuita y de código abierto para el desarrolló de aplicaciones multimedia, especialmente videojuegos en 2D. Ésta fue de suma importancia en este proyecto para el manejo de los gráficos y el input del usuario a través del teclado para realizar las acciones como desplazarse y disparar, así como para reiniciar la partida una vez perdido el juego. 
### Flet
Flet es un framework muy conocido de Python para interfaz de usuario enriquecido, que permite crear de manera rápida y sencilla aplicaciones web, de escritorio y/o móviles interactivas; ésto sin la necesidad de poseer conocimientos previoos de HTML, JavaScript o estilos CSS.
Para este proyecto en concreto se utilizó para el desarrollo de la interfaz de usuario en la que el jugador (usuario) tiene que loguearse, o registrarse en si defecto.

## Características principales
A continuación se muestran carácterísticas destacables del proyecto.
### Arquitectura Modelo Vista Controlador
Este fue un factor clave en el desarrollo, permitió separar de manera clara las funcionalidades de las partes principales del código. Más adelante se ahondará en las clases que componen cada una de las funcionalidades mencionadas anteriormente.

## Patrones de diseño aplicados
Se emplearon únicamente dos patrones de diseño: MVC y DAO. Que tuvieron una destacada influencia en la estructuración y lógica del código.
### (MVC) Modelo Vista Controlador
El modelo realiza la representación del estado y los datos del juego; contiene las entidades, la lógica y el negocio del juego.
La vista se encarga exclusivamente de representar visualmente el juego, solo recibe datos del usuario y los muestra.
Y por último el controlador se ocupa de manejar el input de usuario y actualizar los datos del modelo en consecuencia, así como de coordinar la actualización de la vista.
### (DAO) Data Access Object


## Estructutura del proyecto
Esta sección es de crucial importancia, ya que se va a explicar detalladamente cada componente del proyecto
