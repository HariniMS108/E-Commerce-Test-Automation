from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        # Cart product
        self.cart_item = (
            By.CSS_SELECTOR,
            ".cart_item"
        )

        # Sauce Labs Backpack
        self.backpack_item = (
            By.CSS_SELECTOR,
            "[data-test='inventory-item']"
        )

        # Remove Sauce Labs Backpack
        self.remove_backpack_button = (
            By.CSS_SELECTOR,
            "[data-test='remove-sauce-labs-backpack']"
        )

        # Checkout
        self.checkout_button = (
            By.ID,
            "checkout"
        )

        # Continue shopping
        self.continue_shopping_button = (
            By.ID,
            "continue-shopping"
        )

    # -----------------------------------------
    # Get cart items
    # -----------------------------------------

    def get_cart_items(self):
        return self.driver.find_elements(
            *self.cart_item
        )

    # -----------------------------------------
    # Remove backpack
    # -----------------------------------------

    def remove_backpack(self):

        # Wait until cart page is loaded
        self.wait.until(
            EC.presence_of_element_located(
                self.cart_item
            )
        )

        # Find remove button
        remove_button = self.wait.until(
            EC.element_to_be_clickable(
                self.remove_backpack_button
            )
        )

        # Click remove
        remove_button.click()

        # Wait until the backpack remove button disappears
        self.wait.until(
            EC.invisibility_of_element_located(
                self.remove_backpack_button
            )
        )

    # -----------------------------------------
    # Checkout
    # -----------------------------------------

    def click_checkout(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.checkout_button
            )
        ).click()

    # -----------------------------------------
    # Continue shopping
    # -----------------------------------------

    def click_continue_shopping(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.continue_shopping_button
            )
        ).click()

    # -----------------------------------------
    # Wait for cart item
    # -----------------------------------------

    def wait_for_cart_item(self):

        self.wait.until(
            EC.presence_of_element_located(
                self.cart_item
            )
        )