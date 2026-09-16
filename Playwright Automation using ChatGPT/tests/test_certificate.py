import json

import pytest

from pageObjects.certificate import Certificate
from pageObjects.login import LoginPage

with open("data/credentials.json") as f:
    test_data = json.load(f)
    user_credentials = test_data["user_credentials"]

@pytest.mark.parametrize("user_credentials", user_credentials)
def test_certificate(browserInstance,user_credentials):
    login_page = LoginPage(browserInstance,user_credentials)
    login_page.navigate()
    login_page.login()
    certificate_page = Certificate(browserInstance)
    certificate_page.show_certificate()
    assert browserInstance.get_by_text("You don't have any certificates yet.").is_visible()