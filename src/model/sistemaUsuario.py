from src.model.jugador import Jugador  
from src.model.puntuaciones import Puntuaciones  

class SistemaJugador:

    """
    Clase que gestiona el sistema de usuarios y puntuaciones del juego.

    Atributos:
    - jugadores_registrados (list): Lista de objetos Jugador registrados.
    - puntuaciones (Puntuaciones): Objeto para gestionar la tabla de puntuaciones.

    Métodos:
    - registrar_jugador(nombre_usuario, contraseña): Registra un nuevo jugador si el usuario no existe.
    - iniciar_sesion(nombre_usuario, contraseña): Verifica las credenciales e inicia sesión.
    - actualizar_puntaje(nombre_usuario, puntos): Suma puntos al jugador y actualiza la tabla de puntuaciones.

    """

    def __init__(self):

        self.jugadores_registrados = [] 
        self.puntuaciones = Puntuaciones()  

        """
        Inicializa el sistema con una lista vacía de jugadores y una instancia de Puntuaciones.

        """

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
    
    """
        Registra un nuevo jugador si el nombre de usuario no existe previamente.

        Parámetros:
        - nombre_usuario (str): Nombre del nuevo usuario.
        - contraseña (str): Contraseña del nuevo usuario.

        Retorna:
        - bool: True si el registro fue exitoso, False en caso de error.

    """

    def iniciar_sesion(self, nombre_usuario: str, contraseña: str) -> Jugador:

       
        for j in self.jugadores_registrados:
            if j.nombre_usuario == nombre_usuario and j.contraseña == contraseña:
                print("INICIO DE SESIÓN EXITOSO")
                return j  
        
        print("NOMBRE DE USUARIO O CONTRASEÑA INCORRECTOS")
        return None
    
    """
        Inicia sesión para un jugador registrado, validando las credenciales.

        Parámetros:
        - nombre_usuario (str): Nombre del usuario.
        - contraseña (str): Contraseña del usuario.

        Retorna:
        - Jugador: El objeto Jugador si las credenciales son correctas.
        - None: Si el usuario o la contraseña no coinciden.

    """
    
    def actualizar_puntaje(self, nombre_usuario: str, puntos: int):

        
        for j in self.jugadores_registrados:
            if j.nombre_usuario == nombre_usuario:
                j.actualizar_puntaje(puntos)
                self.puntuaciones.actualizar_puntuacion(j)
                print(f"PUNTAJE ACTUALIZADO: {j.nombre_usuario} - {j.puntaje} puntos")
                return
        print("JUGADOR NO ENCONTRADO")

    """
        Actualiza el puntaje de un jugador específico y lo refleja en la tabla de puntuaciones.

        Parámetros:
        - nombre_usuario (str): Nombre del jugador al que se le sumarán puntos.
        - puntos (int): Cantidad de puntos a agregar.
        
    """
