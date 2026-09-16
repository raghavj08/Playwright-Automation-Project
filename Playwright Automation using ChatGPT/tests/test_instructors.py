from pageObjects.instructors import Instructors
from pageObjects.login import LoginPage


def test_instructor(browserInstance):
    login_page = LoginPage(browserInstance)
    login_page.navigate()
    instructors = Instructors(browserInstance)
    instructors.goto_instructors()
    assert browserInstance.locator(".card-instructor").count() > 0
    
def test_instructor_course(browserInstance):
    login_page = LoginPage(browserInstance)
    login_page.navigate()
    instructors = Instructors(browserInstance)
    instructors.goto_instructors()
    instructors.select_instructor()
    instructors.select_instructor_courses()
    assert browserInstance.get_by_text("Instructor Profile").is_visible()
    

