from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from page_objects.base_page import BasePage


class LoginPage(BasePage):

    __url = 'https://practicetestautomation.com/practice-test-login/'
    
    # locators
    __txt_input_username = (By.NAME, 'username')
    __txt_input_password = (By.NAME, 'password')
    __btn_sumbit = (By.XPATH, '//button[@class="btn"]')
    __banner_error = (By.XPATH, '//div[@id="error"]')

    # constructor
    def __init__(self, driver: webdriver):
        super().__init__(driver)

    # method to open the page
    def open(self):
        # 1. navigate to page
        super()._open_url(self.__url)

    # method to login
    def login(self, username: str, password: str):
        # 1. Type username into Username field
        super()._type(self.__txt_input_username, username)
        # 2. Type password into Password field
        super()._type(self.__txt_input_password, password)
        # 3. Click button
        super()._click(self.__btn_sumbit)


    # method to get the error msg
    def get_error_msg(self) -> str:
        return super()._get_text(self.__banner_error, time = 3)
