from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty
from src.controller.app_controlador import ControladorBatallaNaval

import os
from kivy.lang import Builder

kv_path = os.path.join(os.path.dirname(__file__), 'kv', 'login.kv')
Builder.load_file(os.path.abspath(kv_path))


class LoginScreen(Screen):
    usuario_input = ObjectProperty(None)
    contraseña_input = ObjectProperty(None)
    mensaje = StringProperty("")
    controlador = ControladorBatallaNaval()

    def iniciar_sesion(self):
        usuario = self.usuario_input.text.strip()
        contraseña = self.contraseña_input.text.strip()
        if not usuario or not contraseña:
            self.mensaje = "❌ El usuario y la contraseña no pueden estar vacíos."
            return

        exito = self.controlador.iniciar_sesion(usuario, contraseña)
        if exito:
            self.mensaje = "✅ Inicio de sesión exitoso."
            self.manager.get_screen("juego").controlador = self.controlador
            self.manager.current = "juego"
        else:
            self.mensaje = "❌ Usuario o contraseña incorrectos."

    def volver(self):
        self.manager.current = "menu"