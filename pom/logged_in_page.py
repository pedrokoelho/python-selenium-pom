from selenium.webdriver.common.by import By
from selenium import webdriver
from pom.base_page import BasePage

class LogedInSuccessfully(BasePage):
    
    __url = 'https://practicetestautomation.com/logged-in-successfully/'
    
    # locators
    __h1_title = (By.XPATH, '//h1[@class="post-title"]')
    __btn_log_out = (By.XPATH, '//a[contains(text(), "Log out")]')

    
    # constructor
    def __init__(self, driver: webdriver):
        super().__init__(driver)
    
    # get expected url
    @property
    def expected_url(self) -> str:
        return self.__url
    
    # get the title text
    @property
    def title_text(self) -> str:
        return super()._get_text(self.__h1_title)
    
    # method to verify if logout btn is displayed
    def is_logout_btn_displayed(self) -> bool:
        return super()._is_displayed(self.__btn_log_out)
