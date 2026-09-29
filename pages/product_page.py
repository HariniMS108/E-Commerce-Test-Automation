from selenium.webdriver.common.by import By


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack_to_cart(self):
        self.driver.find_element(*self.backpack).click()

    def click_cart(self):
        self.driver.find_element(*self.cart_icon).click()

    def get_products_title(self):
        return self.driver.find_element(
            By.CLASS_NAME,
            "title"
        ).text