from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

CODE = "Mi4wNDh8fDE2NjU2NTQ0NTcyMDI7MTY2NTY1NDQ1NzIwMjsxNjY1Njc2OTQ3MDA2O0RlbGljaW91cyBDbGljaztkc21pbnwxMTExMTEwMTEwMDEwMTEwMDEwMTAxMTAwMDF8NDI2NDc3MDQzLjMzMzkxNTU7Njg0NTA5NDQ0OC4zMzk3ODE7Nzg4NTQ7OTsxNTM5MTU5MTg5LjI1MzM5NTsyMzswOzA7MDswOzA7MDswOzA7MDs5OzA7MDswOzA7MDswOzswOzA7MDswOzA7MDswOy0xOy0xOy0xOy0xOy0xOzA7MDswOzA7NzU7MDswOzA7MDsxNjY1NjY2Njk1Njk1OzA7MDs7NDE7MDswOzEzMTkzOTQuOTUwODk4NTAwNDs1MDt8MTAwLDEwMSwzNjgzMDg2NzcsMCwsMCwxMDA7OTAsOTAsMTcwODYxMzQ5LDAsLDEsOTA7ODAsODAsMTQ3MjA3MDEyLDAsLDEsODA7NjAsNjAsMzYwNDAyNTAxLDAsLDEsNjA7NDAsNDAsMTAwNjQ2NTY5MCwwLCwxLDQwOzMwLDMwLDEzNDM0MTE0NzQsMCwsMCwzMDsxNSwxNSwxMzE0MDM0MDc5LDAsLDAsMTU7NCw0LDU4NzA4MzQ0NywwLCwwLDQ7MCwwLDAsMCwsMCwwOzAsMCwwLDAsLDAsMDswLDAsMCwwLCwwLDA7MCwwLDAsMCwsMCwwOzAsMCwwLDAsLDAsMDswLDAsMCwwLCwwLDA7MCwwLDAsMCwsMCwwOzAsMCwwLDAsLDAsMDswLDAsMCwwLCwwLDA7MCwwLDAsMCwsMCwwOzAsMCwwLDAsLDAsMDt8MTExMTExMTExMTExMDAxMTExMTExMTExMTExMTExMTExMTExMTEwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMTEwMTExMTExMTExMTExMTExMDEwMTAwMDExMTEwMDEwMDAwMDAwMDAxMDAwMDAxMDEwMTExMTExMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMTExMTEwMTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMTExMTAwMDAwMDAxMTEwMDAwMDAwMDAxMDAwMDAwMDAwMDAxMTEwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMTExMTEwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMTEwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwfDExMTExMTAwMDAwMDAwMDAxMTExMTEwMDAwMDAwMDExMTExMTExMDAxMTAxMTAxMDAxMTAwMDAwMDAwMDAwMDAwMDAxMTAwMTEwMTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDEwMDAwMTAwMDAxMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDB8fA%3D%3D%21END%21"

timeout_product = time.time() + 60 * 3
timeout_upgrade = time.time() + 60 * 5

def buy_product():
  print("BUY PRODUCTS")
  cookies = driver.find_element(By.ID, "cookies")
  cookies_info = cookies.text.split()

  if "." in cookies_info[0]:
    if cookies_info[1] == "million":
      cookies_count = float(cookies_info[0]) * 10**6
    elif cookies_info[1] == "billion":
      cookies_count = float(cookies_info[0]) * 10**9
      
  else:
    cookies_count = int(''.join(cookies_info[0].split(",")))
  
  products = driver.find_elements(By.CLASS_NAME, "product")
  products = products[::-1]
  for p in products:
    classes = p.get_attribute("class")
    if not "toggledOff" in classes:
      id = p.get_attribute("id")
      price = driver.find_element(By.CSS_SELECTOR, f"#{id} .price")
      product_info = price.text.split()
      try: 
        if product_info[1] == "million":
          product_price = float(product_info[0]) * 10**6
        elif product_info[1] == "billion":
          product_price = float(product_info[0]) * 10**9
        elif product_info[1] == "trillion":
          product_price = float(product_info[0]) * 10**12
      except IndexError:
        product_price = int(''.join(product_info[0].split(",")))
      
      if cookies_count >= product_price:
        print(p.text)
        p.click()
        return
      
def buy_upgrade():
  print("BUY UPGRADES")
  try:
    upgrade = driver.find_element(By.ID, "upgrade0")
    upgrade.click()
    return
  except:
    return


def click_cookie():
  global timeout_product, timeout_upgrade
  WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, "bigCookie"))
  )

  try:
    cookie = driver.find_element(By.ID, "bigCookie")
  except:
    cookie = driver.find_element(By.ID, "bigCookie")
  finally:
    while True:
      cookie.click()
      if time.time() > timeout_upgrade:
        timeout_upgrade = time.time() + 60 * 5
        buy_upgrade()
        time.sleep(90)
        
      elif time.time() > timeout_product:
        timeout_product = time.time() + 60 * 3
        buy_product()



driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.get("https://orteil.dashnet.org/cookieclicker/")


WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "langSelect-EN"))
    )

language = driver.find_element(By.ID, "langSelect-EN")
language.click()

if CODE == '':
  click_cookie()
else:
  try:
    options_button = driver.find_element(By.CSS_SELECTOR, "#prefsButton .subButton")
    options_button.click()
  except:
    options_button = driver.find_element(By.CSS_SELECTOR, "#prefsButton .subButton")
    options_button.click()
    
    import_button = driver.find_element(By.LINK_TEXT, "Import save")
    import_button.click()
    

    text_area = driver.find_element(By.ID, "textareaPrompt")
    text_area.send_keys(CODE)
    text_area.send_keys(Keys.ENTER)
    close_button = driver.find_element(By.CLASS_NAME, "menuClose")

    close_button.click()
  finally:
    click_cookie()