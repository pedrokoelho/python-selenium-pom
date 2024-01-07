"""
Tests Login Valid
TC0 login valid
"""

import pytest
import time
from selenium.webdriver.common.by import By


class TestLoginValid:
    
    @pytest.mark.smoke
    @pytest.mark.login
    @pytest.mark.valid
    def test_TC0_login_valid(self, driver):

        # open browser 
        # we get the driver through the driver fixture

        # navigate to webpage
        driver.get('https://practicetestautomation.com/practice-test-login/')
        time.sleep(2)

        # Type username student into Username field
        input_username = driver.find_element(By.NAME, 'username')
        input_username.send_keys('student')

        # Type password Password123 into Password field
        input_password = driver.find_element(By.NAME, 'password')
        input_password.send_keys('Password123')

        # Click Submit button
        btn_sumbit = driver.find_element(By.XPATH, '//button[@class="btn"]')
        btn_sumbit.click()

        # Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        url_captured = driver.current_url
        assert url_captured == 'https://practicetestautomation.com/logged-in-successfully/'

        # Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        text_captured = driver.find_element(By.XPATH, '//h1[@class="post-title"]').text
        assert text_captured == 'Logged In Successfully'  

        time.sleep(2)

        # Verify button Log out is displayed on the new page
        txt_btn_log_out = driver.find_element(By.XPATH, '//a[contains(text(), "Log out")]')
        assert txt_btn_log_out.is_displayed()