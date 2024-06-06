import tkinter as tk
import customtkinter as ctk
import tkinter.font as tkFont
from tkinter import messagebox
from app.user_manager import *


class LoginPage(ctk.CTkFrame):
    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master)
        welcome_label = ctk.CTkLabel(master, text="Welcome!")
        welcome_label.pack(pady=20)

    def login(self, master):
        username = self.username_var.get()
        password = self.password_var.get()

        if len(username) < 4:
            messagebox.showerror(
                title="Username Error",
                message="Username must be at least 4 characters long!",
            )
            return

        if len(password) < 4:
            messagebox.showerror(
                title="Password Error",
                message="Password must be at least 4 characters long!",
            )
            return

        user_manager = UserManager()
        if user_manager.validate_user_login(username, password):
            user_manager.close_connection()
            master.switch_frame("MainPage")
        else:
            messagebox.showerror(
                title="Login Error", message="Incorrect credentials, please try again!"
            )
            return
