from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(article_count.text)
# article_count.click()

# encyclopedia = driver.find_element(By.LINK_TEXT, "encyclopedia")
# encyclopedia.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
driver.quit()


# driver.get("http://secure-retreat-92358.herokuapp.com/")

# fname = driver.find_element(By.NAME, "fName")
# fname.send_keys("Alicja")
# lname = driver.find_element(By.NAME, "lName")
# lname.send_keys("Zubel")
# email = driver.find_element(By.NAME, "email")
# email.send_keys("m@mail.com")
# email.send_keys(Keys.ENTER)
