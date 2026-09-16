from pageObjects.dashBoard import DashBoard
import time


class LoginPage:
    def __init__(self, page,user_credentials):
        self.page = page
        self.user_credentials = user_credentials
        pass
    
    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client")
        
    def login(self):
        self.page.get_by_placeholder("email@example.com").fill(self.user_credentials["userEmail"])
        self.page.get_by_placeholder("enter your passsword").fill(self.user_credentials["user_password"])
        print("Hello")
        self.page.get_by_role("button",name = "Login").click()
        print("Hello")
        dashBoard = DashBoard(self.page)
        return dashBoard