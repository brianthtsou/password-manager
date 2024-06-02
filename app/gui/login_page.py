import tkinter as tk
import tkinter.font as tkFont

class LoginPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        headerFont = tkFont.Font(family="Arial",size=24,weight="bold")
        tk.Label(self, text="Password Manager", font=headerFont).grid(row = 0, column=0, columnspan=2, sticky="EW", pady= 20, padx=10)
        tk.Button(self, text="Login", command=lambda: master.switch_frame("MainPage")).grid(row = 3, column = 0, columnspan=2)
        tk.Button(self, text="Create New User", command=lambda: master.switch_frame("CreateNewUserPage")).grid(row = 4, column = 0, columnspan=2)

        l1 = tk.Label(self, text = "Username:")
        l2 = tk.Label(self, text = "Password:")

        l1.grid(row = 1, column=0, pady= 2)
        l2.grid(row = 2, column=0, pady= 2)

        e1 = tk.Entry(self)
        e2 = tk.Entry(self)

        e1.grid(row=1, column=1, pady=25)
        e2.grid(row=2, column = 1, pady = 25)