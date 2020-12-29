from locator import *
from element import BasePageElement

class SearchTextElement(BasePageElement):
   
    #The locator for search box where search string is entered
    locator = "q"

class BasePage(object):
    def __init__(self,driver):
        self.driver = driver

class MainPage(BasePage):

    search_text_element = SearchTextElement() 

    def is_title_matches(self):
        return "Python" in self.driver.title

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

class SearchResultPage(BasePage):

    def is_results_found(self):
        return "No results found." not in self.driver.page_source