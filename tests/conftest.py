import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    print("\nAccessing driver fixture on conftest -> Creating chrome driver")
    # open browser
    my_driver = webdriver.Chrome()
    yield my_driver
    print("\nClosing chrome driver")
    my_driver.quit()
