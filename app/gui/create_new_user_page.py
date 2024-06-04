import tkinter as tk
from tkinter import messagebox
from app.user_manager import *

class CreateNewUserPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Enter in a new username and password:").grid(row = 0, column=0, columnspan=2, sticky="EW", pady= 50, padx=10)
        tk.Button(self, text="Create", width=15, command=lambda: self.submit(master)).grid(row = 4, column = 0, columnspan=2, pady=10)
        tk.Button(self, text="Back", width=8, command=lambda: master.switch_frame("LoginPage")).grid(row = 5, column = 0, columnspan=2)

        username_label = tk.Label(self, text = "Username:")
        password_label = tk.Label(self, text = "Password:")
        reenter_password_label = tk.Label(self, text = "Re-enter your password:")

        username_label.grid(row = 1, column=0, pady= 10)
        password_label.grid(row = 2, column=0, pady= 10)
        reenter_password_label.grid(row = 3, column=0, pady= 10)

        self.username_var=tk.StringVar()
        self.password_var=tk.StringVar()
        self.reenter_password_var=tk.StringVar()

        username_entry = tk.Entry(self, textvariable=self.username_var)
        password_entry = tk.Entry(self, show="*", textvariable=self.password_var)
        reenter_password_entry = tk.Entry(self, show="*", textvariable=self.reenter_password_var)

        username_entry.grid(row=1, column=1, pady=10)
        password_entry.grid(row=2, column = 1, pady = 10)
        reenter_password_entry.grid(row=3, column = 1, pady = 10)

    def submit(self, master):
        username = self.username_var.get()
        password = self.password_var.get()
        reenter_password = self.reenter_password_var.get()

        if (len(username) < 4):
            messagebox.showerror(title="Username Error", message="Username must be at least 4 characters long!")
            return

        if (len(password) < 4):
            messagebox.showerror(title="Password Error", message="Password must be at least 4 characters long!")
            return

        if (password != reenter_password):
            messagebox.showerror(title="Password Error", message="Passwords do not match!")
            return
        
        user_manager = UserManager()
        user_manager.create_new_user(username, password)
        user_manager.close_connection()
        
        messagebox.showinfo(title="Success", message="New user successfully created!")

        master.switch_frame("LoginPage")