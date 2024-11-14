from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from storageakun import StorageManager  # Pastikan ini adalah impor yang benar
from databaseakun import Database

class AdminScreen(Screen):
    input_email = ObjectProperty(None)
    input_alamat = ObjectProperty(None)
    input_noHp = ObjectProperty(None)
    selected_image_path = StringProperty('')  # Menyimpan jalur gambar
    image_url = StringProperty('')  # Menyimpan URL gambar yang diunggah

    def on_enter(self):
        self.load_account_info()

    def load_account_info(self):
        user_id = App.get_running_app().user_id
        if user_id:
            user_data = Database.get_user(user_id)
            if user_data:
                self.input_email.text = user_data.get('email', '')
                self.input_alamat.text = user_data.get('alamat', '')
                self.input_noHp.text = user_data.get('no_hp', '')
                self.image_url = user_data.get('image_url', '')  # Dapatkan URL gambar
                self.ids.image_preview.source = self.image_url  # Tampilkan gambar yang tersimpan
            else:
                self.show_popup('Error', 'Informasi akun tidak ditemukan.')
        else:
            self.show_popup('Error', 'User ID tidak ditemukan.')

    def update_user(self):
        email = self.input_email.text.strip()
        alamat = self.input_alamat.text.strip()
        no_hp = self.input_noHp.text.strip()

        if email and alamat and no_hp:
            try:
                updated_data = {
                    'email': email,
                    'alamat': alamat,
                    'no_hp': no_hp,
                }
                
                # Jika gambar baru dipilih, upload gambar dan perbarui URL gambar
                if self.selected_image_path:
                    upload_result = StorageManager.upload_image(self.selected_image_path)
                    if upload_result['status'] == 'success':
                        updated_data['image_url'] = upload_result['url']  # Simpan URL gambar yang diunggah
                        self.image_url = upload_result['url']
                        self.ids.image_preview.source = self.image_url
                        self.ids.image_preview.reload()
                    else:
                        self.show_popup('Error', 'Gagal mengupload gambar: ' + upload_result['message'])
                
                Database.update_user(App.get_running_app().user_id, updated_data)
                self.show_popup('Sukses', 'Informasi akun berhasil diperbarui!')
            except Exception as e:
                self.show_popup('Error', f'Terjadi kesalahan: {str(e)}')
        else:
            self.show_popup('Error', 'Semua field harus diisi!')

    def show_popup(self, title, content):
        popup = Popup(
            title=title,
            content=Label(text=content),
            size_hint=(None, None),
            size=(400, 200)
        )
        popup.open()

    def select_image(self):
        # Membuka ImageChooserPopup
        popup = ImageChooserPopup(callback=self.on_image_selected)
        popup.open()
        
    def on_image_selected(self, selected_image_path):
        self.selected_image_path = selected_image_path
        self.ids.image_preview.source = self.selected_image_path  # Set gambar terpilih ke pratinjau
        self.ids.image_preview.reload()
        self.show_popup('Gambar Dipilih', f'Gambar yang dipilih: {self.selected_image_path}')

class ImageChooserPopup(Popup):
    def __init__(self, callback, **kwargs):
        super().__init__(**kwargs)
        self.title = 'Pilih Gambar'
        self.size_hint = (0.9, 0.9)
        self.callback = callback

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.file_chooser = FileChooserIconView(
            filters=['*.png', '*.jpg', '*.jpeg'],
            path='.'
        )
        layout.add_widget(self.file_chooser)

        button_layout = BoxLayout(size_hint_y=None, height=40, spacing=10)
        
        cancel_btn = Button(text='Batal')
        cancel_btn.bind(on_press=self.dismiss)
        
        select_btn = Button(text='Pilih', background_color=(0.3, 0.5, 0.9, 1))
        select_btn.bind(on_press=self.select_image)
        
        button_layout.add_widget(cancel_btn)
        button_layout.add_widget(select_btn)
        
        layout.add_widget(button_layout)
        self.content = layout

    def select_image(self, instance):
        if self.file_chooser.selection:
            self.callback(self.file_chooser.selection[0])
            self.dismiss()
