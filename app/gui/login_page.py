import tkinter as tk
import customtkinter as ctk
import tkinter.font as tkFont
from tkinter import messagebox
from app.user_manager import *
from PIL import ImageTk, Image


class LoginPage(ctk.CTkFrame):
    def __init__(self, master):
        parent_frame = ctk.CTkFrame.__init__(self, master)

        icon_image = ctk.CTkImage(
            light_image=Image.open("password-manager-icon.png"),
            dark_image=Image.open("password-manager-icon.png"),
            size=(200, 200),
        )

        image_label = ctk.CTkLabel(parent_frame, image=icon_image, text="")

        image_label.pack(pady=20)

        login_field_frame = ctk.CTkFrame(parent_frame)
        login_field_frame.grid_columnconfigure(0, weight=1)

        username_label = ctk.CTkLabel(login_field_frame, text="Username:", padx=20)
        username_label.grid(column=0, row=0)

        password_label = ctk.CTkLabel(login_field_frame, text="Password:", padx=20)
        password_label.grid(column=0, row=1)

        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        username_entry = ctk.CTkEntry(login_field_frame, textvariable=self.username_var)
        username_entry.grid(column=1, row=0)
        password_entry = ctk.CTkEntry(login_field_frame, textvariable=self.password_var)
        password_entry.grid(column=1, row=1)

        login_button = ctk.CTkButton(
            login_field_frame, text="Login", command=lambda: self.login(master)
        ).grid(row=2, column=0, columnspan=2, pady=5)

        ctk.CTkButton(
            login_field_frame,
            text="Create New User",
            command=lambda: master.switch_page("CreateNewUserPage"),
        ).grid(row=3, column=0, columnspan=2, pady=5)

        login_field_frame.pack(side="bottom")

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
