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
        input_row_2 = wait.until(ec.presence_of_element_located((By.XPATH, '//div[@id="row2"]//following::input')))

        # Verify Row 2 input field is displayed
        
        # we don´t need the find_element anymore -> the wait already uses the find_element
        #input_row_2 = driver.find_element(By.XPATH, '//div[@id="row2"]//following::input')
        
        assert input_row_2.is_displayed(), 'Row 2 is not displayed'