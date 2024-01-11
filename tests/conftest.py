import pytest
from selenium import webdriver

@pytest.fixture()
def driver(request):

    # get the option selected in the command line
    browser = request.config.getoption("--browser")

    print(f"\nCreating {browser} driver")
    
    if browser == "chrome":
        # open Chrome browser
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        my_driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        # open Firefox browser
        my_driver = webdriver.Firefox()
    elif browser == "edge":
        # open Edge browser
        # with option - maximize window
        options = webdriver.EdgeOptions()
        options.add_argument("--start-maximized")
        my_driver = webdriver.Edge(options=options)
    else:
        raise TypeError("Expected 'chrome', 'edge' or firefox but got {browser}")
    
    my_driver.implicitly_wait(10)
    
    yield my_driver
    
    print(f"\nClosing {browser} driver")
    my_driver.quit()


# Method to add command line option
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser to run the tests: Chrome | Edge | Firefox"
    )
