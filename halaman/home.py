from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder
import os
from kivy.uix.screenmanager import Screen

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

        # Bar Pencarian
        self.search_bar = BoxLayout(orientation='horizontal',
                                    size_hint=(1, 0.1),
                                    pos_hint={'top': 1})

        self.menu_button = Button(text='☰', size_hint_x=0.1)
        self.search_input = TextInput(hint_text='Cari...',
                                      size_hint_x=0.7,
                                      multiline=False)
        self.cart_button = Button(text='🛒', size_hint_x=0.1)
        self.message_button = Button(text='✉️', size_hint_x=0.1)

        self.search_bar.add_widget(self.menu_button)
        self.search_bar.add_widget(self.search_input)
        self.search_bar.add_widget(self.cart_button)
        self.search_bar.add_widget(self.message_button)

        self.add_widget(self.search_bar)

        # Gambar Utama di Tengah
        self.main_image = Image(source='placeholder.png',
                                size_hint=(0.6, 0.4),
                                color = (0,0,0,1),
                                pos_hint={'center_x': 0.5, 'center_y': 0.6})
        self.add_widget(self.main_image)

        # Label untuk menunjukkan elemen di bawah gambar
        self.label_info = Label(text='...',
                                size_hint=(None, None),
                                height=30,
                                pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.add_widget(self.label_info)

        # Grid Kategori
        self.category_layout = GridLayout(cols=5,
                                          size_hint=(0.9, 0.15),
                                          pos_hint={'center_x': 0.5, 'center_y': 0.3},
                                          spacing=10)

        for i in range(5):
            category_button = Button(text=f'Kategori {i+1}')
            self.category_layout.add_widget(category_button)

        self.add_widget(self.category_layout)

        # Navigasi Bawah
        self.nav_layout = BoxLayout(orientation='horizontal',
                                    size_hint=(1, 0.1),
                                    pos_hint={'bottom': 1})

        self.home_button = Button(text='🏠', size_hint_x=0.2)
        self.shop_button = Button(text='🛍️', size_hint_x=0.2)
        self.orders_button = Button(text='📦', size_hint_x=0.2)
        self.profile_button = Button(text='👤', size_hint_x=0.2)
        self.more_button = Button(text='⚙️', size_hint_x=0.2)

        self.nav_layout.add_widget(self.home_button)
        self.nav_layout.add_widget(self.shop_button)
        self.nav_layout.add_widget(self.orders_button)
        self.nav_layout.add_widget(self.profile_button)
        self.nav_layout.add_widget(self.more_button)

        self.add_widget(self.nav_layout)

# class HomeApp(App):
#     def build(self):
#         Window.size = (360, 640)
#         Window.clearcolor = (1, 1, 1, 1)
#         return HomeScreen()

# if __name__ == '__main__':
#     HomeApp().run()
