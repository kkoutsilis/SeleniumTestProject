from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = ("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(PATH)

driver.get("https://github.com/")
print(driver.title)

search = driver.find_element_by_name("q")
search.send_keys("koutsilis1999")
search.send_keys(Keys.RETURN)
time.sleep(5)
driver.quit()