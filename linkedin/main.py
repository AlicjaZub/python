from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3325349047&f_AL=true&f_E=2%2C4&f_JT=F&f_TPR=r604800&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&refresh=true&sortBy=R")

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD_LINKEDIN")

sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in.click()

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

username.send_keys(EMAIL)
password.send_keys(PASSWORD)

password.send_keys(Keys.ENTER)

time.sleep(2)

all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for listing in all_listings:
    listing.click()
    time.sleep(2)

    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)
        
        #If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
        if submit_button.get_attribute("aria-label") == "Continue to next step":
            close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
          print("SUBMITTED")
            # submit_button.click()
    
        time.sleep(2)
        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()

    #If already applied to job or job is no longer accepting applications, then skip.
    except:
        print("No application button, skipped.")
        continue
driver.quit()