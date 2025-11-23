import pygame

from Modelos.usuarios_dao import UsuarioDAO

class Login:
    def __init__(self, dao: UsuarioDAO):
        self.dao = dao
        self.usuario_ingresado = ""
        self.contraseña_ingresada = ""
        self.escribiendo_usuario = True
        self.login_exitoso = False
        self.usuario_logueado = ""  # nombre del usuario que quedó logueado

    def registrar_usuario(self, usuario, contraseña):
        try:
            self.dao.agregar_usuario(usuario, contraseña)
            return True
        except ValueError:
            return False

    def procesar_tecla(self, tecla):
        if self.login_exitoso:
            return
        if tecla == pygame.K_BACKSPACE:
            if self.escribiendo_usuario:
                self.usuario_ingresado = self.usuario_ingresado[:-1]
            else:
                self.contraseña_ingresada = self.contraseña_ingresada[:-1]
        elif tecla == pygame.K_RETURN:
            if self.escribiendo_usuario:
                self.escribiendo_usuario = False
            else:
                if self.dao.verificar_usuario(self.usuario_ingresado, self.contraseña_ingresada):
                    self.login_exitoso = True
                    self.usuario_logueado = self.usuario_ingresado
                else:
                    self.usuario_ingresado = ""
                    self.contraseña_ingresada = ""
                    self.escribiendo_usuario = True
        else:
            letra = pygame.key.name(tecla)
            if len(letra) == 1:
                if self.escribiendo_usuario:
                    self.usuario_ingresado += letra
                else:
                    self.contraseña_ingresada += letra
