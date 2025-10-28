import flet as ft
import random
import time
import threading

usuarios_db = {}

def guardar_usuario(usuario, contraseña):
    if usuario in usuarios_db:
        return False
    usuarios_db[usuario] = contraseña
    return True

def login(usuario, contraseña):
    return usuario in usuarios_db and usuarios_db[usuario] == contraseña

class Nave:
    def __init__(self):
        self.posicion = [225, 420]
        self.salud = 100

    def mover(self, direccion):
        if direccion == "arriba" and self.posicion[1] > 0:
            self.posicion[1] -= 20
        elif direccion == "abajo" and self.posicion[1] < 450:
            self.posicion[1] += 20
        elif direccion == "izquierda" and self.posicion[0] > 0:
            self.posicion[0] -= 20
        elif direccion == "derecha" and self.posicion[0] < 450:
            self.posicion[0] += 20

class Enemigo:
    def __init__(self, x, y):
        self.posicion = [x, y]
        self.salud = 50
        self.direccion = 1

    def mover(self):
        if self.posicion[0] >= 450:
            self.direccion = -1
        elif self.posicion[0] <= 0:
            self.direccion = 1
        self.posicion[0] += 5 * self.direccion

def main(page: ft.Page):
    page.title = "🚀 Juego Espacial"
    page.window_width = 500
    page.window_height = 500
    page.bgcolor = "blue"

    nave_img = "assets/nave.png"
    enemigo_img = "assets/enemigo.png"
    fondo_img = "assets/fondo_espacial.jpg"
    bala_img = "assets/bala.png"

    usuario_input = ft.TextField(label="Usuario")
    contra_input = ft.TextField(label="Contraseña", password=True)

    def mostrar_login():
        page.clean()
        page.add(
            ft.Column([
                ft.Image(src=nave_img, width=100),
                ft.Text("🪐 Bienvenido al Juego Espacial🪐", size=20, color="white"),
                usuario_input,
                contra_input,
                ft.ElevatedButton("Iniciar sesión", on_click=iniciar_juego),
                ft.TextButton("¿No tienes cuenta? Regístrate", on_click=mostrar_registro)
            ], alignment="center", horizontal_alignment="center")
        )

    def mostrar_registro(e):
        page.clean()
        nuevo_usuario = ft.TextField(label="Nuevo usuario")
        nueva_contra = ft.TextField(label="Nueva contraseña", password=True)

        def registrar(e):
            if guardar_usuario(nuevo_usuario.value.strip(), nueva_contra.value.strip()):
                page.snack_bar = ft.SnackBar(ft.Text("✅ Usuario registrado"))
                page.snack_bar.open = True
                mostrar_login()
            else:
                page.snack_bar = ft.SnackBar(ft.Text("❌ Usuario ya existe"))
                page.snack_bar.open = True
            page.update()

        page.add(
            ft.Column([
                ft.Text("🧑‍🚀 Registro", size=20, color="white"),
                nuevo_usuario,
                nueva_contra,
                ft.ElevatedButton("Registrar", on_click=registrar),
                ft.TextButton("Volver al login", on_click=lambda e: mostrar_login())
            ], alignment="center", horizontal_alignment="center")
        )

    def iniciar_juego(e):
        usuario = usuario_input.value.strip()
        contraseña = contra_input.value.strip()
        if login(usuario, contraseña):
            mostrar_juego()
        else:
            page.snack_bar = ft.SnackBar(ft.Text("❌ Credenciales inválidas"))
            page.snack_bar.open = True
            page.update()

    def mostrar_juego():
        page.clean()

        nave = Nave()
        enemigos = [Enemigo(random.randint(0, 450), random.randint(30, 120)) for _ in range(5)]

        salud_txt = ft.Text(f"❤️ Salud: {nave.salud}", color="white")
        resultado_txt = ft.Text("", color="white", size=20)

        fondo = ft.Image(src=fondo_img, width=500, height=500, fit=ft.ImageFit.COVER)

        nave_visual = ft.Image(src=nave_img, width=50, left=nave.posicion[0], top=nave.posicion[1])
        enemigos_visual = [
            ft.Image(src=enemigo_img, width=40, left=e.posicion[0], top=e.posicion[1])
            for e in enemigos
        ]

        stack = ft.Stack(controls=[fondo, *enemigos_visual, nave_visual])

        def actualizar_pantalla():
            nave_visual.left = nave.posicion[0]
            nave_visual.top = nave.posicion[1]
            salud_txt.value = f"❤️ Salud: {nave.salud}"

            for i, e in enumerate(enemigos):
                enemigos_visual[i].left = e.posicion[0]
                enemigos_visual[i].top = e.posicion[1]

            if nave.salud <= 0:
                resultado_txt.value = "💀 GAME OVER"
                controles.disabled = True
            elif len(enemigos) == 0:
                resultado_txt.value = "🎉 ¡Ganaste!"
                controles.disabled = True

            page.update()

        def mover(direccion):
            if nave.salud <= 0 or len(enemigos) == 0:
                return
            nave.mover(direccion)
            for enemigo in enemigos:
                if abs(nave.posicion[0] - enemigo.posicion[0]) < 40 and abs(nave.posicion[1] - enemigo.posicion[1]) < 40:
                    nave.salud -= 5
            actualizar_pantalla()

        def disparar(e):
            if nave.salud <= 0 or len(enemigos) == 0:
                return

            bala = ft.Container(width=5, height=15, bgcolor="yellow",
                                top=nave.posicion[1], left=nave.posicion[0] + 20)
            stack.controls.append(bala)
            page.update()

            def mover_bala():
                while bala.top > 0:
                    time.sleep(0.03)
                    bala.top -= 10
                    for i, enemigo in enumerate(enemigos):
                        if abs(bala.top - enemigo.posicion[1]) < 30 and abs(bala.left - enemigo.posicion[0]) < 30:
                            enemigo.salud -= 25
                            if enemigo.salud <= 0:
                                enemigos.pop(i)
                                stack.controls.remove(enemigos_visual[i])
                                enemigos_visual.pop(i)
                            if bala in stack.controls:
                                stack.controls.remove(bala)
                            actualizar_pantalla()
                            return
                    page.update()
                if bala in stack.controls:
                    stack.controls.remove(bala)
                actualizar_pantalla()

            threading.Thread(target=mover_bala).start()

        controles = ft.Row([
            ft.IconButton(icon="arrow_upward", on_click=lambda e: mover("arriba")),
            ft.IconButton(icon="arrow_downward", on_click=lambda e: mover("abajo")),
            ft.IconButton(icon="arrow_back", on_click=lambda e: mover("izquierda")),
            ft.IconButton(icon="arrow_forward", on_click=lambda e: mover("derecha")),
            ft.IconButton(icon="bolt", on_click=disparar),
        ], alignment="center")

        page.add(ft.Column([
            salud_txt,
            resultado_txt,
            stack,
            controles
        ]))

        def mover_enemigos():
            while nave.salud > 0 and len(enemigos) > 0:
                for enemigo in enemigos:
                    enemigo.mover()
                    if abs(nave.posicion[0] - enemigo.posicion[0]) < 40 and abs(nave.posicion[1] - enemigo.posicion[1]) < 40:
                        nave.salud -= 5
                actualizar_pantalla()
                time.sleep(0.3)

        threading.Thread(target=mover_enemigos, daemon=True).start()
        actualizar_pantalla()

    mostrar_login()

ft.app(target=main)
