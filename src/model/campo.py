
from src.model.juego import ComienzaElJuego


class Campo:



    Tamaño_maximo = 20
    Tamaño_minimo = 2
    


    def __init__(self, ancho: int, alto: int, num_naves: int):

        if ancho < self.Tamaño_minimo or alto < self.Tamaño_minimo:
            raise ValueError(f"El tamaño minimo del campo es {self.Tamaño_minimo} X {self.Tamaño_minimo}") 
        
        if ancho > self.Tamaño_maximo or alto > self.Tamaño_maximo:

            raise ValueError(f"El tamaño máximo del campo es {self.Tamaño_maximo} X {self.Tamaño_maximo}") 

        
        if num_naves > ancho * alto:
            raise ValueError("No se pueden colocar más naves que casillas disponibles.")
        
        if ancho < 0 or alto < 0 or num_naves < 0:
            raise ValueError("No se permiten valores negativos para el ancho, alto o número de naves.")
        
        if num_naves < 1:
            raise ValueError("Debe haber al menos una nave en el campo de juego.")

        self.ancho = ancho
        self.alto = alto
        self.jugadores = []
        self.celdas = [[None for _ in range(ancho)] for _ in range(alto)]

    def ColocarNaves(self, ancho, alto, num_naves ):
        
        pass

    def VerificarImpacto(self, fila: int, columna: int) -> bool:
        pass 

    def MostrarCampo ():
        pass
