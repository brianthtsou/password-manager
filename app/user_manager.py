import sqlite3
from app.hash_manager import *
from app.db import *

class UserManager:
    def __init__(self):
        self.connection = create_connection("database.db")
        self.cursor = self.connection.cursor()
    
    def create_new_user(self, username, password):
        hashed_password = HashManager.hash_password(password)
        self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        self.connection.commit()

    def validate_user_login(self, username, password):
        self.cursor.execute("SELECT password FROM users WHERE username = (?)", (username, ))
        result = self.cursor.fetchone()
        if result is None:
            print("Did not find user with the given username.")
            return False
        hashed_password = result[0]

        return HashManager.validate_password(password, hashed_password)
    
    def close_connection(self):
        self.connection.close()
    

