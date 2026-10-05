# E-Commerce Test Automation

Automated testing project for an e-commerce application using Python, Selenium WebDriver, and Pytest.

## Application Under Test

The automation tests are performed on the **SauceDemo** e-commerce website.

**Website:** https://www.saucedemo.com/

## Project Description

This project is an E-Commerce Test Automation framework developed to automate important user functionalities of an e-commerce application.

The project uses Selenium WebDriver to interact with the web application and Pytest to execute and manage the test cases.

The framework follows the **Page Object Model (POM)** design pattern to keep the automation code organized, reusable, and maintainable.

## Technologies Used

- Python
- Selenium WebDriver
- Pytest
- Pytest-HTML
- Page Object Model (POM)
- Database Testing
- Git
- GitHub

## Functionalities Tested

The following important e-commerce functionalities are automated:

### Login Testing
- Valid login
- Invalid username
- Invalid password
- Login validation

### Logout Testing
- Successful logout

### Product Testing
- Product availability
- Product selection

### Shopping Cart Testing
- Add product to cart
- Verify product in cart
- Remove product from cart
- Continue shopping

### Checkout Testing
- Checkout functionality
- Checkout flow validation

### Database Testing
- Product/data validation using database testing

## Test Scenarios

The project covers positive and negative test scenarios.

### Positive Test Scenarios

- Login with valid credentials
- Add a product to the shopping cart
- Verify product in the cart
- Proceed to checkout
- Logout successfully

### Negative Test Scenarios

- Login with invalid username
- Login with invalid password
- Validate unsuccessful login behavior
- Validate invalid application actions

## Project Structure

```text
E-Commerce-Test-Automation/
│
├── pages/
│   ├── login_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   └── ...
│
├── tests/
│   ├── test_login.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_logout.py
│   └── ...
│
├── utils/
│   └── ...
│
├── screenshots/
│
├── README.md
├── requirements.txt
├── conftest.py
├── pytest.ini
└── test_report.html
│
├── screenshots/
├── html-reports/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md