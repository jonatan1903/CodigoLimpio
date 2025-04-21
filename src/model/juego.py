from src.model.campo import Campo

class ComienzaElJuego:


    """
    Controlador principal del juego de naves.

    Esta clase se encarga de manejar la lógica del juego, incluyendo disparos, verificación
    de victoria y reinicio del campo de batalla.

    Atributos:
    - campo (Campo): Instancia del campo de juego donde se colocan y atacan las naves.

    Métodos:
    - realizar_disparo(x, y): Ejecuta un disparo sobre una celda del campo e imprime el resultado.
    - verificar_ganador(): Verifica si ya no quedan naves.
    - reiniciar_juego(): Reinicia el campo de juego con los mismos parámetros iniciales.

    """ 

    def __init__(self, alto: int, ancho: int, num_naves: int):

        self.campo = Campo(ancho, alto, num_naves)

        """
        Inicializa una nueva partida del juego.

        Parámetros:
        - alto (int): Número de filas del campo.
        - ancho (int): Número de columnas del campo.
        - num_naves (int): Número total de naves que se deben colocar.

        """

    def realizar_disparo(self, x: int, y: int):

        impacto = self.campo.evaluar_disparo_en_tablero(x, y)
        if impacto:
            print("¡Impacto en una nave!")
        else:
            print("Disparo al agua.")

        """ 
        Realiza el disparo en la posicion indicada.

        parametros:
        x (int):  Fila del disparo
        y (int): Columna del disparo 

        """
        
    def verificar_ganador(self) -> bool:


        return not self.campo.QuedanNaves()

    """
        Verifica si el jugador ha destruido todas las naves.

        Retorna:
        - bool: True si no quedan naves, False en caso contrario.

    """    

    def reiniciar_juego(self):

        ancho, alto, num_naves = self.campo.ancho, self.campo.alto, self.campo.num_naves
        self.campo = Campo(ancho, alto, num_naves)
        print("El juego ha sido reiniciado.")

    """
        Reinicia el juego con las mismas dimensiones y numero de naves 
    """