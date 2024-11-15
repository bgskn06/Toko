from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Cart:
    def __init__(self):
        self.items = []  # Daftar produk di keranjang

    def add_item(self, product):
        """Menambahkan produk ke dalam keranjang"""
        # Cek apakah produk sudah ada dalam keranjang
        for item in self.items:
            if item['id'] == product['id']:
                item['quantity'] += 1  # Jika sudah ada, tambahkan jumlahnya
                return
        # Jika belum ada, tambahkan produk baru
        product['quantity'] = 1  # Set jumlah produk menjadi 1
        self.items.append(product)

    def remove_item(self, product_id):
        """Menghapus produk dari keranjang berdasarkan ID"""
        self.items = [item for item in self.items if item['id'] != product_id]

    def get_items(self):
        """Mengambil semua produk di keranjang"""
        return self.items

    def total_price(self):
        """Menghitung total harga semua produk di keranjang"""
        return sum(item['harga'] * item['quantity'] for item in self.items)

    def clear(self):
        """Menghapus semua produk dari keranjang"""
        self.items = []


class KeranjangScreen(Screen):
    def on_enter(self):
        self.load_cart_items()

    def load_cart_items(self):
        cart_items = App.get_running_app().cart.get_items()  # Mengakses cart yang sudah didefinisikan di MyApp
        self.ids.cart_layout.clear_widgets()  # Kosongkan layout keranjang
        
        if cart_items:
            for item in cart_items:
                product_name = item['nama']
                product_quantity = item['quantity']
                product_price = f"Rp {item['harga']:,.0f}"
                total_price = f"Rp {item['harga'] * product_quantity:,.0f}"
                
                product_label = BoxLayout(orientation='horizontal', size_hint_y=None, height='50dp', padding=[10, 10])
                product_label.add_widget(Label(text=f"{product_name} x{product_quantity}", size_hint_x=0.5))
                product_label.add_widget(Label(text=product_price, size_hint_x=0.25))
                product_label.add_widget(Label(text=total_price, size_hint_x=0.25))
                
                self.ids.cart_layout.add_widget(product_label)  # Menambahkan produk ke layout keranjang
        else:
            self.ids.cart_layout.add_widget(Label(text="Keranjang Anda kosong."))


    def go_to_checkout(self):
        """Navigasi ke halaman checkout"""
        print("Navigasi ke halaman checkout...")
        # Navigasi ke halaman checkout di sini