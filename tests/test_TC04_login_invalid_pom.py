import pytest
from page_objects.login_page import LoginPage


class TestLoginInValidPom:
    
    @pytest.mark.smoke
    @pytest.mark.login
    @pytest.mark.invalid
    @pytest.mark.pom
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("incorrectUser", "Password123", "Your username is invalid!"),
                              ("student", "incorrectPassword", "Your password is invalid!")])
    def test_TC04_login_invalid_pom(self, driver, username, password, expected_error_message):

        login_page = LoginPage(driver)

        login_page.open()
        login_page.login(username, password)

        assert login_page.get_error_msg() == expected_error_message, "Error message does not match expected message!"