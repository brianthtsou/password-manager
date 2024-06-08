import tkinter as tk
import customtkinter as ctk
from app.login_manager import *


class MainPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.parent_frame = self

        lm = LoginManager()
        lm.fetch_logins(master._active_user)

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
