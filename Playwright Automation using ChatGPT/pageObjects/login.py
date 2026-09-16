from pageObjects.allCourses import AllCourses
from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page, user_credentials = None):
        self.page = page
        self.user_credentials = user_credentials

    def navigate(self):
        self.page.goto(
            "https://testautomationu.applitools.com/"
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
        self.page.locator(
            'input[name="password"]'
        ).fill(self.user_credentials["password"])

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