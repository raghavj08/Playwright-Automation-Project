
import pytest
import json

from pageObjects.login import LoginPage
from constants.constants import COURSE_FILTER_CHOICE_FIRST, COURSE_FILTER_CHOICE_SECOND

with open("data/credentials.json") as f:
    test_data = json.load(f)
    user_credentials = test_data["user_credentials"]
    
@pytest.mark.parametrize("user_credentials", user_credentials)
def test_valid_courses(browserInstance, user_credentials):
    login_page = LoginPage(browserInstance,user_credentials)
    login_page.navigate()
    all_courses = login_page.login()
    all_courses.get_all_courses(COURSE_FILTER_CHOICE_FIRST)
    assert browserInstance.locator(".cardLink").count() > 0
    

@pytest.mark.parametrize("user_credentials", user_credentials)
def test_invalid_courses(browserInstance, user_credentials):
    login_page = LoginPage(browserInstance,user_credentials)
    login_page.navigate()
    all_courses = login_page.login()
    all_courses.get_all_courses(COURSE_FILTER_CHOICE_SECOND)
    assert browserInstance.locator(".cardLink").count() == 0
    
    
@pytest.mark.parametrize("user_credentials", user_credentials)
def test_valid_course_chapters(browserInstance, user_credentials):
    login_page = LoginPage(browserInstance,user_credentials)
    login_page.navigate()
    all_courses = login_page.login()
    all_courses.get_all_courses(COURSE_FILTER_CHOICE_FIRST)
    all_courses.select_course()
    assert browserInstance.locator(".chapter-nav-link").count() >= 5
    
    
    

    
    
    
    