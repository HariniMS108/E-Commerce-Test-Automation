import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


def test_checkout_product():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # -------------------------------------------------
        # 1. Open SauceDemo
        # -------------------------------------------------
        driver.get(BASE_URL)

        # -------------------------------------------------
        # 2. Login
        # -------------------------------------------------
        wait.until(
            EC.visibility_of_element_located(
                (By.ID, "user-name")
            )
        ).send_keys(USERNAME)

        driver.find_element(By.ID, "password").send_keys(PASSWORD)

        driver.find_element(By.ID, "login-button").click()

        # -------------------------------------------------
        # 3. Verify products page
        # -------------------------------------------------
        wait.until(
            EC.visibility_of_element_located(
                (By.ID, "inventory_container")
            )
        )

        # -------------------------------------------------
        # 4. Add product to cart
        # -------------------------------------------------
        wait.until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-backpack")
            )
        ).click()

        # -------------------------------------------------
        # 5. Open cart
        # -------------------------------------------------
        wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "shopping_cart_link")
            )
        ).click()

        # -------------------------------------------------
        # 6. Verify cart
        # -------------------------------------------------
        wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "cart_item")
            )
        )

        assert "Sauce Labs Backpack" in driver.page_source

        # -------------------------------------------------
        # 7. Click checkout
        # -------------------------------------------------
        wait.until(
            EC.element_to_be_clickable(
                (By.ID, "checkout")
            )
        ).click()

        # -------------------------------------------------
        # 8. Verify checkout step one
        # -------------------------------------------------
        wait.until(
            EC.url_contains("checkout-step-one")
        )

        assert "checkout-step-one" in driver.current_url

        # -------------------------------------------------
        # 9. Enter checkout information
        # -------------------------------------------------
        wait.until(
            EC.visibility_of_element_located(
                (By.ID, "first-name")
            )
        ).send_keys("Test")

        driver.find_element(
            By.ID, "last-name"
        ).send_keys("User")

        driver.find_element(
            By.ID, "postal-code"
        ).send_keys("560001")

        # -------------------------------------------------
        # 10. Click Continue
        # -------------------------------------------------
        wait.until(
            EC.element_to_be_clickable(
                (By.ID, "continue")
            )
        ).click()

        # -------------------------------------------------
        # 11. NOW verify checkout step two
        # -------------------------------------------------
        wait.until(
            EC.url_contains("checkout-step-two")
        )

        assert "checkout-step-two" in driver.current_url

        # -------------------------------------------------
        # 12. Verify product is shown in checkout
        # -------------------------------------------------
        wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "cart_item")
            )
        )

        assert "Sauce Labs Backpack" in driver.page_source

        # -------------------------------------------------
        # 13. Verify Finish button
        # -------------------------------------------------
        finish_button = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "finish")
            )
        )

        assert finish_button.is_displayed()

        # -------------------------------------------------
        # 14. Finish checkout
        # -------------------------------------------------
        finish_button.click()

        # -------------------------------------------------
        # 15. Verify checkout complete
        # -------------------------------------------------
        wait.until(
            EC.url_contains("checkout-complete")
        )

        assert "checkout-complete" in driver.current_url

        assert "Thank you for your order" in driver.page_source

    finally:
        driver.quit()