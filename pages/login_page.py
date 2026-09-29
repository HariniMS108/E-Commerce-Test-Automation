from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, "user-name").send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, "login-button").click()

    def get_error_message(self):
        return self.driver.find_element(
            By.CSS_SELECTOR,
            "[data-test='error']"
        ).text

    def click_logout(self):
        wait = WebDriverWait(self.driver, 10)

        # Click the menu button
        wait.until(
            EC.element_to_be_clickable(
                (By.ID, "react-burger-menu-btn")
            )
        ).click()

        # Click Logout
        wait.until(
            EC.element_to_be_clickable(
                (By.ID, "logout_sidebar_link")
            )
        ).click()