from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


def login(driver):

    login_page = LoginPage(driver)

    login_page.enter_username("standard_user")

    login_page.enter_password("secret_sauce")

    login_page.click_login()


def test_shopping_cart(driver):

    # Login
    login(driver)

    # Create ProductPage object
    product_page = ProductPage(driver)

    # Add backpack to cart
    product_page.add_backpack_to_cart()

    # Open cart
    product_page.click_cart()

    # Wait for cart page
    WebDriverWait(driver, 10).until(
        EC.url_contains("cart.html")
    )

    # Create CartPage object
    cart_page = CartPage(driver)

    # Get cart items
    cart_items = cart_page.get_cart_items()

    # Check that cart contains product
    assert len(cart_items) > 0


def test_remove_product(driver):

    # Login
    login(driver)

    # Create ProductPage object
    product_page = ProductPage(driver)

    # Add backpack
    product_page.add_backpack_to_cart()

    # Open cart
    product_page.click_cart()

    # Wait for cart page
    WebDriverWait(driver, 10).until(
        EC.url_contains("cart.html")
    )

    # Create CartPage object
    cart_page = CartPage(driver)

    # Remove backpack
    cart_page.remove_backpack()

    # Get cart items
    cart_items = cart_page.get_cart_items()

    # Check cart is empty
    assert len(cart_items) == 0


def test_checkout_button(driver):

    # Login
    login(driver)

    # Create ProductPage object
    product_page = ProductPage(driver)

    # Add backpack
    product_page.add_backpack_to_cart()

    # Open cart
    product_page.click_cart()

    # Wait for cart page
    WebDriverWait(driver, 10).until(
        EC.url_contains("cart.html")
    )

    # Create CartPage object
    cart_page = CartPage(driver)

    # Click checkout
    cart_page.click_checkout()

    # Wait for checkout page
    WebDriverWait(driver, 10).until(
        EC.url_contains("checkout-step-one.html")
    )

    # Verify checkout page
    assert "checkout-step-one.html" in driver.current_url