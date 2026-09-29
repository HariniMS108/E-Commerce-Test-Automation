from selenium.webdriver.common.by import By


class CheckoutOverviewPage:

    finish_button = (By.ID, "finish")
    cancel_button = (By.ID, "cancel")

    def __init__(self, driver):
        self.driver = driver

    def click_finish(self):
        self.driver.find_element(*self.finish_button).click()

    def click_cancel(self):
        self.driver.find_element(*self.cancel_button).click()