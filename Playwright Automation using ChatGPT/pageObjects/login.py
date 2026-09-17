from pageObjects.all_courses import AllCourses
from playwright.sync_api import Page
from constants.constants import BASE_URL
from utils.decrypt import decrypt_password

class LoginPage:

    def __init__(self, page: Page, user_credentials = None):
        self.page = page
        self.user_credentials = user_credentials

    def navigate(self):
        self.page.goto(
            BASE_URL
        )

    def open_login(self):
        self.page.get_by_text("Sign In").first.click()
        self.page.get_by_text("Sign in with email").click()

    def enter_email(self):
        self.page.locator(
            'input[name="email"]'
        ).fill(self.user_credentials["username"])

    def click_next(self):
        self.page.get_by_role(
            "button",
            name="Next"
        ).click()

    def enter_password(self):
        encrypted_password = self.user_credentials["password"]

        password = decrypt_password(encrypted_password)

        self.page.locator(
            'input[name="password"]'
        ).fill(password)

    def click_sign_in(self):
        self.page.get_by_role(
            "button",
            name="Sign In"
        ).click()

    def login(self):
        self.open_login()
        self.enter_email()
        self.click_next()
        self.enter_password()
        self.click_sign_in()

        self.page.wait_for_timeout(2000)

        self.page.reload()

        return AllCourses(self.page)