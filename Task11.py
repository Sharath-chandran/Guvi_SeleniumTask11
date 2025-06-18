# Load & Logon to Guvi site
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# Setting up ChromeDriver
driver = webdriver.Chrome()

# Loading the Guvi base site
driver.get("https://www.guvi.in/")
# To Maximize the browser window
driver.maximize_window()
print ("Site loaded successfully")
# wait (time in seconds) is added to load the webpage completely
time.sleep(2)

# Selecting the Login button in the base site
driver.find_element(By.XPATH, value ="//*[@id='login-btn']").click()

# Scroll is added inorder to view the input fields clearly
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(2)

# Locating the Username & Password fields to enter credentials
driver.find_element(By.XPATH, value= "//*[@id='email']").send_keys("sharathdfire@gmail.com")
driver.find_element(By.XPATH, value="//*[@id='password']").send_keys("4045D$harath")
time.sleep(2)
# Hitting the Login button
driver.find_element(By.XPATH, value="//*[@id='login-btn']").click()

# Landing in the Homepage and hitting the logout button
time.sleep(2)
driver.find_element(By.XPATH, value="//div[@id='dropdown_container']").click()
time.sleep(2)
driver.find_element(By.XPATH, value="(//li[@id='dropdown_contents'][4])").click()

# Close the browser
driver.quit()
