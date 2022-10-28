from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

CODE = "Mi4wNDh8fDE2NjU2NTQ0NTcyMDI7MTY2NTY1NDQ1NzIwMjsxNjY2OTUzMDExNTUzO0RlbGljaW91cyBDbGljaztkc21pbnwxMTExMTEwMTEwMDEwMTEwMDEwMTAxMTAwMDF8MjYwNTQ5MDM2OTMyMTk2ODA7NDI0MTgyNTE1NDg0MDg2NTMwMDs1NTI0MjYzOzg4MjsyOTQ4OTI3ODkxNzI0MDEzNjAwOzYyNTswOzA7MDszOzI7MDswOy0xOzA7ODgyOzQzOTYzMzQ2ODEwODU1MTIwOzExNzswOzA7MDswO2hhbGxvd2VlbjswOzA7MDswOzA7MDswOy0xOy0xOy0xOy0xOy0xOzA7MDswOzA7MDswOzA7MDsxNTsxNjY2OTQ0NTE1MzQ5OzA7MDs7NDE7MDswOzE4NjA3MjYxNDM0NTExLjIwNzs1MDt8MjAwLDIwMSwxMjE0MTA0ODQyOTA1NjM4LDEsLDAsMjAwOzIwMCwyMDQsNDE3NTc2MDQ4NzgyNzgzOSwxLCwxLDIwMDsyMDAsMjEwLDExNDg3MDg3NjE2NDUsMiwxNjY2OTUzMjY5ODUzOjI6MTY2NjcwNjI1ODUyMTowOjE5OjE5OjE6MDoxNjY2Njg1MzIzMzI4OiAxMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwIDA6MDowOjA6MDowOjA6MDowOjA6MDowOjA6MDowOjA6MDowOjA6MDowOjA6MDowOjA6MDowOjA6MTozNDoxOjMxOjE6MDowOjA6MDowOjA6MDoxOjMxOjE6MzI6MTowOjA6MDowOjA6MDowOjA6MDowOjA6MDowOjA6MDowOjA6MDowOjA6MDowOjA6MDowOjA6MDosMCwyMDA7MjAwLDIwMywxNTcyMDcyMjc2NjgyLDAsLDEsMjAwOzE1NSwxNTcsNjcxNzI1OTg0MjczOCwxLCwxLDE1NTsxNTUsMTU2LDMzNDA0Nzg2NzgyNjQ0LDAsLDEsMTU1OzE1MCwxNTAsMTE0ODc2NTQyMTgzMDg3LDEsLTEvLTEvLTEgMyAxNjY1ODI4Mzc4NzIxIDEsMSwxNTA7MTI0LDEyNCw0NDI3OTE0NDQwMjE2MDEsMSw1NSAyIDIgMSwxLDEyNDsxMDYsMTA2LDE1MzkxMzQ0MDQ0MjgxMDMsMSwsMSwxMDY7ODcsODcsNDYyMzk0NjQ1NDE0MDg2MSwxLCwxLDg3OzY5LDY5LDE3ODYxODM4NDY0NTc1NTE2LDEsLDEsNjk7NTUsNTUsNDY5NzAyOTk4NzQ2NTExNzAsMSwsMSw1NTs0Miw0MiwxMzIzMjI1MTAzMDU1MzYyNzAsMSwsMSw0MjsyNSwyNSwxNzI3NjA2MjcwNDQ4NzY1ODAsMSwsMSwyNTsxMCwxMCwxODA2NTQzMDk3MzgzMTIyNjAsMSwsMSwxMDsxLDEsMzk2NTEyNjg1MzY3MDQ3NjAsMCwsMSwxOzAsMCwwLDAsLDAsMDswLDAsMCwwLCwwLDA7MCwwLDAsMCwsMCwwO3wxMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMDExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTAxMTExMTExMTAwMTExMTAwMDAxMDExMTEwMDExMTExMTAwMTEwMDAwMDAwMDAwMDAxMTExMTEwMDExMTExMTExMTExMTAwMTExMTExMTExMTAwMDAwMDAwMTEwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMTExMTAwMTExMTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMTExMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDExMTExMDAwMDAxMTAwMDAwMDAwMDAwMDEwMDAwMDExMTExMTExMTExMTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTEwMDExMTExMTAwMDAwMDExMTExMTEwMTAxMDEwMTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMTExMTEwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMTExMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDExMTExMTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDExMTEwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDB8MTExMTExMTExMTExMDAwMDExMTExMTExMTEwMDAwMTExMTExMTExMTExMTExMTExMTExMTExMTExMDExMDExMDAwMDExMTAxMTExMTAxMDEwMTExMTAwMTAwMTAwMDAwMDAwMDExMTAwMTEwMDAwMDAwMDExMTAwMDAwMTAwMDAwMDAwMDEwMDAwMDAwMDAwMDExMDAwMTAxMDAwMDAwMDAwMDAwMDAwMDAwMTExMTAxMTExMDExMTAwMDAwMDAwMDAwMDAwMDAwMDAwMTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMTEwMDAwMDAwMDAwMTEwMDAwMDAwMDAwMDAwMDAwMDAxMTAxMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDEwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMHwwLDQ2MjAsNzk2LDc7fA%3D%3D%21END%21"

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
    elif cookies_info[1] == "trillion":
      cookies_count = float(cookies_info[0]) * 10**12
    elif cookies_info[1] == "quadrillion":
      cookies_count = float(cookies_info[0]) * 10**15
    elif cookies_info[1] == "quintillion":
      cookies_count = float(cookies_info[0]) * 10**18
      
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
        elif product_info[1] == "quadrillion":
          product_price = float(product_info[0]) * 10**15
        elif product_info[1] == "quintillion":
          product_price = float(product_info[0]) * 10**18
        elif product_info[1] == "sextillion":
          product_price = float(product_info[0]) * 10**21
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
      try:
        driver.find_element(By.CLASS_NAME, "shimmer").click()
      except:
        pass
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
    consent = driver.find_element(By.LINK_TEXT, "Got it!")
    consent.click()
    click_cookie()
    
    
    # <div class="shimmer" alt="Golden cookie" style="left: 177px; top: 296px; width: 96px; height: 96px; background-image: url(&quot;img/goldCookie.png&quot;); background-position: 0px 0px; opacity: 0.881127; display: block; transform: rotate(18.8344deg) scale(0.960475);"></div>