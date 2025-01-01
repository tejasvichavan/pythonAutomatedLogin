from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Function to test login
def test_login():
    url = "https://www.saucedemo.com/"
    username = "testuser"
    password = "password123"

    service = Service('path/to/chromedriver')
    driver = webdriver.Chrome(service=service)

    try:
        driver.get(url)
        print("Navigated to the login page.")
        wait = WebDriverWait(driver, 10)
        username_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='user-name']")))
        password_field = driver.find_element(By.XPATH, "//*[@id='password']")
        login_button = driver.find_element(By.XPATH, "//*[@id='login-button']")
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()
        print("Login form submitted.")
        try:
            wait.until(EC.presence_of_element_located((By.ID, "homepage-indicator")))
            print("Login successful! Redirected to homepage.")
        except TimeoutException:
            error_message = wait.until(EC.presence_of_element_located((By.ID, "error-message")))
            print(f"Login failed. Error message: {error_message.text}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        time.sleep(5)
        driver.quit()
if __name__ == "__main__":
    test_login()
