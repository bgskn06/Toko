import os
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from login import LoginScreen
from home import HomeScreen
from register import RegisterScreen

from kivy.lang import Builder
from kivy.core.window import Window

class MyScreenManager(ScreenManager):
    pass

class MyApp(App):
    def build(self):
        Window.size = (360,640)
        Window.clearcolor = (1, 1, 1, 1)
        kv_path = os.path.join(os.path.dirname(__file__), 'kv')
        Builder.load_file(os.path.join(kv_path, 'loginscreen.kv'))
        Builder.load_file(os.path.join(kv_path, 'pilihtokoscreen.kv'))

        sm = MyScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(HomeScreen(name='home'))

        sm.current = 'login'

        return sm

if __name__ == '__main__':
    MyApp().run()