from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.lang import Builder
import os

# buat kv
Builder.load_file(os.path.join(os.path.dirname(__file__), 'kv', 'homescreen.kv'))

class HomeScreen(FloatLayout):
    pass

class HomeApp(App):
    def build(self):
        Window.size = (360, 640)  
        Window.clearcolor = (1, 1, 1, 1)  
        return HomeScreen()

if __name__ == '__main__':
    HomeApp().run()
