# pilih_toko.py
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import AsyncImage
from kivy.app import App
from database import Database 
from kivy.uix.popup import Popup # Pastikan import Database yang benar

class PilihTokoScreen(Screen):
    def on_enter(self):
        # Memuat produk ketika layar ditampilkan
        self.load_products_for_toko()

    def load_products_for_toko(self):
        app = App.get_running_app()
        selected_toko_id = app.selected_toko_id  # Pastikan ID toko telah dipilih sebelumnya
        
        if selected_toko_id:
            # Ambil produk dari database berdasarkan toko
            products = Database.get_products_by_toko(selected_toko_id)
            
            # Bersihkan daftar produk yang ada di GridLayout
            self.ids.product_list.clear_widgets()

            if products:
                for product_id, product in products:
                    # Membuat BoxLayout untuk setiap produk
                    product_box = BoxLayout(orientation='vertical', padding=10, size_hint_y=None, height=200)

                    # Gambar produk
                    image_url = product.get('image_url', 'path/to/default/image.png')
                    product_image = AsyncImage(source=image_url, size_hint=(None, None), size=(100, 100))
                    product_box.add_widget(product_image)

                    # Nama produk dengan warna hitam
                    product_name = Label(
                        text=product.get('nama', 'Nama Produk Tidak Ditemukan'),
                        size_hint_y=None,
                        height=30,
                        color=(0, 0, 0, 1)  # Warna hitam
                    )
                    product_price = Label(
                        text=f"Harga: Rp {product.get('harga', 0):,.0f}",
                        size_hint_y=None,
                        height=30,
                        color=(0, 0, 0, 1)  # Warna hitam
                    )
                    product_box.add_widget(product_name)
                    product_box.add_widget(product_price)

                    # Tombol Pilih
                    pilih_button = Button(text="Pilih", size_hint_y=None, height=40)
                    pilih_button.bind(on_press=lambda instance, pid=product_id: self.pilih_product(pid))
                    product_box.add_widget(pilih_button)

                    # Tambahkan produk ke dalam grid
                    self.ids.product_list.add_widget(product_box)
            else:
                self.show_popup("Info", "Tidak ada produk untuk toko ini.")
        else:
            self.show_popup("Error", "Toko yang dipilih tidak valid.")
    def pilih_product(self, product_id):
        print(f"Produk dengan ID {product_id} dipilih.")
        # Lanjutkan aksi ketika produk dipilih (misalnya navigasi ke detail produk)
        
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