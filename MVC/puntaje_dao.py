import json
import os

class PuntajeDAO:
    def __init__(self, archivo="puntajes.json"):
        self.archivo = archivo
        if not os.path.exists(self.archivo):
            with open(self.archivo, "w", encoding="utf-8") as f:
                json.dump({}, f)

    def cargar_puntajes(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def guardar_puntajes(self, puntajes):
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(puntajes, f, indent=4)

    def actualizar_puntaje(self, usuario, puntaje):
        if not usuario:
            return False
        puntajes = self.cargar_puntajes()
        mejor = puntajes.get(usuario, 0)
        if puntaje > mejor:
            puntajes[usuario] = puntaje
            self.guardar_puntajes(puntajes)
            return True
        return False

    def obtener_puntaje(self, usuario):
        puntajes = self.cargar_puntajes()
        return puntajes.get(usuario, 0)

    def obtener_todos(self):
        return self.cargar_puntajes()
