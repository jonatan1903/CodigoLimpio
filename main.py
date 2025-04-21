from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from src.view.gui.menu_screen import MenuScreen
from src.view.gui.registro_screen import RegistroScreen
from src.view.gui.login_screen import LoginScreen
from src.view.gui.juego_screen import JuegoScreen
from src.view.gui.puntuaciones_screen import PuntuacionesScreen

class BatallaNavalApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(RegistroScreen(name="registro"))
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(JuegoScreen(name="juego"))
        sm.add_widget(PuntuacionesScreen(name="puntuacion"))
        return sm

if __name__ == "__main__":
    BatallaNavalApp().run()