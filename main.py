import time
from selenium import webdriver

# open browser
driver = webdriver.Chrome()
time.sleep(5)

# navigate to webpage
driver.get('https://practicetestautomation.com/practice-test-login/')
time.sleep(10)