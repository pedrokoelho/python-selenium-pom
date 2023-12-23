import time
from selenium import webdriver
from utils.locators import LoginPageLocators
from selenium.webdriver.common.by import By
# open browser
driver = webdriver.Chrome()

# navigate to webpage
driver.get('https://practicetestautomation.com/practice-test-login/')
time.sleep(2)

# Instatiate the locators
locator = LoginPageLocators()

# Type username student into Username field
input_username = driver.find_element(*locator.input_username)
input_username.send_keys('student')
# Type password Password123 into Password field
input_password = driver.find_element(*locator.input_password)
input_password.send_keys('Password123')
# Click Submit button
btn_sumbit = driver.find_element(*locator.btn_submit)
btn_sumbit.click()
# Verify new page URL contains practicetestautomation.com/logged-in-successfully/
url_page = driver.current_url
assert url_page == 'https://practicetestautomation.com/logged-in-successfully/'
# Verify new page contains expected text ('Congratulations' or 'successfully logged in')
text_captured = driver.find_element(*locator.txt_logged_in).text
assert text_captured == 'Logged In Successfully'  
# Verify button Log out is displayed on the new page
txt_btn_log_out = driver.find_element(*locator.txt_btn_log_out).text
assert txt_btn_log_out == 'Log out' 