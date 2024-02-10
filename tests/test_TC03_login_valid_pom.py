import pytest
from page_objects.login_page import LoginPage
from page_objects.logged_in_page import LogedInSuccessfullyPage


class TestLoginValidPom:
    
    @pytest.mark.smoke
    @pytest.mark.login
    @pytest.mark.valid
    @pytest.mark.pom
    def test_TC03_login_valid_pom(self, driver):
        """
        In order to use page objects
        we need to create instances of the class
        """
        login_page = LoginPage(driver)
        logged_in_page = LogedInSuccessfullyPage(driver)

        login_page.open()
        login_page.login("student", "Password123")

        assert logged_in_page.expected_url == logged_in_page.current_url, "Actual URL does not match expected"
        assert logged_in_page.title_text == "Logged In Successfully", "Captured text does not match expected"
        assert logged_in_page.is_logout_btn_displayed(), "Logout button should be displayed"
