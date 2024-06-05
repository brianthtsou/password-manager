import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from app.user_manager import *

class LoginPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        headerFont = tkFont.Font(family="Arial",size=24,weight="bold")
        tk.Label(self, text="Password Manager", font=headerFont).grid(row = 0, column=0, columnspan=2, sticky="EW", pady= 20, padx=10)
        tk.Button(self, text="Login", command=lambda: self.login(master)).grid(row = 3, column = 0, columnspan=2)
        tk.Button(self, text="Create New User", command=lambda: master.switch_frame("CreateNewUserPage")).grid(row = 4, column = 0, columnspan=2)

        self.username_var=tk.StringVar()
        self.password_var=tk.StringVar()

        username_label = tk.Label(self, text = "Username:")
        password_label = tk.Label(self, text = "Password:")

        username_label.grid(row = 1, column=0, pady= 2)
        password_label.grid(row = 2, column=0, pady= 2)

        username_entry = tk.Entry(self, textvariable=self.username_var)
        password_entry = tk.Entry(self, show="*", textvariable=self.password_var)

        username_entry.grid(row=1, column=1, pady=25)
        password_entry.grid(row=2, column = 1, pady = 25)

    
    def login(self, master):
        username = self.username_var.get()
        password = self.password_var.get()

        if (len(username) < 4):
            messagebox.showerror(title="Username Error", message="Username must be at least 4 characters long!")
            return

        if (len(password) < 4):
            messagebox.showerror(title="Password Error", message="Password must be at least 4 characters long!")
            return
        
        user_manager = UserManager()
        if (user_manager.validate_user_login(username, password)):
             user_manager.close_connection()
             master.switch_frame("MainPage")
        else:
            messagebox.showerror(title="Login Error", message="Incorrect credentials, please try again!")
            return

       
