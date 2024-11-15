from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivy.app import App
from database import Database
from kivy.uix.popup import Popup
from kivy.uix.button import Button

class DetailScreen(Screen):
    def on_enter(self):
        self.load_product_details()

    def load_product_details(self):
        app = App.get_running_app()
        product_id = app.selected_product_id  # Mengambil ID produk yang dipilih
        
        # Pastikan ID produk valid
        if product_id:
            product_data = Database.get_product_by_id(product_id)  # Ambil data produk dari database
            if product_data:
                self.display_product_details(product_data)
            else:
                self.show_popup("Error", "Produk tidak ditemukan.")
        else:
            self.show_popup("Error", "ID produk tidak valid.")

    def display_product_details(self, product_data):
        """Menampilkan detail produk ke dalam UI"""
        # Mengambil data produk
        product_name = product_data.get('nama', 'Nama Produk Tidak Ditemukan')
        product_price = f"Rp {product_data.get('harga', 0):,.0f}"
        image_url = product_data.get('image_url', 'assets/default_image.png')  # Menambahkan path gambar default jika tidak ada
        product_stock = product_data.get('stok', 0)
        
        # Memperbarui UI dengan informasi produk
        self.ids.product_name_label.text = product_name
        self.ids.product_price_label.text = product_price
        self.ids.product_stock_label.text = f"Stok: {product_stock}"
        
        # Memperbarui sumber gambar menggunakan URL atau path
        self.ids.product_image.source = image_url  # Pastikan sumber adalah string, bukan objek AsyncImage
        self.ids.product_image.reload()  # Pastikan gambar dimuat ulang

    def show_popup(self, title, message):
        """Menampilkan popup dengan pesan"""
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=message))

        close_button = Button(text="Tutup", size_hint_y=None, height=40)
        content.add_widget(close_button)
        
        # Membuat popup
        popup = Popup(title=title, content=content, size_hint=(None, None), size=(400, 200))
        close_button.bind(on_press=popup.dismiss)  # Menutup popup ketika tombol 'Tutup' diklik
        popup.open()  # Menampilkan popup
