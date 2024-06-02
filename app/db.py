import sqlite3

def create_connection(db_file):
    connection = sqlite3.connect("database.db")
    print(f"Connected to {db_file}!")
    return connection

def setup_database(connection):
    cursor = connection.cursor()
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                   username TEXT NOT NULL UNIQUE, password TEXT NOT NULL)""")
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS logins (login_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                   user_id INTEGER NOT NULL, 
                   login_username TEXT NOT NULL, login_password TEXT NOT NULL, 
                   FOREIGN KEY(user_id) REFERENCES users(user_id))""")
    
    connection.commit()
    

