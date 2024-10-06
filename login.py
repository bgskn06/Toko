from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class LoginScreen(FloatLayout):
    def __init__(self, **kwargs):
        super(LoginScreen,self).__init__(**kwargs)

        self.label_judul= Label(text="SISTEM DIGITAL TOKO TERPADU",
                                 size_hint_y = None,
                                 font_size = '20sp',
                                 pos_hint = {'center_x':0.5,'center_y':0.9})
        self.add_widget(self.label_judul)

        self.logo = Image(source = 'logo.png',
                          size_hint = (None, None),
                          pos_hint = {'center_x':0.5,'center_y':0.75})
        self.add_widget(self.logo)

        self.form_layout = BoxLayout(orientation = 'vertical',
                                     size_hint = (0.8, 0.4),
                                     pos_hint = {'center_x':0.5, 'center_y': 0.4},
                                     padding = 10,
                                     spacing = 10)
        
        self.label_email = Label(text = 'Email', size_hint_y = None, height = 40)
        self.input_email = TextInput(hint_text = 'Masukkan email',
                                    size_hint_y = None,
                                    height = 40,
                                    multiline = False)
        self.form_layout.add_widget(self.label_email)
        self.form_layout.add_widget(self.input_email)

        self.label_password = Label(text = 'Kata Sandi', size_hint_y = None, height = 40)
        self.input_password = TextInput(hint_text = 'Masukkan Kata Sandi',
                                    size_hint_y = None,
                                    height = 40,
                                    password = True,
                                    multiline = False)
        self.form_layout.add_widget(self.label_password)
        self.form_layout.add_widget(self.input_password)

        self.button_layout = GridLayout(cols=2, padding = 20, spacing = 20)
        self.tombol_masuk = Button(text = 'Masuk', size_hint_y = None, height = 50)
        self.tombol_daftar = Button(text = 'Daftar', size_hint_y = None, height = 50)
        self.button_layout.add_widget(self.tombol_masuk)
        self.button_layout.add_widget(self.tombol_daftar)
        self.form_layout.add_widget(self.button_layout)

        self.add_widget(self.form_layout)

        self.lupa_password = Label(text='Lupa Kata Sandi?',
                                   size_hint_y = None,
                                   height = 30,
                                   pos_hint = {'center_x':0.5, 'center_y': 0.1})
        self.add_widget(self.lupa_password)

class myApp(App):
    def build(self):
        return LoginScreen()
    
if __name__ == '__main__':
    myApp().run()