from src.model.jugador import Jugador

class Puntuaciones:

    """
    Clase para gestionar y mostrar las puntuaciones de los jugadores.

    Atributos:
    - lista_puntuaciones (list): Lista de diccionarios que contienen el nombre de usuario y su puntaje.

    Métodos:
    - actualizar_puntuacion(jugador): Actualiza o agrega la puntuación de un jugador.
    - mostrar_puntuaciones(): Muestra por consola la tabla de puntuaciones.
    
    """

    def __init__(self):

        self.lista_puntuaciones = []

        """
        Inicializa una instancia de Puntuaciones con una lista vacía.

        """

    def actualizar_puntuacion(self, jugador: Jugador):
        
        encontrado = False
        for registro in self.lista_puntuaciones:
            if registro["nombre_usuario"] == jugador.nombre_usuario:
                registro["puntaje"] = jugador.puntaje
                encontrado = True
                break
        
       
        if not encontrado:
            self.lista_puntuaciones.append({
                "nombre_usuario": jugador.nombre_usuario,
                "puntaje": jugador.puntaje
            })

        """
        Actualiza la puntuación de un jugador en la tabla.

        Si el jugador ya existe en la tabla, se actualiza su puntaje.
        Si no existe, se añade un nuevo registro con su nombre y puntaje.

        Parámetros:
        - jugador (Jugador): Objeto de tipo Jugador con nombre y puntaje actualizado.

        """

    def mostrar_puntuaciones(self):

        print("\nTABLA DE PUNTUACIONES:")
        for i, registro in enumerate(self.lista_puntuaciones, start=1):
            print(f"{i}. {registro['nombre_usuario']} - {registro['puntaje']} puntos")

    """
        Imprime en consola la tabla de puntuaciones de todos los jugadores registrados.

    """