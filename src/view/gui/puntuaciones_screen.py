from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from src.controller.app_controlador import ControladorBatallaNaval

import os
from kivy.lang import Builder

kv_path = os.path.join(os.path.dirname(__file__), 'kv', 'puntuaciones.kv')
Builder.load_file(os.path.abspath(kv_path))


class PuntuacionesScreen(Screen):
    puntuaciones = StringProperty("")
    controlador = ControladorBatallaNaval()

    def mostrar_puntuaciones(self):
        lista_puntuaciones = self.controlador.obtener_puntuaciones()
        if lista_puntuaciones:
            self.puntuaciones = "\n".join(
                [f"{i+1}. {p['nombre_usuario']} - {p['puntaje']} puntos" for i, p in enumerate(lista_puntuaciones)]
            )
        else:
            self.puntuaciones = "No hay puntuaciones registradas."

    def volver(self):
        self.manager.current = "menu"