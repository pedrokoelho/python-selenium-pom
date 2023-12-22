from selenium.webdriver.common.by import By


class LoginPageLocators:

    # constructor
    def __init__(self):
        # locators
        self.input_username = (By.NAME, 'username')
        self.input_password = (By.NAME, 'password')
        self.btn_submit = (By.XPATH, '//button[@class="btn"]')