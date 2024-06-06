from app.gui.login_page import LoginPage
from app.gui.main_page import MainPage
from app.gui.create_new_user_page import CreateNewUserPage


class PageFactory:
    global page_dict
    page_dict = {
        "LoginPage": LoginPage,
        "MainPage": MainPage,
        "CreateNewUserPage": CreateNewUserPage,
    }

    def create_page(page_name, master):
        if page_name in page_dict:
            return page_dict[page_name](master)
        else:
            raise ValueError(f"Unknown page name: {page_name}")
