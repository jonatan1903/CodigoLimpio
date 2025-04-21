import random
from src.model.celda import Celda
from src.model.nave import Nave

class Campo:

    """    
    Representa un campo de juego con un tablero bidimensional donde se colocan naves.

    Atributos de clase:
    - Tamaño_maximo (int): Valor máximo permitido para el ancho y alto del campo.
    - Tamaño_minimo (int): Valor mínimo permitido para el ancho y alto del campo.

    Atributos de instancia:
    - ancho (int): Número de columnas del campo.
    - alto (int): Número de filas del campo.
    - num_naves (int): Número total de naves a colocar en el campo.
    - naves_restantes (int): Número de naves que aún no han sido destruidas o descubiertas.
    - tablero (list): Matriz que representa el campo de juego, compuesta por objetos de tipo Celda.
    - naves (list): Lista de las posiciones o referencias de las naves colocadas.

    """    
    Tamaño_maximo = 20
    Tamaño_minimo = 2

    def __init__(self, ancho: int, alto: int, num_naves: int):

        """         
        Inicializa una instancia del campo de juego, validando los tamaños y la cantidad de naves.

        Parámetros:
        - ancho (int): Ancho del campo (número de columnas).
        - alto (int): Alto del campo (número de filas).
        - num_naves (int): Cantidad de naves a colocar en el campo.

        Excepciones:
        - ValueError: Si se ingresan valores negativos, tamaños fuera del rango permitido, más naves que casillas disponibles, o ninguna nave.

        """    
        
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
        self.colocar_naves()


    def colocar_naves(self):

        """"
        Coloca aleatoriamente las naves en el campo de juego sin repetir posiciones.

        Este método genera coordenadas aleatorias dentro del tablero y ubica una nave
        en una celda vacía (que no contenga otra nave). Repite ese procedimiento hasta que haya
        colocado el número total de naves especificado.

        """
        
        colocadas = 0
        while colocadas < self.num_naves:
            fila, columna = random.randint(0, self.alto - 1), random.randint(0, self.ancho - 1)
            if not self.tablero[fila][columna].contiene_nave:
                nueva_nave = Nave([(fila, columna)])
                self.naves.append(nueva_nave)
                self.tablero[fila][columna].contiene_nave = True
                colocadas += 1

        

    def evaluar_disparo_en_tablero(self, fila: int, columna: int) -> bool:

        """
        Evalua un disparo en una celda especifica del tablero
        parametros 
        -fila (int): indice de la fila donde se desea disparar 
        -columba(int): indice de la columna donde se desea disparar
         
        retorna 
        -bool: True si el disparo impacto una nave de lo contrario False si fue en agua 
         
        Excepciones 
        -typeError:Si las coordenadas no son enteros.
        - ValueError: Si las coordenadas están fuera de los límites del tablero o
        si la celda ya fue impactada previamente. 

        """


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
    
    

    def mostrar_campo(self):

        """
        Muestra en consola el estado actual del campo de juego.

        Recorre cada fila del tablero e imprime una representación de cada celda,
        separadas por espacios. 

        """

        for fila in self.tablero:
            print(" ".join(str(celda) for celda in fila))
        print()

            
    def quedan_naves(self) -> bool:

        """
        Indica si aún quedan naves activas en el campo de juego.

        Retorna:
        - bool: True si hay naves restantes, False si todas han sido destruidas.

        """

        return self.naves_restantes > 0
    
    
