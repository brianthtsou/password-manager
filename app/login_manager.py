import sqlite3
from app.hash_manager import *
from app.db import *


class LoginManager:
    def __init__(self):
        self.connection = create_connection("database.db")
        self.cursor = self.connection.cursor()

    def create_new_login(self, user_id, login_username, login_password, login_website):
        self.cursor.execute(
            "INSERT INTO logins (user_id, login_username, login_password, login_website) VALUES (?, ?, ?, ?)",
            (user_id, login_username, login_password, login_website),
        )
        self.connection.commit()

    def get_active_user_id(self, active_user):
        self.cursor.execute(
            "SELECT user_id FROM users WHERE username = (?)", (active_user,)
        )
        user_id = self.cursor.fetchone()
        if user_id:
            print(user_id)
            return user_id[0]
        else:
            print("No user_id found!")
            return None

    def fetch_logins(self, active_user):
        user_id = self.get_active_user_id(active_user)
        self.cursor.execute(
            "SELECT login_username, login_password, login_website FROM logins WHERE user_id = (?)",
            (user_id,),
        )
        logins = self.cursor.fetchall()
        print(logins)

    def close_connection(self):
        self.connection.close()
