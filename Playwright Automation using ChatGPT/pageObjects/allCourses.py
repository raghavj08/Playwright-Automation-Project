import time

from pageObjects.instructors import Instructors


class AllCourses:
    def __init__(self,page):
        self.page = page
        
    def get_all_courses(self,choice):
        self.page.get_by_text("All Courses").first.click()
        self.page.locator(".form-control ").fill(choice)
        time.sleep(2)
        
    
    def select_course(self):
        self.page.locator(".cardLink").first.click()
        time.sleep(2)
        self.page.locator(".chapter-nav-link").nth(1).click()
        time.sleep(2)
        instructors = Instructors(self.page)
        return instructors