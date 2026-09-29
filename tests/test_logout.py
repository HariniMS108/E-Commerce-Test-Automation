from pages.login_page import LoginPage


def test_logout(driver):
    login_page = LoginPage(driver)

    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    login_page.click_logout()

    assert "saucedemo.com" in driver.current_url