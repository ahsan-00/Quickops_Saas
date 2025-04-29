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

def github_login(email, password):
    driver = webdriver.Chrome()
    driver.get("https://qa.quickops.io/auth/login")
    driver.maximize_window()

    try:
        github_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'])[3]"))
        )
        github_button.click()
        print("Clicked 'Continue with GitHub' button.")
    except Exception as e:
        print("Could not click the GitHub login button:", e)
        driver.quit()
        return False


    time.sleep(3)
    windows = driver.window_handles
    driver.switch_to.window(windows[-1])

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login_field"))
    ).send_keys(email)

    driver.find_element(By.ID, "password").send_keys(password)


    driver.find_element(By.NAME, "commit").click()


    time.sleep(3)
    page_source = driver.page_source
    if "Incorrect username or password." in page_source:
        print("Invalid Email or Password Detected!")
        driver.quit()
        return False

    
    time.sleep(5)
    driver.switch_to.window(windows[0])
    time.sleep(5)

    if "dashboard" in driver.current_url:
        print("Successfully logged in and reached Dashboard!")
        driver.quit()
        return True
    else:
        print("Login failed. Current URL:", driver.current_url)
        driver.quit()
        return False

#  Test Cases 

print("\nTest Case 1: Login with Valid Email and Valid Password")
result = github_login(VALID_EMAIL, VALID_PASSWORD)
print("Test Result:", "Passed" if result else "Failed")

print("\nTest Case 2: Login with Invalid Email")
result = github_login(INVALID_EMAIL, VALID_PASSWORD)
print("Test Result:", "Passed" if not result else "Failed")

print("\nTest Case 3: Login with Invalid Password")
result = github_login(VALID_EMAIL, INVALID_PASSWORD)
print("Test Result:", "Passed" if not result else "Failed")
#Sanjida Afrin
# 2023-10-05    
