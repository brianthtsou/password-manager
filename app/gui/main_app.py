import tkinter as tk
from tkinter import *
from tkinter import ttk

class MainApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(LoginPage)
    
    """Method to destroy the current frame, replacing it with another; main way to switch between screens on the app."""
    def switch_frame(self, frame_class):
        new_frame = frame_class(self) # instantiating a new frame of the given parameter of frame_class
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class LoginPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Login").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Go to Page One", command=lambda: master.switch_frame(PageOne)).pack()

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Page One").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Go to the Start Page", command=lambda: master.switch_frame(LoginPage)).pack()