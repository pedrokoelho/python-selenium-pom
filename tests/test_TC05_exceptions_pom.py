import pytest
from page_objects.exceptions_page import ExceptionsPage

class TestException:

    @pytest.mark.exceptions
    @pytest.mark.pom
    def test_TC05_1_no_such_element_exception(self, driver):

        """
        In order to use page objects
        we need to create instances of the class
        """
        exceptions_page = ExceptionsPage(driver)

        # using the page object methods
        exceptions_page._open()
        exceptions_page._add_row2()
        assert exceptions_page._is_row2_displayed(), "Row 2 should be displayed"
    
    @pytest.mark.exceptions
    @pytest.mark.pom
    def test_TC05_2_element_not_interactable_exception(self, driver):
        
        # instantiating ExceptionsPage and sending the fixture
        exceptions_page = ExceptionsPage(driver)
        
        # using the page object methods
        
        # 1. Open page
        exceptions_page._open()
        # 2. Click Add button
        # 3. Wait for the second row to load
        exceptions_page._add_row2()
        # 4. Type text into the second input field
        # 5. Push Save button using locator By.name(“Save”)
        exceptions_page._save_text_on_row2('Testing...')
        # 6. Verify if confirmation message is 'Row 2 was saved'
        assert exceptions_page._get_confirmation_message() == 'Row 2 was saved', 'WARNING! Captured text does not match expected message!'
        
        print(f'Captured Text -> {exceptions_page._get_confirmation_message()}')

    
    @pytest.mark.exceptions
    @pytest.mark.pom
    def test_TC02_3_invalid_element_state_exception(self, driver):

        # instantiating ExceptionsPage and sending the fixture
        exceptions_page = ExceptionsPage(driver)
        
        # using the page object methods
        
        # 1. Open page
        exceptions_page._open()

        # 2. Clear input field
        # 3. Type text into the input field
        exceptions_page._edit_text_in_row_1_input('Francesinha')

        # 4. Verify text changed
        assert exceptions_page._get_confirmation_message() == 'Row 1 was saved', 'WARNING! Captured text does not match expected text!'


    @pytest.mark.exceptions
    @pytest.mark.pom
    def test_TC02_4_stale_element_reference_exception(self, driver):

        # instantiating ExceptionsPage and sending the fixture
        exceptions_page = ExceptionsPage(driver)
        
        # using the page object methods
        
        # 1. Open page
        exceptions_page._open()

         # 2. click Add btn
        exceptions_page._add_row2()

        # 3. Verify instruction text element is no longer displayed
        assert not exceptions_page._are_instructions_displayed(), 'Instructions text should not be displayed!'


    @pytest.mark.exceptions
    @pytest.mark.pom
    @pytest.mark.debug
    def test_TC02_5_timeout_exception(self, driver):

        # instantiating ExceptionsPage and sending the fixture
        exceptions_page = ExceptionsPage(driver)
        
        # using the page object methods
        
        # 1. Open page
        exceptions_page._open()

        #Click Add button
        exceptions_page._add_row2()

        #Verify second input field is displayed
        assert exceptions_page._is_row2_displayed(), 'Row 2 is not dispalyed'