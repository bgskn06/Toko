from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

class TokoScreen(FloatLayout):
    def __init__(self, **kwargs):
        super(TokoScreen, self).__init__(**kwargs)

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

        # ScrollView untuk daftar toko
        self.scroll_view = ScrollView(size_hint=(1, 0.75),
                                      pos_hint={'x': 0, 'y': 0.15})

        self.list_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.list_layout.bind(minimum_height=self.list_layout.setter('height'))

        # Menambahkan daftar toko
        for i in range(7):  # Contoh 7 toko
            toko_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=80, padding=10)

            # Ikon toko
            self.toko_icon = Button(text=f"{chr(65 + i)}", size_hint_x=0.1)

            # Nama dan alamat toko
            toko_info_layout = BoxLayout(orientation='vertical', size_hint_x=0.6)
            toko_name = Label(text=f'Toko {chr(65 + i)}', font_size='16sp')
            toko_address = Label(text=f'Alamat Toko {chr(65 + i)}', font_size='12sp')
            toko_info_layout.add_widget(toko_name)
            toko_info_layout.add_widget(toko_address)

            # Ikon aksi di sebelah kanan
            action_layout = GridLayout(cols=2, size_hint_x=0.3, spacing=10)
            action_button_1 = Button(text='🔺')
            action_button_2 = Button(text='◼️')
            action_layout.add_widget(action_button_1)
            action_layout.add_widget(action_button_2)

            toko_layout.add_widget(self.toko_icon)
            toko_layout.add_widget(toko_info_layout)
            toko_layout.add_widget(action_layout)

            self.list_layout.add_widget(toko_layout)

        self.scroll_view.add_widget(self.list_layout)
        self.add_widget(self.scroll_view)

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

class TokoApp(App):
    def build(self):
        return TokoScreen()

if __name__ == '__main__':
    TokoApp().run()
