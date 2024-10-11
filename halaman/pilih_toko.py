from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.core.window import Window
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), 'kv', 'pilihtokoscreen.kv'))

class PilihTokoScreen(Screen):
    pass

class HalamanToko(App):
    def build(self):
        return PilihTokoScreen()

if __name__ == '__main__':
    Window.size = (320, 640)  # Ukuran jendela
    Window.clearcolor = (1, 1, 1, 1) 
    HalamanToko().run()
