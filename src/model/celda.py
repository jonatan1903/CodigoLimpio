class Celda:

    """
    Representa una celda del campo de juego.

    Atributos:
    - contiene_nave (bool): Indica si la celda contiene una nave.
    - impactada (bool): Indica si la celda ha sido impactada por un disparo.

    Métodos:
    - recibir_disparo(): Marca la celda como impactada y retorna si contenía una nave.
    - _str_(): Representa el estado de la celda como un carácter visual.
        - '~' si no ha sido impactada.
        - 'X' si fue impactada y contenía una nave.
        - 'O' si fue impactada pero estaba vacía.
    """

    def __init__(self, contiene_nave=False):
        self.contiene_nave = contiene_nave
        self.impactada = False


    def recibir_disparo(self):

        if self.impactada:
            raise ValueError("Esta celda ya ha sido impactada")
        
        self.impactada = True
        return self.contiene_nave
    
    """
        Marca la celda como impactada.

        Returns:
            bool: True si la celda contenía una nave, False en caso contrario.

        Raises:
            ValueError: Si la celda ya había sido impactada previamente.

    """


    def __str__(self):


        if not self.impactada:
            return "~"
        return "X" if self.contiene_nave else "O"

    """
        Devuelve una representación visual del estado de la celda.

        Return:
            str: '~' si no ha sido impactada, 'X' si tenía una nave y fue impactada,
                 'O' si fue impactada pero estaba vacía.
    """