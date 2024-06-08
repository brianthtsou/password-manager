import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox


class CreateNewLoginPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.parent_frame = self

        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        username_label = ctk.CTkLabel(self, text="Username:").grid(row=0, column=0)
        username_entry = ctk.CTkEntry(self, textvariable=self.username_var).grid(
            row=0, column=1
        )

        password_label = ctk.CTkLabel(self, text="Password:").grid(row=2, column=0)
        password_entry = ctk.CTkEntry(
            self, show="*", textvariable=self.password_var
        ).grid(row=2, column=1)

        ctk.CTkButton(
            self, text="Create", width=15, command=lambda: self.submit(master)
        ).grid(row=3, column=1, columnspan=2)
        ctk.CTkButton(
            self,
            text="Back",
            width=8,
            command=lambda: master.switch_page("MainPage"),
        ).grid(row=4, column=1, columnspan=2, pady=5)

    def submit(self, master):
        username = self.username_var.get()
        password = self.password_var.get()

        messagebox.showinfo(title="Success", message="New login successfully created!")

        master.switch_page("MainPage")
