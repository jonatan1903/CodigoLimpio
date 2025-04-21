
from src.model.juego import ComienzaElJuego
from src.model.sistemaUsuario import SistemaJugador
from src.model.puntuaciones import Puntuaciones

class ControladorBatallaNaval:
    def __init__(self):
        self.sistema = SistemaJugador()
        self.sistema.puntuaciones = Puntuaciones()
        self.juego = None
        self.jugador_activo = None

    def registrar_jugador(self, nombre, contraseña):
        return self.sistema.registrar_jugador(nombre, contraseña)

    def iniciar_sesion(self, nombre, contraseña):
        jugador = self.sistema.iniciar_sesion(nombre, contraseña)
        if jugador:
            self.jugador_activo = jugador
            return True
        return False

    def iniciar_juego(self, ancho, alto, num_naves):
        self.juego = ComienzaElJuego(alto, ancho, num_naves)

    def obtener_tablero(self):
        if self.juego:
            return self.juego.campo.tablero
        return []

    def realizar_disparo(self, x, y):
        if self.juego:
            impacto = self.juego.campo.evaluar_disparo_en_tablero(x, y)
            return impacto  

    def juego_terminado(self):
        if self.juego:
            return self.juego.verificar_ganador()
        return False

    def reiniciar_juego(self):
        if self.juego:
            self.juego.reiniciar_juego()

    def actualizar_puntaje(self, puntos=10):
        if self.jugador_activo:
            self.sistema.actualizar_puntaje(self.jugador_activo.nombre_usuario, puntos)

    def obtener_puntuaciones(self):
        return self.sistema.puntuaciones.lista_puntuaciones
