import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Declaring the Login URL
LOGIN_URL = "https://www.guvi.in/sign-in/"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_invalid_login(driver):
    driver.get(LOGIN_URL)
    driver.maximize_window()

    # Locating the Username & Password fields to enter credentials
    driver.find_element(By.XPATH, value="//*[@id='email']").send_keys("Test@123.com")
    driver.find_element(By.XPATH, value="//*[@id='password']").send_keys("Demo@123")
    time.sleep(3)

    # Hitting the Login button
    driver.find_element(By.XPATH, value="//*[@id='login-btn']").click()
    time.sleep(3)

    # Locating the error message element and extracting the error content
    error = driver.find_element(By.XPATH, value=("//*[@id='emailgroup']/div")).text
    print("Error message: ", error)

    assert "Incorrect Email or Password" == error, "Invalid login attempt"