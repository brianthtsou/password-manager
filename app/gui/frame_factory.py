from app.gui.login_page import LoginPage
from app.gui.main_page import MainPage

class FrameFactory:

    def create_frame(frame_name, master):
        if frame_name == "LoginPage":
            return LoginPage(master)
        elif frame_name == "MainPage":
            return MainPage(master)
        else:
            raise ValueError(f"Unknown frame name: {frame_name}")