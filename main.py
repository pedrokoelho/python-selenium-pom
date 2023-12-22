import time
from selenium import webdriver
from utils.locators import LoginPageLocators

# open browser
driver = webdriver.Chrome()
time.sleep(5)

# navigate to webpage
driver.get('https://practicetestautomation.com/practice-test-login/')
time.sleep(10)

# Instatiate the locators
locator = LoginPageLocators()

# Type username student into Username field
input_username = driver.find_element(locator.input_username)
input_username.send_keys('')
# Type password Password123 into Password field

# Click Submit button

# Verify new page URL contains practicetestautomation.com/logged-in-successfully/

# Verify new page contains expected text ('Congratulations' or 'successfully logged in')

# Verify button Log out is displayed on the new page