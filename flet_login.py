import flet as ft
import subprocess
import os
from Modelos.usuarios_dao import UsuarioDAO

def generar_login(page: ft.Page):
    dao = UsuarioDAO()

    page.title = "Login - Juego MVC"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20
    page.bgcolor = "#E3F2FD"

    username = ft.TextField(label="Usuario", width=300, autofocus=True)
    password = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300)
    mensaje = ft.Text(value="", color="red", size=16)

   
    ruta_main = os.path.join(os.path.dirname(__file__), "main.py")

    def registrar(e):
        try:
            dao.agregar_usuario(username.value, password.value)
            mensaje.value = "Usuario registrado correctamente."
            mensaje.color = "green"
        except ValueError:
            mensaje.value = "Nombre de usuario ya existe."
            mensaje.color = "red"
        page.update()

    def iniciar_juego(e):
        if dao.verificar_usuario(username.value, password.value):
            mensaje.value = f"Bienvenido, {username.value}"
            mensaje.color = "green"
            page.update()

            # Minimizamos la ventana
            page.window_minimized = True

            # Ejecutamos main.py con subprocess
            subprocess.Popen(["python", ruta_main, username.value])
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
