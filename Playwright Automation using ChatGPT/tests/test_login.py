import json

import pytest

from pageObjects.login import LoginPage
from pageObjects.logout import LogOut


with open("data/credentials.json") as f:
    test_data = json.load(f)
    user_credentials = test_data["user_credentials"]
    
@pytest.mark.parametrize("user_credentials", user_credentials)
def test_valid_login(browserInstance,user_credentials):
    login_page = LoginPage(browserInstance,user_credentials)
    login_page.navigate()
    login_page.login()
    assert browserInstance.get_by_text("All Courses").first.is_visible()
    logout = LogOut(browserInstance)
    logout.perform_logout()
    
def test_invalid_login(browserInstance):
    invalid_credentials = {
            "username": "raghavj987@gmail.com",
            "password": "test@12345"
        }
    login_page = LoginPage(browserInstance,invalid_credentials)
    login_page.navigate()
    login_page.open_login()
    login_page.enter_email()
    login_page.click_next()
    login_page.enter_password()
    login_page.click_sign_in()
    assert not browserInstance.get_by_text("The email and password you entered don't match").first.is_visible()
    
def test_empty_mail(browserInstance):
    invalid_credentials = {
        "username": "",
        "password": "test@1234"
    }
    login_page = LoginPage(browserInstance,invalid_credentials)
    login_page.navigate()
    login_page.open_login()
    login_page.enter_email()
    login_page.click_next()
    assert browserInstance.get_by_text("Enter your email address to continue").first.is_visible()
    
def test_empty_password(browserInstance):
    invalid_credentials = {
        "username": "raghavj987@gmail.com",
        "password": ""
    }
    login_page = LoginPage(browserInstance,invalid_credentials)
    login_page.navigate()
    login_page.open_login()
    login_page.enter_email()
    login_page.click_next()
    login_page.enter_password()
    login_page.click_sign_in()
    assert browserInstance.get_by_text("Enter your password").first.is_visible()