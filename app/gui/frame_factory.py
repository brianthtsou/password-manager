from app.gui.login_page import LoginPage
from app.gui.main_page import MainPage

class FrameFactory:
    global page_dict  
    page_dict = {
        "LoginPage": LoginPage,
        "MainPage": MainPage,
    }
    def create_frame(frame_name, master):
        if frame_name in page_dict:
            return page_dict[frame_name](master)
        else:
            raise ValueError(f"Unknown frame name: {frame_name}")
        
        