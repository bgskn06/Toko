from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

class DetailProdukScreen(FloatLayout):
    def __init__(self, **kwargs):
        super(DetailProdukScreen, self).__init__(**kwargs)

        # Bar Pencarian
        self.search_bar = BoxLayout(orientation='horizontal',
                                    size_hint=(1, 0.1),
                                    pos_hint={'top': 1})

        self.menu_button = Button(text='☰', size_hint_x=0.1)
        self.search_input = TextInput(hint_text='Gas...', size_hint_x=0.7, multiline=False)
        self.cart_button = Button(text='🛒', size_hint_x=0.1)
        self.message_button = Button(text='✉️', size_hint_x=0.1)

        self.search_bar.add_widget(self.menu_button)
        self.search_bar.add_widget(self.search_input)
        self.search_bar.add_widget(self.cart_button)
        self.search_bar.add_widget(self.message_button)

        self.add_widget(self.search_bar)

        # Detail Produk
        self.product_box = BoxLayout(orientation='vertical',
                                     size_hint=(0.9, 0.6),
                                     pos_hint={'center_x': 0.5, 'center_y': 0.55},
                                     padding=10,
                                     spacing=10)

        # Header produk dengan nama dan harga
        header_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)

        self.product_icon = Button(text="A", size_hint_x=0.1)
        product_info_layout = BoxLayout(orientation='vertical', size_hint_x=0.7)
        product_name = Label(text="Gas 3Kg", font_size='16sp')
        product_price = Label(text="$20", font_size='14sp')
        product_info_layout.add_widget(product_name)
        product_info_layout.add_widget(product_price)

        more_button = Button(text="⋮", size_hint_x=0.1)

        header_layout.add_widget(self.product_icon)
        header_layout.add_widget(product_info_layout)
        header_layout.add_widget(more_button)

        self.product_box.add_widget(header_layout)

        # Gambar Produk
        self.product_image = Button(text='Gambar Produk',
                                    size_hint=(1, 0.5),
                                    background_normal='',
                                    background_color=(0.9, 0.9, 0.9, 1))

        self.product_box.add_widget(self.product_image)

        # Informasi tambahan
        product_description = Label(text="Gas 3 Kg\nStok : 25",
                                    size_hint_y=None,
                                    halign='left',
                                    valign='middle')

        store_info = Label(text="Alamat Toko :\nJl. Ambarawa no 25\nWA : 08586454841516",
                           size_hint_y=None,
                           halign='left',
                           valign='middle')

        self.product_box.add_widget(product_description)
        self.product_box.add_widget(store_info)

        # Tombol tindakan
        button_layout = BoxLayout(size_hint=(1, None), height=50, spacing=10)

        chat_button = Button(text="Chat Penjual", background_color=(0.7, 0.7, 0.7, 1))
        order_button = Button(text="Pesan", background_color=(0.6, 0.3, 0.8, 1))

        button_layout.add_widget(chat_button)
        button_layout.add_widget(order_button)

        self.product_box.add_widget(button_layout)
        self.add_widget(self.product_box)

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

class DetailProduk(App):
    def build(self):
        return DetailProdukScreen()

if __name__ == '__main__':
    DetailProduk().run()
