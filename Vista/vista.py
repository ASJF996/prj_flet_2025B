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
