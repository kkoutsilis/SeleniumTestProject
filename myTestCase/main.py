import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        PATH = ("C:\Program Files (x86)\chromedriver.exe")
        self.driver = webdriver.Chrome(PATH)
        self.driver.get("http://www.python.org")

    def test_search_in_python_org(self):
        assert "Python" in self.driver.title
        search =  WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.NAME,"q"))
        )
        search.send_keys("pycon")
        go_button = self.driver.find_element_by_id("submit")
        go_button.click()
        assert "No results found." not in self.driver.page_source
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()