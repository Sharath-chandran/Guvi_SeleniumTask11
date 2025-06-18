import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Declaring the base URL / Login URL in a variable
Guvi_base_URL = "https://www.guvi.in/"
Login_button_URL = "https://www.guvi.in/sign-in/"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Loading Guvi site and navigating to Login button
# Assert validates the current URL with expected Login button URL
def test_loginbutton_url(driver):
    driver.get(Guvi_base_URL)
    # To Maximize the browser window
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.XPATH, value="//*[@id='login-btn']").click()
    assert driver.current_url == Login_button_URL, "Login button URL mismatch"
    print ("Current URL: ", driver.current_url)

# Loading Guvi login site
# Assert validates the Username/Password fields
def test_input_fields(driver):
    driver.get(Login_button_URL)
    driver.maximize_window()
    username = driver.find_element(By.XPATH, value="//*[@id='email']")
    password = driver.find_element(By.XPATH, value="//*[@id='password']")
    assert username.is_displayed() and username.is_enabled(), "Username field is not enabled & accessible"
    assert password.is_displayed() and password.is_enabled(), "Password field is not enabled & accessible"
    print ("Validated the input fields successfully")

# Loading Guvi login site and validating the Login button
# Assert validate the logon button is displayed and enabled
def test_submit_button(driver):
    driver.get(Login_button_URL)
    driver.maximize_window()
    submit = driver.find_element(By.XPATH, "//*[@id='login-btn']")
    assert submit.is_displayed() and submit.is_enabled(), "Login button is not working"
    print ("Validated the Logon button successfully")




