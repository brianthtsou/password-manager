import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from app.user_manager import *


class CreateNewUserPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.parent_frame = self

        # form_frame = ctk.CTkFrame(self)
        # form_frame.grid_columnconfigure(0, weight=1)
        # form_frame.pack()

        ctk.CTkLabel(self, text="Enter in a new username and password:").grid(
            row=0, column=0, pady=10, columnspan=3
        )

        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.reenter_password_var = tk.StringVar()

        username_label = ctk.CTkLabel(self, text="Username:").grid(
            row=1, column=1, pady=15
        )
        username_entry = ctk.CTkEntry(self, textvariable=self.username_var).grid(
            row=1, column=2, pady=15, padx=5
        )
        password_label = ctk.CTkLabel(self, text="Password:").grid(
            row=2, column=1, pady=15
        )
        password_entry = ctk.CTkEntry(
            self, show="*", textvariable=self.password_var
        ).grid(row=2, column=2, pady=15, padx=5)

        reenter_password_label = ctk.CTkLabel(
            self, text="Re-enter your password:"
        ).grid(row=3, column=1, pady=15)

        reenter_password_entry = ctk.CTkEntry(
            self, show="*", textvariable=self.reenter_password_var
        ).grid(row=3, column=2, pady=15, padx=5)

        ctk.CTkButton(
            self, text="Create", width=15, command=lambda: self.submit(master)
        ).grid(row=4, column=1, columnspan=2)
        ctk.CTkButton(
            self,
            text="Back",
            width=8,
            command=lambda: master.switch_page("LoginPage"),
        ).grid(row=5, column=1, columnspan=2, pady=5)

    def submit(self, master):
        username = self.username_var.get()
        password = self.password_var.get()
        reenter_password = self.reenter_password_var.get()

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

        if password != reenter_password:
            messagebox.showerror(
                title="Password Error", message="Passwords do not match!"
            )
            return

        user_manager = UserManager()
        user_manager.create_new_user(username, password)
        user_manager.close_connection()

        messagebox.showinfo(title="Success", message="New user successfully created!")

        master.switch_page("LoginPage")
