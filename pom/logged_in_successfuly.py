from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class LogedInSuccessfully:
    
    __url = 'https://practicetestautomation.com/logged-in-successfully/'
    
    # locators
    __h1_tilte = (By.XPATH, '//h1[@class="post-title"]')
    __btn_log_out = (By.XPATH, '//a[contains(text(), "Log out")]')

    
    # constructor
    def __init__(self, driver: WebDriver):
        self._driver = driver


    # get current url
    # this method does not execute any step - it just return a string
    # so we can change it to be a property
    @property
    def current_url(self) -> str:
        return self._driver.get(self.__url)
    
    # get expected url
    # this method does not execute any step - it just return a string
    # so we can change it to be a property
    @property
    def expected_url(self) -> str:
        return self.__url
    
    # get the title text
    # this method does not execute any step - it just return a string
    # so we can change it to be a property
    @property
    def title_text(self) -> str:
        return self._driver.find_element(self.__h1_tilte).text
    
    # method to verify if logout btn is displayed
    def is_logout_btn_displayed(self) -> bool:
        return self._driver.find_element(self.__btn_log_out).is_displayed()
