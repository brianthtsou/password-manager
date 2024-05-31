import tkinter as tk

class LoginPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Login").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Go to Page One", command=lambda: master.switch_frame("MainPage")).pack()