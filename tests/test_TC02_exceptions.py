import pytest
from selenium.webdriver.common.by import By

class TestException:

    @pytest.mark.exceptions
    def test_TC02_1_exception(self, driver):
        
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # click Add btn
        btn_add = driver.find_element(By.XPATH, '//button[@id="add_btn"]')
        btn_add.click()

        # Verify Row 2 input field is displayed
        input_row_2 = driver.find_element(By.XPATH, '//div[@id="row2"]//following::input')
        assert input_row_2.is_displayed(), 'Row 2 is not displayed'