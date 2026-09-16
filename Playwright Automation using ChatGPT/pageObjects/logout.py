import time

class LogOut:
    def __init__(self,page):
        self.page = page
        
    def perform_logout(self):
        self.page.get_by_text("Logout").first.click()
        time.sleep(5)