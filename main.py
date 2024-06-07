from app.gui.main_app import *
from app.db import *
import customtkinter as ctk


def main():
    connection = create_connection("database.db")
    setup_database(connection)
    connection.close()

    ctk.set_appearance_mode("dark")
    app = MainApp()
    app.geometry("600x480")
    # app.minsize(width=600, height=480)
    # app.maxsize(width=900, height=720)
    app.resizable(height=None, width=None)
    app.mainloop()


if __name__ == "__main__":
    main()
