from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty
from src.controller.app_controlador import ControladorBatallaNaval

import os
from kivy.lang import Builder

kv_path = os.path.join(os.path.dirname(__file__), 'kv', 'juego.kv')
Builder.load_file(os.path.abspath(kv_path))


class JuegoScreen(Screen):
    mensaje = StringProperty("")
    controlador = ControladorBatallaNaval()

    def iniciar_juego(self):
        try:
            ancho = int(self.ids.ancho_input.text)
            alto = int(self.ids.alto_input.text)
            num_naves = int(self.ids.naves_input.text)
            self.controlador.iniciar_juego(ancho, alto, num_naves)
            self.mensaje = "Juego iniciado. ¡Buena suerte!"
        except ValueError:
            self.mensaje = "❌ Entrada inválida. Usa números enteros."

    def realizar_disparo(self):
        try:
            x = int(self.ids.fila_input.text)
            y = int(self.ids.columna_input.text)
            impacto = self.controlador.realizar_disparo(x, y)
            if impacto:
                self.mensaje = "¡Impacto en una nave!"
            else:
                self.mensaje = "Disparo al agua."
        except ValueError:
            self.mensaje = "❌ Entrada inválida. Usa números enteros."
        except Exception as e:
            self.mensaje = f"❌ Error: {str(e)}"

    def volver(self):
        self.manager.current = "menu"