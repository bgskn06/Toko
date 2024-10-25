from auth import AuthService
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label

auth_service = AuthService()
class RegisterScreen(Screen):
    def register(self, email, password, alamat, no_hp):
        success, message = auth_service.register(email, password, alamat, no_hp, role='pengguna')
        if success:
            print(message)  # Feedback saat registrasi berhasil
            App.get_running_app().root.current = 'login'
        else:
            print(message)  # Anda dapat mengganti ini dengan popup atau notifikasi
            self.show_popup('Gagal', 'gagal daftar')

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()
