from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.core.window import Window
import os

kv_path = os.path.join(os.path.dirname(__file__), 'kv')
Builder.load_file(os.path.join(kv_path, 'tokoscreen.kv'))

class TokoScreen(Screen):
    pass

class MyApp(App):
    def build(self):
        return TokoScreen()

if __name__ == '__main__':
    Window.size = (320, 640)  # Ukuran jendela
    Window.clearcolor = (1, 1, 1, 1) 
    MyApp().run()
