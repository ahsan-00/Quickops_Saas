#open gmail and search verification mail .it is used for local signup and forget password functionality
import time
import pyautogui  #ignore korar jnno popup message
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)  

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 30)

try:
    #  Open Gmail
    driver.get("https://mail.google.com/")
    print("📨 Opening Gmail...")

    #  Login
    wait.until(EC.presence_of_element_located((By.ID, "identifierId"))).send_keys("sanjida.afrin@anwargroup.com", Keys.ENTER)
    print("✅ Email entered.")

    wait.until(EC.presence_of_element_located((By.NAME, "Passwd"))).send_keys("Hello3963", Keys.ENTER)
    print("✅ Password entered.")


    wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Compose']")))
    print("📥 Inbox loaded.")

    
    time.sleep(5)
    try:
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')
        pyautogui.press('tab')
        pyautogui.press('enter')
        print("🧩 Simulated keyboard input.")
    except Exception as e:
        print("⚠️ Keyboard input failed:", e)

    try:
        no_thanks_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='No thanks']")))
        no_thanks_btn.click()
        print("🛑 'No thanks' clicked.")
    except:
        print("✅ 'No thanks' button not shown.")

    #  Open Spam folder
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='More']"))).click()
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '#spam')]"))).click()
    print("📁 Spam folder opened.")
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Spam')]")))

    # Search  Spam
    search_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search mail']")))
    search_box.clear()
    search_box.send_keys('subject:"Verify your Email address for QuickOps account" in:spam', Keys.ENTER)
    print("🔍 Search executed.")

    # Open the email
    try:
        print("📨 Looking for the email...")
        email_subject = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span/b[contains(text(),'Verify your Email address for QuickOps account')]")
        ))
        email_subject.click()
    except:
        try:
            email_subject = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//span[contains(text(),'Verify your Email address for QuickOps account')]")
            ))
            email_subject.click()
        except Exception as e:
            print("❌ Email not found or click failed:", e)
            raise

    print("✅ Email opened.")

    #  Click the verification link
    try:
        print("🔗 Looking for the verification link...")
        verification_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'quickops')]")))
        verification_link.click()
        print("✅ Verification link clicked.")
    except Exception as e:
        print("❌ Could not find or click the verification link:", e)
        raise

finally:
   
    driver.quit()


