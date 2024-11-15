# database.py
import pyrebase
from firebase_config import get_firebase_config

class Database:
    config = get_firebase_config()
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()

    @staticmethod
    def get_all_products():
        
        try:
            products = Database.db.child("products").get()
            if products.each():
                return [(product.key(), product.val()) for product in products.each()]
            return []
        except Exception as e:
            print(f"Error getting products: {e}")
            return []
        
    @staticmethod
    def get_product_by_id(product_id):
        """Mengambil data produk berdasarkan ID produk"""
        try:
            product = Database.db.child("products").child(product_id).get()
            if product.val():
                return product.val()  # Mengembalikan data produk jika ditemukan
            return None
        except Exception as e:
            print(f"Error getting product by id: {e}")
            return None
        
    @staticmethod
    def get_toko_data_by_id(toko_id):
        try:
            toko = Database.db.child("toko").child(toko_id).get()
            if toko.val():
                return toko.val()  # Mengembalikan data toko jika ditemukan
            return None
        except Exception as e:
            print(f"Error getting toko data: {e}")
            return None
                
    @staticmethod
    def get_products_by_toko(created_by):
        try:
            # Ambil produk berdasarkan created_by
            products = Database.db.child("products").order_by_child("created_by").equal_to(created_by).get()
            if products.each():
                return [(product.key(), product.val()) for product in products.each()]
            return []
        except Exception as e:
            print(f"Error getting products by toko: {e}")
            return []   

    @staticmethod
    def add_product(product_data):
        try:
            return Database.db.child("products").push(product_data)
        except Exception as e:
            print(f"Error adding product: {e}")
            raise e

    @staticmethod
    def update_product(product_id, product_data):
        try:
            return Database.db.child("products").child(product_id).update(product_data)
        except Exception as e:
            print(f"Error updating product: {e}")
            raise e

    @staticmethod
    def delete_product(product_id):
        try:
            return Database.db.child("products").child(product_id).remove()
        except Exception as e:
            print(f"Error deleting product: {e}")
            raise e