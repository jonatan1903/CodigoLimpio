class Jugador:
    def __init__(self, nombre_usuario: str, contraseña: str):

        
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        self.puntaje = 0

    def cambiar_contraseña(self, nueva_contraseña: str) -> str:
        pass

    def actualizar_puntaje(self, puntos: int) -> int:
        pass