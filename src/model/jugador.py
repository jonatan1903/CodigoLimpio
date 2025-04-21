class Jugador:

    """
    Representa a un jugador en el juego
    
    Atributos 
    -nombre_usuario: nombre del usuario del jugador
    -contraseña: Contraseña del jugador 
    -Puntaje: puntaje del jugador 

     Metodos

     -cambiar_contraseña(cambiar_contraseña): Cambia la contraseña actual por una nueva
     -actualizar_puntaje(actualizar_puntaje): Suma puntos al puntaje actual y actualiza el puntaje del jugador 

    """

    def __init__(self, nombre_usuario: str, contraseña: str):

        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        self.puntaje = 0

        """
        Inicializa un nuevo jugador con nombre de usuario y contraseña.

        Parámetros:
        - nombre_usuario (str): Nombre del jugador.
        - contraseña (str): Contraseña del jugador.

        """


    def cambiar_contraseña(self, nueva_contraseña: str) -> str:


        if self.validar_contraseña(nueva_contraseña):
            self.contraseña = nueva_contraseña
            print("CONTRASEÑA CAMBIADA CON ÉXITO")
            return "ÉXITO"
        return "ERROR"
    
    """
        Cambia la contraseña del jugador.

        Parámetros:
        - nueva_contraseña (str): Se establece la nueva contraseña que desee el jugador.

        Retorna:
        - str: "ÉXITO" si se cambia correctamente, "ERROR" si la contraseña está vacía.

    """

    def validar_contraseña(self, nueva_contraseña: str) -> bool:


        if not nueva_contraseña:
            print("LA CONTRASEÑA NO PUEDE ESTAR VACÍA")
            return False
        return True
    
    """
        valida que la nueva contrasña no este vacia 
          Parámetros:
        - nueva_contraseña (str): La nueva contraseña ingresada por el usuario.
         Retorna:
        - bool: True si la contraseña es válida (no vacía), False en caso contrario.
        
    """

    def actualizar_puntaje(self, puntos: int) -> int:

        self.puntaje += puntos
        return self.puntaje
    
    """
        Suma puntos al puntaje actual del jugador.

        Parámetros:
        - puntos (int): Cantidad de puntos para sumar.

        Retorna:
        - int: Nuevo puntaje acumulado del jugador.
        
    """
