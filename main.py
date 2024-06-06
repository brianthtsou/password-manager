from app.gui.main_app import *
from app.db import *
import sqlite3


def main():
    connection = create_connection("database.db")
    setup_database(connection)
    connection.close()

    app = MainApp()
    app.geometry("600x480")
    app.mainloop()


if __name__ == "__main__":
    main()
