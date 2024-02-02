import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class TestException:

    @pytest.mark.exceptions
    def test_TC02_1_no_such_element_exception(self, driver):
        
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # click Add btn
        btn_add = driver.find_element(By.XPATH, '//button[@id="add_btn"]')
        btn_add.click()

        # EXPLICIT WAIT
        # create a new instance of the WebDriverWait
        wait = WebDriverWait(driver, 10)

        # wait for the element
        # return the web element and assign it to the variable
        input_row_2_element = wait.until(ec.presence_of_element_located((By.XPATH, '//div[@id="row2"]//following::input')))

        # Verify Row 2 input field is displayed
        
        # we don´t need the find_element anymore -> the wait already uses the find_element and returns the web element
        #input_row_2_locator = driver.find_element(By.XPATH, '//div[@id="row2"]//following::input')
        
        assert input_row_2_element.is_displayed(), 'Row 2 is not displayed'

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_TC02_2_element_not_interactable_exception(self, driver):

        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # click Add btn
        btn_add = driver.find_element(By.XPATH, '//button[@id="add_btn"]')
        btn_add.click()

        # EXPLICIT WAIT
        # create a new instance of the WebDriverWait
        wait = WebDriverWait(driver, 10)
        input_row_2 = wait.until(ec.presence_of_element_located((By.XPATH, '//div[@id="row2"]//following::input')))

        # Type text into the second input field
        input_row_2.send_keys('Teste')

        # Click Save button using locator By.name(“Save”)
        btn_save = driver.find_element(By.XPATH, '//div[@id="row2"]//button[@id="save_btn"]')
        btn_save.click()

        # Verify saved text
        confirmation_banner = driver.find_element(By.XPATH, '//div[@id="confirmation"]')
        captured_message_text = confirmation_banner.text

        assert captured_message_text == 'Row 2 was saved', 'Text captured does not macth expected text'