import time
import pyautogui # type: ignore
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome setup
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)  # Keeps the browser open for debugging if crash happens

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 30)

try:
    # Step 1: Go to Gmail
    driver.get("https://mail.google.com/")
    print(" Opening Gmail login...")

    # Step 2: Enter Email
    wait.until(EC.presence_of_element_located((By.ID, "identifierId"))).send_keys("sanjida.afrin@anwargroup.com" + Keys.ENTER)
    print(" Email entered.")

    # Step 3: Enter Password
    password_input = wait.until(EC.presence_of_element_located((By.NAME, "Passwd")))
    password_input.send_keys("Hello3963" + Keys.ENTER)
    print(" Password entered.")

    # Step 4: Wait for Inbox to Load
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Compose']")))
    print(" Logged in and inbox loaded.")

    time.sleep(5)  # wait for the prompt to appear

    try:
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')
        pyautogui.press('tab')
        pyautogui.press('enter')
        print(" Simulated keyboard input.")
    except Exception as e:
        print("Failed to simulate keyboard input:", e)

    # Step 4.1: Check for "Google permission popup" prompt
    # try:
    #     gpopup_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Allow')]")))
    #     gpopup_btn.click()
    #     print(" 'Allow' button clicked.")
    # except:
    #     print("ℹ 'Allow' button not shown, continuing...")

    # Step 5: Click "No thanks" if it appears
    try:
        no_thanks_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='No thanks'])[1]")))
        no_thanks_btn.click()
        print(" 'No thanks' clicked.")
    except:
        print("ℹ 'No thanks' not shown, continuing...")

    # Step 6: Open Spam Folder
    print(" Clicking 'More' to find Spam folder...")
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='More']"))).click()

    print(" Clicking on Spam folder...")
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '#spam')]"))).click()

    # Step 7: Wait for Spam Folder to Load
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Spam']")))
    print(" Spam folder opened.")
    time.sleep(4)  # Let emails render properly

    # Step 8: Search for the Mail
    print(" Searching for mail by subject...")
    search_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search mail']")))
    search_box.clear()
    search_box.send_keys('subject:"Verify your Email address for QuickOps account" in:spam' + Keys.ENTER)

    # Step 9: Wait for Email Result and Open
    print(" Waiting for email to appear...")
    try:
        email_subject = wait.until(EC.element_to_be_clickable((By.XPATH, "//span/b[contains(text(),'Verify your Email address for QuickOps account')]")))
        email_subject.click()
        print(" Email opened successfully.")
    except Exception as e:
        print(" Email not found or failed to open:", e)

    time.sleep(10)

except Exception as e:
    print(" General Error:", e)

finally:
    driver.quit()