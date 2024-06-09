import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from app.login_manager import *


class MainPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.parent_frame = self

        lm = LoginManager()
        logins = lm.fetch_logins(master._active_user)

        cols = ("Username", "Password", "Website")
        tree = ttk.Treeview(master, columns=cols, show="headings")

        for col in cols:
            tree.heading(col, text=col)

        for login in logins:
            tree.insert("", "end", values=login)

        tree.pack(side="top")

        ctk.CTkLabel(self, text=master._active_user).pack(side="top")
        ctk.CTkButton(
            self,
            text="Go to the Start Page",
            command=lambda: master.switch_page("LoginPage"),
        ).pack(side="bottom")
        ctk.CTkButton(
            self,
            text="Create New Login",
            command=lambda: master.switch_page("CreateNewLoginPage"),
        ).pack(side="bottom", pady=10)
