import json
import time

from playwright.sync_api import Page
import pytest
from pageObjects.login import LoginPage 

with open("data/credentials.json") as f:
    test_data = json.load(f)
    user_credentials_list = test_data["user_credentials"]

@pytest.mark.parametrize("user_credentials", user_credentials_list)
def test_main(browserInstance,user_credentials):
    login_page = LoginPage(browserInstance,user_credentials)
    login_page.navigate()
    all_courses = login_page.login()
    choice = "Playwright"
    all_courses.get_all_courses(choice)
    instructors = all_courses.select_course()
    certificate = instructors.get_instructors()
    logut = certificate.show_certificate()
    logut.perform_logout()