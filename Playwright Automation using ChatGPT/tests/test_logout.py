import json

import pytest

from pageObjects.login import LoginPage
from pageObjects.logout import LogOut

with open("data/credentials.json") as f:
    test_data = json.load(f)
    user_credentials = test_data["user_credentials"]

@pytest.mark.parametrize("user_credentials",user_credentials)
def test_logout(browserInstance,user_credentials):
    login_page = LoginPage(browserInstance,user_credentials)
    login_page.navigate()
    login_page.login()
    logout = LogOut(browserInstance)
    logout.perform_logout()
    assert browserInstance.get_by_text("Sign In").first.is_visible()
    