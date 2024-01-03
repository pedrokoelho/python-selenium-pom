from selenium.webdriver.common.by import By


class LoginPageLocators:

    # constructor
    def __init__(self):
        # locators
        self.input_username = (By.NAME, 'username')
        self.input_password = (By.NAME, 'password')
        self.btn_submit = (By.XPATH, '//button[@class="btn"]')
        self.banner_username_error = (By.XPATH, '//div[@id="error"]')
        


class LoggedInPageLocators:

    # constructor
    def __init__(self):
        # locators
        self.txt_logged_in = (By.XPATH, '//h1[@class="post-title"]')
        self.txt_btn_log_out = (By.XPATH, '//a[contains(text(), "Log out")]')
               