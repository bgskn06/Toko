from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.lang import Builder
import os


class RegisterScreen(FloatLayout):
    def __init__(self, **kwargs):
        super(RegisterScreen, self).__init__(**kwargs)

        self.label_judul = Label(text="SISTEM DIGITAL TOKO TERPADU", 
                                  size_hint_y=None, 
                                  height=40, 
                                  font_size='20sp', 
                                  color=(0,0,0,1),
                                  pos_hint={'center_x': 0.5, 'center_y': 0.9})
        self.add_widget(self.label_judul)

        self.form_layout = BoxLayout(orientation = 'vertical',
                                     size_hint = (0.8, 0.4),
                                     pos_hint = {'center_x':0.5, 'center_y':0.25},
                                     padding = 10,
                                     spacing = 10)
        
        self.label_email = Label(text = 'Email', 
                                 size_hint_y = None, 
                                 color=(0,0,0,1),
                                 height = 40)
        self.input_email = TextInput(hint_text = 'Masukkan Email', 
                                     size_hint_y = None, 
                                     height = 40,
                                     multiline = False)
        self.form_layout.add_widget(self.label_email)
        self.form_layout.add_widget(self.input_email)

        self.label_password = Label(text = 'Password', 
                                    size_hint_y = None, 
                                    color=(0,0,0,1),
                                    height = 40)
        self.input_password = TextInput(hint_text = 'Masukkan Password', 
                                     size_hint_y = None, 
                                     height = 40,
                                     password = True,
                                     multiline = False)
        self.form_layout.add_widget(self.label_password)
        self.form_layout.add_widget(self.input_password)

        self.label_alamat = Label(text = 'Alamat', 
                                  size_hint_y = None, 
                                  color=(0,0,0,1),
                                  height = 40)
        self.input_alamat = TextInput(hint_text = 'Masukkan Alamat', 
                                     size_hint_y = None, 
                                     height = 40,
                                     multiline = False)
        self.form_layout.add_widget(self.label_alamat)
        self.form_layout.add_widget(self.input_alamat)

        self.label_noHp = Label(text = 'No HP', 
                                size_hint_y = None, 
                                color=(0,0,0,1),
                                height = 40)
        self.input_noHp = TextInput(hint_text = 'Masukkan No Hp', 
                                     size_hint_y = None, 
                                     height = 40,
                                     multiline = False)
        self.form_layout.add_widget(self.label_noHp)
        self.form_layout.add_widget(self.input_noHp)

        self.label_role = Label(text = 'Daftar Sebagai', 
                                size_hint_y = None,
                                color=(0,0,0,1), 
                                height = 40)
        self.input_role = TextInput(hint_text = 'Pembeli / Penjual', 
                                     size_hint_y = None, 
                                     height = 40,
                                     multiline = False)
        self.form_layout.add_widget(self.label_role)
        self.form_layout.add_widget(self.input_role)
        
        self.tombol_daftar = Button(text = 'Daftar', 
                                    size_hint_y = None, 
                                    height = 50, 
                                    padding_x = 20,
                                    background_normal='',
                                    background_color = (0.396, 0.333, 0.561, 1))
        self.form_layout.add_widget(self.tombol_daftar)

        self.add_widget(self.form_layout)

class myApp(App):
    def build(self):
        Window.size = (360, 640)
        Window.clearcolor = (1, 1, 1, 1)
        return RegisterScreen()
    
if __name__ == '__main__':
    myApp().run()