# 59 - Homework

# 1. create exception page object
# 2. implement page objects in the exceptions tests  
from selenium import webdriver
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class ExceptionsPage(BasePage):

    __url = "https://practicetestautomation.com/practice-test-exceptions/"

    # locators
    __btn_add = (By.XPATH, '//button[@id="add_btn"]')
    __btn_save_row_1 = (By.XPATH, '//div[@id="row1"]//button[@id="save_btn"]')
    __btn_save_row_2 = (By.XPATH, '//div[@id="row2"]//button[@id="save_btn"]')
    __input_row_1 = (By.XPATH, '//div[@id="row1"]//following::input')
    __input_row_2 = (By.XPATH, '//div[@id="row2"]//following::input')
    __confirmation_banner = (By.XPATH, '//div[@id="confirmation"]')

    # constructor
    def __init__(self, driver: webdriver):
        super().__init__(driver)


    # method to open the page
    def _open(self):
        super()._open_url(self.__url)

    
    # method to add Row 2 input field
    def _add_row2(self):
        super()._click(self.__btn_add)
        super()._wait_until_element_is_visible(self.__input_row_2, time=6)


    # method to verify if Row 2 input field is displayed
    def _is_row2_displayed(self) -> bool:
        return super()._is_displayed(self.__input_row_2)
    

    # method add text in the row 2
    def _save_text_on_row2(self, text: str):
        super()._type(self.__input_row_2, text)
        super()._click(self.__btn_save_row_2)
        super()._wait_until_element_is_visible(self.__confirmation_banner)


    # method to verify if the text on row 2 was saved
    def _get_confirmation_message(self) -> str:
        return super()._get_text(self.__confirmation_banner)

        
    