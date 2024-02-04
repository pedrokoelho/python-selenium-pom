from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage:

    __url = 'https://practicetestautomation.com/practice-test-login/'
    
    # locators
    __txt_input_username = (By.NAME, 'username')
    __txt_input_password = (By.NAME, 'password')
    __btn_sumbit = (By.XPATH, '//button[@class="btn"]')
    __banner_username_error = (By.XPATH, '//div[@id="error"]')

    # constructor
    def __init__(self, driver: WebDriver):
        self._driver = driver

    # method to open the page
    def open(self):
        self._driver.get(self.__url)

    # method to login
    def login(self, usernme: str, password: str):
        wait = WebDriverWait(self._driver, 5)
        wait.until(ec.visibility_of_element_located(self.__txt_input_password))
        self._driver.find_element(self.__txt_input_username).send_keys(usernme)
        wait.until(ec.visibility_of_element_located(self.__txt_input_password))
        self._driver.find_element(self.__txt_input_password).send_keys(password)
        wait.until(ec.element_to_be_clickable(self.__btn_sumbit))
        self._driver.find_element(self.__btn_sumbit).click