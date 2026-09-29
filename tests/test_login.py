from pages.login_page import LoginPage
from pages.product_page import ProductPage


def test_valid_login(driver):
    login_page = LoginPage(driver)

    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    product_page = ProductPage(driver)

    assert product_page.get_products_title() == "Products"