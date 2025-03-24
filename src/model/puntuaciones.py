from src.model.jugador import Jugador

class Puntuaciones:
    def __init__(self):
        self.lista_puntuaciones = []

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

    def mostrar_puntuaciones(self):
        print("\nTABLA DE PUNTUACIONES:")
        for i, registro in enumerate(self.lista_puntuaciones, start=1):
            print(f"{i}. {registro['nombre_usuario']} - {registro['puntaje']} puntos")
