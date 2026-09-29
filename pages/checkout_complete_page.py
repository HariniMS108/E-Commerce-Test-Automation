from selenium.webdriver.common.by import By


class CheckoutCompletePage:

    complete_message = (By.CLASS_NAME, "complete-header")
    back_home_button = (By.ID, "back-to-products")

    def __init__(self, driver):
        self.driver = driver

    def get_complete_message(self):
        return self.driver.find_element(*self.complete_message).text

    def click_back_home(self):
        self.driver.find_element(*self.back_home_button).click()