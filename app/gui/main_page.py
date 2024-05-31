import tkinter as tk

class MainPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Page One").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Go to the Start Page", command=lambda: master.switch_frame("LoginPage")).pack()
        
        