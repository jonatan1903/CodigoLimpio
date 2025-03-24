class Jugador:
    def __init__(self, nombre_usuario: str, contraseña: str):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        self.puntaje = 0

    def cambiar_contraseña(self, nueva_contraseña: str) -> str:
        if not nueva_contraseña:
            print("LA CONTRASEÑA NO PUEDE ESTAR VACÍA")
            return "ERROR"
        
        self.contraseña = nueva_contraseña
        print("CONTRASEÑA CAMBIADA CON ÉXITO")
        return "ÉXITO"

    def actualizar_puntaje(self, puntos: int) -> int:
        self.puntaje += puntos
        return self.puntaje
