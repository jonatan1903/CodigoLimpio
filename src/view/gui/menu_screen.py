from kivy.uix.screenmanager import Screen
import os
from kivy.lang import Builder

kv_path = os.path.join(os.path.dirname(__file__), 'kv', 'menu.kv')
Builder.load_file(os.path.abspath(kv_path))


class MenuScreen(Screen):
    pass