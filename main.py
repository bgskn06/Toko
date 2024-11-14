import os
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from halaman.login import LoginScreen
from halaman.home import HomeScreen
from halaman.register import RegisterScreen
from halaman.pilih_toko import PilihTokoScreen
from halaman.toko import TokoScreen
from halaman.pesanan import PesananScreen
from halaman.akun import AkunScreen
from halaman.hasil_pencarian import PencarianScreen
from halaman.detail_produk import DetailScreen
from halaman.keranjang import KeranjangScreen
from halaman.chat import ChatScreen
from halaman.admin.product import ProductList, AddProduct, EditProduct
from halaman.admin.admin import AdminScreen

from kivy.lang import Builder
from kivy.core.window import Window


class MyScreenManager(ScreenManager):
    pass

class MyApp(App):
    def build(self):
        Window.size = (360,640)
        Window.clearcolor = (1, 1, 1, 1)
        kv_path = os.path.join(os.path.dirname(__file__), 'kv')
        Builder.load_file(os.path.join(kv_path, 'loginscreen.kv'))
        Builder.load_file(os.path.join(kv_path, 'pilihtokoscreen.kv'))
        Builder.load_file(os.path.join(kv_path, 'homescreen.kv'))
        Builder.load_file(os.path.join(kv_path, 'registerscreen.kv'))
        Builder.load_file(os.path.join(kv_path, 'pesananscreen.kv'))
        Builder.load_file(os.path.join(kv_path, 'akunscreen.kv'))
        Builder.load_file(os.path.join(kv_path, 'tokoscreen.kv'))
        Builder.load_file(os.path.join(kv_path, 'pencarianscreen.kv'))
        Builder.load_file(os.path.join(kv_path, 'detailscreen.kv'))
        Builder.load_file(os.path.join(kv_path, 'keranjangscreen.kv'))
        Builder.load_file(os.path.join(kv_path, 'chatscreen.kv'))
        Builder.load_file(os.path.join(kv_path, 'product.kv'))
        Builder.load_file(os.path.join(kv_path, 'adminscreen.kv'))

        sm = MyScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(PilihTokoScreen(name='pilihtoko'))
        sm.add_widget(TokoScreen(name='toko'))
        sm.add_widget(PesananScreen(name='pesanan'))
        sm.add_widget(AkunScreen(name='akun'))
        sm.add_widget(PencarianScreen(name='pencarian'))
        sm.add_widget(DetailScreen(name='detail'))
        sm.add_widget(KeranjangScreen(name='keranjang'))
        sm.add_widget(ChatScreen(name='chat'))
        # sm.add_widget(EditAkun(name='update_user'))
        sm.add_widget(ProductList(name='product_list'))
        sm.add_widget(AddProduct(name='add_product'))
        sm.add_widget(EditProduct(name='edit_product'))
        sm.add_widget(AdminScreen(name='admin'))
        

        sm.current = 'login'

        return sm

if __name__ == '__main__':
    MyApp().run()