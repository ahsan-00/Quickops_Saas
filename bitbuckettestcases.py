from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

VALID_EMAIL = "sanjida.afrin@anwargroup.com"
VALID_PASSWORD = "Hello3963"
INVALID_EMAIL = "invaliduser@example.com"
INVALID_PASSWORD = "WrongPassword123"

def bitbucket_google_login(email, password):
    driver = webdriver.Chrome()
    driver.get("https://qa.quickops.io/auth/login")
    driver.maximize_window()

    try:
        bitbucket_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[contains(text(),'Continue with Bitbucket')])[1]"))
        )
        bitbucket_btn.click()
        print("Clicked 'Continue with Bitbucket'")
    except Exception as e:
        print("Failed to click Bitbucket button:", e)
        driver.quit()
        return False

    try:
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='username']"))
        )
        email_field.send_keys(email)
        continue_btn = driver.find_element(By.XPATH, "//span[normalize-space()='Continue']")
        continue_btn.click()
        print("Entered Bitbucket email and clicked Continue")
    except Exception as e:
        print("Error entering Bitbucket email:", e)
        driver.quit()
        return False

    
    try:
        google_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='css-178ag6o']"))
        )
        google_btn.click()
        print("Clicked 'Continue with Google'")
    except Exception as e:
        print("Failed to click 'Continue with Google':", e)
        driver.quit()
        return False

    time.sleep(3)
    windows = driver.window_handles
    driver.switch_to.window(windows[-1])

    try:
        email_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='identifierId']"))
        )
        email_input.send_keys(email)
        driver.find_element(By.XPATH, "//span[text()='Next']").click()
        print("Entered Google email")
    except Exception as e:
        print("Error entering Google email:", e)
        driver.quit()
        return False

    time.sleep(3)
    page_source = driver.page_source
    if "Couldn't find your Google Account" in page_source:
        print("Invalid Email Address Detected!")
        driver.quit()
        return False


    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.NAME, "Passwd"))
        )
        password_input = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.NAME, "Passwd"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", password_input)
        time.sleep(1)
        password_input.send_keys(password)
        driver.find_element(By.XPATH, "//span[text()='Next']").click()
        print("Entered Google password")
    except Exception as e:
        print("Error entering Google password:", e)
        driver.quit()
        return False

    time.sleep(3)
    page_source = driver.page_source
    if "Wrong password" in page_source:
        print("Invalid Password Detected!")
        driver.quit()
        return False


    try:
        WebDriverWait(driver, 20).until(
            EC.url_to_be("https://qa.quickops.io/dashboard")
        )
        
        current_url = driver.current_url
        if current_url == "https://qa.quickops.io/dashboard":
            print("Login successful! Reached dashboard.")
            driver.quit()
            return True
        else:
            print(f"Login possibly failed. Current URL: {current_url}")
            driver.quit()
            return False
    except Exception as e:
        print("Error verifying dashboard login:", e)
        driver.quit()
        return False

#  Test Cases 

print("\nTest Case 1: Login with Valid Email and Valid Password")
result = bitbucket_google_login(VALID_EMAIL, VALID_PASSWORD)
print("Test Result:", "Passed" if result else "Failed")

print("\nTest Case 2: Login with Invalid Email")
result = bitbucket_google_login(INVALID_EMAIL, VALID_PASSWORD)
print("Test Result:", "Passed" if not result else "Failed")

print("\nTest Case 3: Login with Invalid Password")
result = bitbucket_google_login(VALID_EMAIL, INVALID_PASSWORD)
print("Test Result:", "Passed" if not result else "Failed")
