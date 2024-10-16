import os
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from halaman.login import LoginScreen
from halaman.home import HomeScreen
from halaman.register import RegisterScreen
from halaman.pilih_toko import PilihTokoScreen
from halaman.toko import TokoScreen

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
        Builder.load_file(os.path.join(kv_path, 'homescreen.kv'))
        Builder.load_file(os.path.join(kv_path, 'registerscreen.kv'))

        sm = MyScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(PilihTokoScreen(name='pilihtoko'))
        sm.add_widget(TokoScreen(name='toko'))
        sm.add_widget()

        sm.current = 'login'

        return sm

if __name__ == '__main__':
    MyApp().run()