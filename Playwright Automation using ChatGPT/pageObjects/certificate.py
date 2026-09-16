import time

from pageObjects.logout import LogOut


class Certificate:
    def __init__(self,page):
        self.page = page
        
    def show_certificate(self):
        self.page.get_by_text("Certificates").first.click()
        time.sleep(2)
        logout = LogOut(self.page)
        return logout