class Celda:
    def __init__(self, contiene_nave=False):
        self.contiene_nave = contiene_nave
        self.impactada = False

    def recibir_disparo(self):
        if self.impactada:
            raise ValueError("Esta celda ya ha sido impactada")
        
        self.impactada = True
        return self.contiene_nave

    def __str__(self):
        if not self.impactada:
            return "~"
        return "X" if self.contiene_nave else "O"
