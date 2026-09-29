from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutInfoPage:

    def __init__(self, driver):
        self.driver = driver

        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.cancel_button = (By.ID, "cancel")

    def enter_first_name(self, first_name):
        self.driver.find_element(
            *self.first_name
        ).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(
            *self.last_name
        ).send_keys(last_name)

    def enter_postal_code(self, postal_code):
        self.driver.find_element(
            *self.postal_code
        ).send_keys(postal_code)

    def click_continue(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                self.continue_button
            )
        ).click()

    def click_cancel(self):
        self.driver.find_element(
            *self.cancel_button
        ).click()

    def enter_checkout_information(
        self, first_name, last_name, postal_code
    ):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
        self.click_continue()