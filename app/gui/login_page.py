import tkinter as tk

class LoginPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Login").grid(row = 0, column=0, columnspan=2, sticky="EW", pady= 20, padx=10)
        # tk.Button(self, text="Go to Page One", command=lambda: master.switch_frame("MainPage")).pack()

        l1 = tk.Label(self, text = "Username:")
        l2 = tk.Label(self, text = "Password:")

        l1.grid(row = 1, column=0, pady= 2)
        l2.grid(row = 2, column=0, pady= 2)

        e1 = tk.Entry(self)
        e2 = tk.Entry(self)

        e1.grid(row=1, column=1, pady=25)
        e2.grid(row=2, column = 1, pady = 25)