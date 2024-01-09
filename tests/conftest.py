import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    print("\nAccessing driver fixture on conftest -> Creating chrome driver")
    
    # open Chrome browser
    #my_driver = webdriver.Chrome()
    
    # open Firefox browser
    #my_driver = webdriver.Firefox()

    # open Edge browser
    # with option - maximize window
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")
    my_driver = webdriver.Edge(options=options)
    
    yield my_driver
    
    print("\nClosing chrome driver")
    my_driver.quit()
