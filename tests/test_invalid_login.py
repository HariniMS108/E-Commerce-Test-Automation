from pages.login_page import LoginPage


def test_invalid_login(driver):
    login_page = LoginPage(driver)

    login_page.enter_username("standard_user")
    login_page.enter_password("wrong_password")
    login_page.click_login()

    assert "Epic sadface" in login_page.get_error_message()