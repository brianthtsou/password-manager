from app.gui.login_page import LoginPage
from app.gui.main_page import MainPage
from app.gui.create_new_user_page import CreateNewUserPage

class FrameFactory:
    global page_dict  
    page_dict = {
        "LoginPage": LoginPage,
        "MainPage": MainPage,
        "CreateNewUserPage": CreateNewUserPage,
    }
    def create_frame(frame_name, master):
        if frame_name in page_dict:
            return page_dict[frame_name](master)
        else:
            raise ValueError(f"Unknown frame name: {frame_name}")
        
        