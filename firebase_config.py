# firebase_config.py
import pyrebase

config = {
    "apiKey": "AIzaSyCqyP8OxbpJrBWyB_j88a6O1Pv5XBu_WOs",
    "authDomain": "toko-6d695.firebaseapp.com",
    "databaseURL": "https://toko-6d695-default-rtdb.asia-southeast1.firebasedatabase.app",
    "storageBucket": "toko-6d695.appspot.com",
    "projectId": "toko-6d695"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

