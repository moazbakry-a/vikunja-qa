from playwright.sync_api import Page
class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = self.page.get_by_label("Username")
        self.password_input = self.page.get_by_role("textbox", name="Password")
        self.login_button = self.page.get_by_role("button", name="Login")
        self.stay_logged_in_checkbox = self.page.get_by_role("checkbox", name="Stay logged in")
        self.wrong_message = self.page.get_by_text("Wrong username or password.")
        self.empty_username_message = self.page.get_by_text("Please provide a username.")
        self.empty_password_message = self.page.get_by_text("Please provide a password.")

    def navigate_to_login_page(self):
        self.page.goto("http://localhost:3456/login")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()