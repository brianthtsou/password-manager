from app.gui.main_app import *
from app.db import *
import sqlite3

def main():
    connection = create_connection("database.db")
    create_tables(connection)

    app = MainApp()
    app.geometry("800x400")
    app.mainloop()

if __name__ == "__main__":
    main()