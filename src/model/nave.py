class Nave:

    """
    Representa una nave en el campo de juego.

    Atributos:
    - posicion (list[tuple]): Lista de coordenadas (fila, columna) donde se encuentra la nave.
    - impactos (set): Conjunto de coordenadas que ya han sido impactadas.

    Métodos:
    - verificar_impacto(coordenada): Verifica si una coordenada impacta la nave y la marca.
    - esta_destruida(): Determina si todas las partes de la nave han sido impactadas.
    
    """

    def __init__(self, posicion: list):

        self.posicion = posicion  
        self.impactos = set() 

        """
        Inicializa una nueva nave en el campo.

        Parámetros:
        - posicion (list[tuple]): Lista de coordenadas que representan las partes de la nave.
        """

    def verificar_impacto(self, coordenada: tuple) -> bool:

        if coordenada in self.posicion and coordenada not in self.impactos:
            self.impactos.add(coordenada)  
            return True
        return False
    
    """
        Verifica si una coordenada corresponde a una parte de la nave y no ha sido impactada antes.

        Parámetros:
        - coordenada (tuple): Coordenada del disparo (fila, columna).

        Retorna:
        - bool: True si la coordenada impacta la nave, False en caso contrario.
    """
    
    def esta_destruida(self) -> bool:

        return set(self.posicion) == self.impactos  
    
    
    """
        Verifica si la nave ha sido completamente destruida.

        Retorna:
        - bool: True si todas las partes de la nave han sido impactadas, False en caso contrario.
    """