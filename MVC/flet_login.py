import flet as ft
import subprocess
from dao import UsuarioDAO

def generar_login(page: ft.Page):
    dao = UsuarioDAO()

    username = ft.TextField(label="Usuario")
    password = ft.TextField(label="Contraseña", password=True, can_reveal_password=True)
    mensaje = ft.Text(value="", color="red")

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
            page.window_minimized = True
            subprocess.Popen(["python", "main.py", username.value])
        else:
            mensaje.value = "Usuario o contraseña incorrectos"
            mensaje.color = "red"
            page.update()

    page.add(
        username,
        password,
        ft.Row([
            ft.ElevatedButton("Login", on_click=iniciar_juego),
            ft.ElevatedButton("Registrar", on_click=registrar)
        ]),
        mensaje
    )

def main():
    ft.app(target=generar_login)

if __name__ == "__main__":
    main()
