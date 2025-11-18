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
