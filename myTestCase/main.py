import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        PATH = ("C:\Program Files (x86)\chromedriver.exe")
        self.driver = webdriver.Chrome(PATH)
        self.driver.get("http://www.python.org")
    

    def test_title_in_python_org(self):
        assert "Python" in self.driver.title

    def test_search_in_python_org(self):       
        search =  WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.NAME,"q"))
        )
        search.send_keys("pycon")
        go_button = self.driver.find_element_by_id("submit")
        go_button.click()
        assert "No results found." not in self.driver.page_source
    
    def test_donate_in_python_org(self):       
        donate =  WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME,"donate-button"))
        )
        donate.click()
        assert "Donation for the PSF" in self.driver.page_source

    def test_windows_downloads_in_python_org(self):
        downloads = ActionChains(self.driver)
        downloads.move_to_element(self.driver.find_element_by_id("downloads"))
        windows = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT,"Windows"))
        )
        windows.click()
        assert "Python Releases for Windows" in self.driver.page_source
    
    def test_jobs_in_python(self):
        self.driver.find_element_by_link_text("Jobs").click()
        assert "Python Job Board" in self.driver.page_source

    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()