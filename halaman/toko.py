# from kivy.uix.screenmanager import Screen
# from kivy.uix.label import Label
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.image import AsyncImage
# from kivy.uix.button import Button
# from databaseakun import Database
# from kivy.app import App

# class TokoScreen(Screen):
#     def on_enter(self):
#         # Memuat data admin saat layar diakses
#         self.load_admin_users()

#     def load_admin_users(self):
#         # Ambil data semua admin dari database
#         admin_users = Database.get_admin_users()
        
#         # Bersihkan widget `toko_list` sebelum menambahkan data baru
#         self.ids.toko_list.clear_widgets()

#         # Periksa apakah ada data admin
#         if admin_users:
#             for uid, user_data in admin_users.items():
#                 # Buat layout horizontal untuk setiap admin
#                 user_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=100, padding=[10, 10])

#                 # Tambahkan gambar profil admin jika tersedia
#                 image_url = user_data.get('image_url', '')
#                 if image_url:
#                     image = AsyncImage(source=image_url, size_hint=(None, None), size=(80, 80))
#                     user_box.add_widget(image)
#                 else:
#                     # Gambar default jika tidak ada URL gambar
#                     image = AsyncImage(source='path/to/default/image.png', size_hint=(None, None), size=(80, 80))
#                     user_box.add_widget(image)

#                 # Buat kotak informasi untuk data pengguna
#                 info_box = BoxLayout(orientation='vertical', spacing=5, padding=[10, 0])
#                 info_box.add_widget(Label(text=f"Email: {user_data.get('email', 'Tidak ada email')}", font_size='14sp', color=(0, 0, 0, 1)))
#                 info_box.add_widget(Label(text=f"Alamat: {user_data.get('alamat', 'Tidak ada alamat')}", font_size='14sp', color=(0, 0, 0, 1)))
#                 info_box.add_widget(Label(text=f"No HP: {user_data.get('no_hp', 'Tidak ada no_hp')}", font_size='14sp', color=(0, 0, 0, 1)))

#                 # Tambahkan `info_box` ke dalam `user_box`
#                 user_box.add_widget(info_box)

#                 # Tambahkan tombol "Pilih"
#                 pilih_button = Button(text='Pilih', size_hint=(None, None), size=(100, 40))
#                 pilih_button.bind(on_press=lambda instance, uid=uid: self.pilih_toko(uid))  # Bind aksi tombol
#                 user_box.add_widget(pilih_button)

#                 # Tambahkan `user_box` ke dalam `toko_list`
#                 self.ids.toko_list.add_widget(user_box)
#         else:
#             # Tampilkan pesan jika tidak ada data admin ditemukan
#             self.show_popup('Info', 'Tidak ada data admin yang ditemukan.')

#     def pilih_toko(self, uid):
#         # Fungsi yang akan dipanggil saat tombol "Pilih" diklik
#         print(f"Toko dengan ID {uid} dipilih")
#         app = App.get_running_app()  # Mendapatkan instance aplikasi
#         app.root.current = 'pilihtoko'

#     def show_popup(self, title, message):
#         # Implementasi fungsi untuk menampilkan popup informasi
#         pass

from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivy.uix.button import Button
from kivy.app import App
from databaseakun import Database

class TokoScreen(Screen):
    def on_enter(self):
        # Memuat data admin saat layar diakses
        self.load_admin_users()

    def load_admin_users(self):
        # Ambil data semua admin dari database
        admin_users = Database.get_admin_users()
        
        # Bersihkan widget `toko_list` sebelum menambahkan data baru
        self.ids.toko_list.clear_widgets()

        # Periksa apakah ada data admin
        if admin_users:
            for uid, user_data in admin_users.items():
                # Buat layout horizontal untuk setiap admin
                user_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=100, padding=[10, 10])

                # Tambahkan gambar profil admin jika tersedia
                image_url = user_data.get('image_url', '')
                if image_url:
                    image = AsyncImage(source=image_url, size_hint=(None, None), size=(80, 80))
                    user_box.add_widget(image)
                else:
                    # Gambar default jika tidak ada URL gambar
                    image = AsyncImage(source='path/to/default/image.png', size_hint=(None, None), size=(80, 80))
                    user_box.add_widget(image)

                # Buat kotak informasi untuk data pengguna
                info_box = BoxLayout(orientation='vertical', spacing=5, padding=[10, 0])
                info_box.add_widget(Label(text=f"Email: {user_data.get('email', 'Tidak ada email')}", font_size='14sp', color=(0, 0, 0, 1)))
                info_box.add_widget(Label(text=f"Alamat: {user_data.get('alamat', 'Tidak ada alamat')}", font_size='14sp', color=(0, 0, 0, 1)))
                info_box.add_widget(Label(text=f"No HP: {user_data.get('no_hp', 'Tidak ada no_hp')}", font_size='14sp', color=(0, 0, 0, 1)))

                # Tambahkan `info_box` ke dalam `user_box`
                user_box.add_widget(info_box)

                # Tambahkan tombol "Pilih"
                pilih_button = Button(text='Pilih', size_hint=(None, None), size=(100, 40))
                pilih_button.bind(on_press=lambda instance, uid=uid: self.pilih_toko(uid))  # Bind aksi tombol
                user_box.add_widget(pilih_button)

                # Tambahkan `user_box` ke dalam `toko_list`
                self.ids.toko_list.add_widget(user_box)
        else:
            # Tampilkan pesan jika tidak ada data admin ditemukan
            self.show_popup('Info', 'Tidak ada data admin yang ditemukan.')

    def pilih_toko(self, uid):
        # Fungsi yang akan dipanggil saat tombol "Pilih" diklik
        print(f"Toko dengan ID {uid} dipilih")
        
        # Simpan `uid` ke dalam aplikasi (sebagai properti)
        app = App.get_running_app()  # Mendapatkan instance aplikasi
        app.selected_toko_id = uid  # Menyimpan ID toko yang dipilih

        # Pindah ke layar pilih toko
        app.root.current = 'pilihtoko'

    def show_popup(self, title, message):
        # Implementasi fungsi untuk menampilkan popup informasi
        pass
