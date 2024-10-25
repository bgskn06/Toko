from auth import AuthService
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label

auth_service = AuthService()
class LoginScreen(Screen):
    def login(self, email, password):
        success, message = auth_service.login(email, password)
        if success:
            user_role = App.get_running_app().user_role
               # Arahkan berdasarkan peran pengguna
            if user_role == 'admin':
                App.get_running_app().root.current = 'product_list'
            elif user_role == 'pengguna':
                App.get_running_app().root.current = 'home'
        else:
            print(message)  # Anda dapat mengganti ini dengan popup atau notifikasi
            self.show_popup('Gagal', 'gagal login')

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()
