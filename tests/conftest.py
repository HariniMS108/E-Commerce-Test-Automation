import pytest
from selenium import webdriver
from pathlib import Path


@pytest.fixture
def driver():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")

    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:
            screenshot_dir = Path("screenshots")
            screenshot_dir.mkdir(exist_ok=True)

            screenshot_path = screenshot_dir / f"{item.name}.png"

            driver.save_screenshot(str(screenshot_path))

            print(f"\nScreenshot saved: {screenshot_path}")