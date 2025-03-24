import random
from src.model.celda import Celda
from src.model.nave import Nave

class Campo:
    Tamaño_maximo = 20
    Tamaño_minimo = 2

    def __init__(self, ancho: int, alto: int, num_naves: int):
        if ancho < 0 or alto < 0 or num_naves < 0:
            raise ValueError("No se permiten valores negativos para el ancho, alto o número de naves.")
        
        if ancho < self.Tamaño_minimo or alto < self.Tamaño_minimo:
            raise ValueError(f"El tamaño mínimo del campo es {self.Tamaño_minimo} X {self.Tamaño_minimo}") 
        
        if ancho > self.Tamaño_maximo or alto > self.Tamaño_maximo:
            raise ValueError(f"El tamaño máximo del campo es {self.Tamaño_maximo} X {self.Tamaño_maximo}") 
        
        if num_naves > ancho * alto:
            raise ValueError("No se pueden colocar más naves que casillas disponibles.")
        
        if num_naves < 1:
            raise ValueError("Debe haber al menos una nave en el campo de juego.")
        
        self.ancho = ancho
        self.alto = alto
        self.num_naves = num_naves
        self.naves_restantes = num_naves
        self.tablero = [[Celda() for _ in range(ancho)] for _ in range(alto)]
        self.naves = []
        self.ColocarNaves()

    def ColocarNaves(self):
        colocadas = 0
        while colocadas < self.num_naves:
            fila, columna = random.randint(0, self.alto - 1), random.randint(0, self.ancho - 1)
            if not self.tablero[fila][columna].contiene_nave:
                nueva_nave = Nave([(fila, columna)])
                self.naves.append(nueva_nave)
                self.tablero[fila][columna].contiene_nave = True
                colocadas += 1

    def VerificarImpacto(self, fila: int, columna: int) -> bool:
        if not isinstance(fila, int) or not isinstance(columna, int):
            raise TypeError("Las coordenadas deben ser enteros")

        if not (0 <= fila < self.alto and 0 <= columna < self.ancho):
            raise ValueError("Disparo fuera de los límites")

        celda = self.tablero[fila][columna]

        if celda.impactada:
            raise ValueError("Esta celda ya ha sido impactada")

        for nave in self.naves:
            if nave.verificar_impacto((fila, columna)):
                celda.recibir_disparo()
                if nave.esta_destruida():
                    self.naves_restantes -= 1
                return True

        celda.recibir_disparo()
        return False

    def MostrarCampo(self):
        for fila in self.tablero:
            print(" ".join(str(celda) for celda in fila))
        print()
    
    def QuedanNaves(self) -> bool:
        return self.naves_restantes > 0
