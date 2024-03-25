from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException

class BasePage:

    # constructor
    def __init__(self, driver: webdriver):
        self._driver = driver

    
    # method to find the element
    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)
 
    
    # method to type text
    def _type(self, locator: tuple, text: str, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).send_keys(text)
    
    
    # method to clear the text
    def _clear_text(self, Locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(Locator, time)
        self._find(Locator).clear()

    
    # method to click 
    def _click(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click()

    
    # method to wait until element is visible
    def _wait_until_element_is_visible(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))


    # method to wait until element is clickable
    def _wait_until_element_is_clickable(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.element_to_be_clickable(locator))
    

    @property
    def current_url(self) -> str:
        return self._driver.current_url
    
    
    # method to verify if element is displayed
    def _is_displayed(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False


    # method to open the page
    def _open_url(self, url: str):
        # 1. navigate to page
        self._driver.get(url)


    # method to get text
    def _get_text(self, locator: tuple, time: int = 10) -> str:
        self._wait_until_element_is_visible(locator, time)
        return self._find(locator).text


