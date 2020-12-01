from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = ("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(PATH)

driver.get("http://ict.ihu.gr/")

link = driver.find_element_by_link_text("Νέο πρόγραμμα σπουδών 5ετούς διάρκειας")
link.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT,"Ανακοινώσεις"))
    )
    element.click()

    element2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT,"ΠΑΙΔΑΓΩΓΙΚΑ"))
    )
    element2.click()

    driver.back()
    driver.back()
    driver.back()
except:
    driver.quit()

time.sleep()
driver.quit()

