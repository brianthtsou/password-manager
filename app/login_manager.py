import sqlite3
from app.hash_manager import *
from app.db import *


class LoginManager:
    def __init__(self):
        self.connection = create_connection("database.db")
        self.cursor = self.connection.cursor()

    def create_new_login(self, user_id, username, password):
        self.cursor.execute(
            "INSERT INTO logins (user_id, username, password) VALUES (?, ?, ?)",
            (user_id, username, password),
        )
        self.connection.commit()

    def close_connection(self):
        self.connection.close()
