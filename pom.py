class LoginPage:
    def __init__(self, page):
        self.page = page  # Playwright page object

    def login(self, username, password):
        self.page.fill("#username", username)
        self.page.fill("#password", password)
        self.page.click("button[type='submit']")

    def is_logged_in(self):
        return self.page.is_visible(".dashboard")


# Your test file — clean, readable
def test_valid_login(page):
    login = LoginPage(page)
    login.login("user@test.com", "pass123")
    assert login.is_logged_in() == True