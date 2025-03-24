class Nave:
    def __init__(self, posicion: list):
        self.posicion = posicion  
        self.impactos = set() 

    def verificar_impacto(self, coordenada: tuple) -> bool:
        if coordenada in self.posicion and coordenada not in self.impactos:
            self.impactos.add(coordenada)  
            return True
        return False
    
    def esta_destruida(self) -> bool:
        return set(self.posicion) == self.impactos 