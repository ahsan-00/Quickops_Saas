from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Test Data
VALID_EMAIL = "sanjida.afrin@anwargroup.com"
VALID_PASSWORD = "Hello3963"
INVALID_EMAIL = "invaliduser@example.com"
INVALID_PASSWORD = "WrongPassword123"

def google_login(email, password):
    driver = webdriver.Chrome()
    driver.get("https://qa.quickops.io/auth/login")
    driver.maximize_window()

    try:
        google_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Continue with Google')]"))
        )
        google_button.click()
        print("Clicked 'Continue with Google' button.")
    except Exception as e:
        print("Could not click the Google login button:", e)
        driver.quit()
        return False

   
    time.sleep(3)
    windows = driver.window_handles
    driver.switch_to.window(windows[-1])


    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "identifierId"))
    ).send_keys(email)
    driver.find_element(By.XPATH, "//span[text()='Next']").click()

    time.sleep(3)
    page_source = driver.page_source
    if "Couldn't find your Google Account" in page_source:
        print("Invalid Email Address Detected!")
        driver.quit()
        return False


    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "Passwd"))
        ).send_keys(password)
        driver.find_element(By.XPATH, "//span[text()='Next']").click()
    except Exception as e:
        print("Password field not found. Possible invalid email flow.")
        driver.quit()
        return False


    time.sleep(3)
    page_source = driver.page_source
    if "Wrong password" in page_source:
        print("Invalid Password Detected!")
        driver.quit()
        return False

  
    time.sleep(10)
    driver.switch_to.window(windows[0])
    time.sleep(5)


    if driver.current_url == "https://qa.quickops.io/dashboard":
        print("Successfully logged in and reached Dashboard!")
        driver.quit()
        return True
    else:
        print("Login failed. Current URL:", driver.current_url)
        driver.quit()
        return False

# Test Cases 

print("\n Test Case 1: Login with Valid Email and Valid Password ")
result = google_login(VALID_EMAIL, VALID_PASSWORD)
print("Test Result:", "Passed" if result else "Failed")

print("\n Test Case 2: Login with Invalid Email ")
result = google_login(INVALID_EMAIL, VALID_PASSWORD)
print("Test Result:", "Passed" if not result else "Failed")

print("\n Test Case 3: Login with Invalid Password ")
result = google_login(VALID_EMAIL, INVALID_PASSWORD)
print("Test Result:", "Passed" if not result else "Failed")
