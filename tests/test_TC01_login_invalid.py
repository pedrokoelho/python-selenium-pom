"""
Test Case 01
Invalid Login
"""

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLoginInvalid:

    @pytest.mark.smoke
    @pytest.mark.login
    @pytest.mark.invalid
    def test_TC01_login_invalid(self):

        # open browser
        driver = webdriver.Chrome()

        # Open page
        driver.get('https://practicetestautomation.com/practice-test-login/')
        time.sleep(2)

        # Type username incorrectUser into Username field
        input_username = driver.find_element(By.NAME, 'username')
        input_username.send_keys('incorrectUser')

        # Type password Password123 into Password field
        input_password = driver.find_element(By.NAME, 'password')
        input_password.send_keys('Password123')

        # Click Submit button
        btn_sumbit = driver.find_element(By.XPATH, '//button[@class="btn"]')
        btn_sumbit.click()
        time.sleep(2)

        # Verify error message is displayed
        banner_username_error = driver.find_element(By.XPATH, '//div[@id="error"]')
        assert banner_username_error.is_displayed()
        
        # Verify error message text is Your username is invalid!
        txt_username_error = banner_username_error.text
        assert txt_username_error == 'Your username is invalid!'
