from src.model.campo import Campo

class ComienzaElJuego:
    def __init__(self, alto: int, ancho: int, num_naves: int):
        self.campo = Campo(ancho, alto, num_naves)

    def realizar_disparo(self, x: int, y: int):
        impacto = self.campo.VerificarImpacto(x, y)
        if impacto:
            print("¡Impacto en una nave!")
        else:
            print("Disparo al agua.")
        
    def verificar_ganador(self) -> bool:
        return not self.campo.QuedanNaves()

    def reiniciar_juego(self):
        ancho, alto, num_naves = self.campo.ancho, self.campo.alto, self.campo.num_naves
        self.campo = Campo(ancho, alto, num_naves)
        print("El juego ha sido reiniciado.")
