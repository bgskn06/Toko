import pyrebase
from firebase_config import get_firebase_config

class Database:
    config = get_firebase_config()
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()

    @staticmethod
    def get_user(user_id):
        try:
            user = Database.db.child("users").child(user_id).get()
            if user.val():
                return user.val()
            return None
        except Exception as e:
            print(f"Error getting user data: {e}")
            return None

    @staticmethod
    def update_user(user_id, user_data):
        try:
            Database.db.child("users").child(user_id).update(user_data)
            print("User data updated successfully.")
        except Exception as e:
            print(f"Error updating user data: {e}")
