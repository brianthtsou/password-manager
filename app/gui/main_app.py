import tkinter as tk
import customtkinter as ctk
from tkinter import *
from app.gui.page_factory import PageFactory


class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self._page = None
        self.switch_page("LoginPage")

    """Method to destroy the current page, replacing it with another; main way to switch between screens on the app."""

    def switch_page(self, page_name):
        new_page = PageFactory.create_page(
            page_name, self
        )  # instantiating a new page of the given parameter of page_name

        if self._page is not None:
            self._page.destroy()
        self._page = new_page
        self._page.pack(expand=True, fill="both")
