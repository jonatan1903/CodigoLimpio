import os
import sys
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

from src.controller.app_controlador import ControladorBatallaNaval
from kivy.lang import Builder

kv_path = os.path.join(os.path.dirname(__file__), 'kv', 'registro.kv')
Builder.load_file(os.path.abspath(kv_path))


class RegistroScreen(Screen):
    usuario_input = ObjectProperty(None)
    contrasena_input = ObjectProperty(None)
    mensaje = StringProperty("")
    controlador = ControladorBatallaNaval()

    def registrar(self):
        usuario = self.usuario_input.text.strip()
        contraseña = self.contrasena_input.text.strip()
        if not usuario or not contraseña:
            self.mensaje = "❌ El usuario y la contraseña no pueden estar vacíos."
            return

        exito = self.controlador.registrar_jugador(usuario, contraseña)
        if exito:
            self.mensaje = "✅ Registro exitoso."
            self.usuario_input.text = ""
            self.contrasena_input.text = ""
        else:
            self.mensaje = "❌ Error: El usuario ya existe o los datos son inválidos."

    def volver(self):
        self.manager.current = "menu"