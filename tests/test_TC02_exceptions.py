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
        # return the web element and assign it to the variable
        input_row_2_element = wait.until(ec.presence_of_element_located((By.XPATH, '//div[@id="row2"]//following::input')))

        # Verify Row 2 input field is displayed
        
        # we don´t need the find_element anymore -> the wait already uses the find_element and returns the web element
        #input_row_2_locator = driver.find_element(By.XPATH, '//div[@id="row2"]//following::input')
        
        assert input_row_2_element.is_displayed(), 'Row 2 is not displayed'

    @pytest.mark.exceptions
    def test_TC02_2_element_not_interactable_exception(self, driver):

        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # click Add btn
        btn_add = driver.find_element(By.XPATH, '//button[@id="add_btn"]')
        btn_add.click()

        # EXPLICIT WAIT
        # create a new instance of the WebDriverWait
        wait = WebDriverWait(driver, 10)
        input_row_2 = wait.until(ec.presence_of_element_located((By.XPATH, '//div[@id="row2"]//following::input')))

        # Type text into the second input field
        input_row_2.send_keys('Teste')

        # Click Save button using locator By.name(“Save”)
        btn_save = driver.find_element(By.XPATH, '//div[@id="row2"]//button[@id="save_btn"]')
        btn_save.click()

        # Verify saved text
        confirmation_banner = driver.find_element(By.XPATH, '//div[@id="confirmation"]')
        captured_message_text = confirmation_banner.text

        assert captured_message_text == 'Row 2 was saved', 'Text captured does not macth expected text'


    @pytest.mark.exceptions
    def test_TC02_3_invalid_element_state_exception(self, driver):

        # Open page
        driver.get('https://practicetestautomation.com/practice-test-exceptions/')

        # Click Edit button
        btn_edit = driver.find_element(By.XPATH, '//button[@id="edit_btn"]')
        btn_edit.click()

        # Before Clear the text in the first input field
        input_row_1 = driver.find_element(By.XPATH, '//div[@id="row1"]//following::input')

        # Adding a wait for the element to be clickable
        wait = WebDriverWait(driver, 10)
        wait.until(ec.element_to_be_clickable(input_row_1))

        # Clear the text in the first input field
        input_row_1.clear()

        # Type text into the input field
        input_row_1.send_keys('Test case 3: InvalidElementStateException')
        
        # Verify text changed
        # in this case is an input field - we can't use text - we have to get the atribute value
        captured_text = input_row_1.get_attribute('value')
        assert captured_text == 'Test case 3: InvalidElementStateException', 'Text captured > ' + captured_text + ' does not macth expected text'


    @pytest.mark.exceptions
    def test_TC02_4_stale_element_reference_exception(self, driver):

        # Open page
        driver.get('https://practicetestautomation.com/practice-test-exceptions/')

        # Find the instructions text element
        txt_instructions = driver.find_element(By.XPATH, '//p[@id="instructions"]')

        # click Add btn
        btn_add = driver.find_element(By.XPATH, '//button[@id="add_btn"]')
        btn_add.click()

        # Verify instruction text element is no longer displayed
        wait = WebDriverWait(driver, 10)
        assert wait.until(ec.invisibility_of_element_located((By.XPATH, '//p[@id="instructions"]')), 'Instructions text element should not be displayed!')
        
        # if we assert if is displayed we get an StaleElementReferenceException
        # because the element is no longer on the DOM
        # we have to use the above wait 
        
        # assert not txt_instructions.is_displayed(), 'Instructions text element should not be displayed!'


    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_TC02_5_timeout_exception(self, driver):

        # Open page
        driver.get('https://practicetestautomation.com/practice-test-exceptions/')

        # click Add btn
        btn_add = driver.find_element(By.XPATH, '//button[@id="add_btn"]')
        btn_add.click()

        # EXPLICIT WAIT
        # create a new instance of the WebDriverWait
        wait = WebDriverWait(driver, 6)

        # wait for the element
        # return the web element and assign it to the variable
        input_row_2_element = wait.until(ec.visibility_of_element_located((By.XPATH, '//div[@id="row2"]//following::input')), 'Row 2 input field is not displayed')
        
        assert input_row_2_element.is_displayed(), 'Row 2 input field is not displayed'

