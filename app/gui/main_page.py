import tkinter as tk


class MainPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.parent_frame = self
        tk.Label(self, text="Page One").pack(side="top", fill="x", pady=10)
        tk.Button(
            self,
            text="Go to the Start Page",
            command=lambda: master.switch_page("LoginPage"),
        ).pack()
