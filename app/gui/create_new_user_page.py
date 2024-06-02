import tkinter as tk

class CreateNewUserPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Enter in a new username and password:").grid(row = 0, column=0, columnspan=2, sticky="EW", pady= 50, padx=10)
        tk.Button(self, text="Create", command=lambda: master.switch_frame("LoginPage")).grid(row = 4, column = 0, columnspan=2)

        l1 = tk.Label(self, text = "Username:")
        l2 = tk.Label(self, text = "Password:")
        l3 = tk.Label(self, text = "Re-enter your password:")

        l1.grid(row = 1, column=0, pady= 10)
        l2.grid(row = 2, column=0, pady= 10)
        l3.grid(row = 3, column=0, pady= 10)

        e1 = tk.Entry(self)
        e2 = tk.Entry(self)
        e3 = tk.Entry(self)

        e1.grid(row=1, column=1, pady=10)
        e2.grid(row=2, column = 1, pady = 10)
        e3.grid(row=3, column = 1, pady = 10)