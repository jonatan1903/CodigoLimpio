from src.model.jugador import Jugador  
from src.model.puntuaciones import Puntuaciones  

class SistemaJugador:
    def __init__(self):
        self.jugadores_registrados = [] 
        self.puntuaciones = Puntuaciones()  

    def registrar_jugador(self, nombre_usuario: str, contraseña: str) -> bool:
       
        if not nombre_usuario.strip():
            print("ERROR: El nombre de usuario no puede estar vacío o contener solo espacios.")
            return False

      
        if not contraseña:
            print("ERROR: La contraseña no puede estar vacía.")
            return False

        
        for j in self.jugadores_registrados:
            if j.nombre_usuario == nombre_usuario:
                print("ERROR: El usuario ya existe.")
                return False

        
        nuevo_jugador = Jugador(nombre_usuario, contraseña)
        self.jugadores_registrados.append(nuevo_jugador)
        print("USUARIO REGISTRADO CON ÉXITO")
        return True

    def iniciar_sesion(self, nombre_usuario: str, contraseña: str) -> Jugador:
       
        for j in self.jugadores_registrados:
            if j.nombre_usuario == nombre_usuario and j.contraseña == contraseña:
                print("INICIO DE SESIÓN EXITOSO")
                return j  
        
        print("NOMBRE DE USUARIO O CONTRASEÑA INCORRECTOS")
        return None
    
    def actualizar_puntaje(self, nombre_usuario: str, puntos: int):
        
        for j in self.jugadores_registrados:
            if j.nombre_usuario == nombre_usuario:
                j.actualizar_puntaje(puntos)
                self.puntuaciones.actualizar_puntuacion(j)
                print(f"PUNTAJE ACTUALIZADO: {j.nombre_usuario} - {j.puntaje} puntos")
                return
        print("JUGADOR NO ENCONTRADO")
