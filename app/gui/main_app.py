import tkinter as tk
from tkinter import *
from app.gui.frame_factory import FrameFactory

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self._frame = None
        self.switch_frame("LoginPage")
    
    """Method to destroy the current frame, replacing it with another; main way to switch between screens on the app."""
    def switch_frame(self, frame_name):
        new_frame = FrameFactory.create_frame(frame_name, self) # instantiating a new frame of the given parameter of frame_name
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
