import time

from pageObjects.certificate import Certificate


class Instructors:
    def __init__(self,page):
        self.page = page
        
    def goto_instructors(self):
        self.page.get_by_text("Instructors").first.click()
        time.sleep(2)
    
    def select_instructor(self):
        self.card = self.page.locator(".card-instructor").first
        time.sleep(2)
        
    def select_instructor_courses(self):
        self.card.get_by_text("See Courses").click()
        time.sleep(2)
        
    def get_instructors(self):
        self.goto_instructors()
        self.select_instructor()
        self.select_instructor_courses()
        certificate = Certificate(self.page)
        return certificate
        