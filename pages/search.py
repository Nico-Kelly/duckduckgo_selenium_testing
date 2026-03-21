"""
This module contains DuckDuckGoSearchPage, the page object for the DuckDuckGo search page.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base_page import BasePage

class DuckDuckGoSearchPage(BasePage):


    #URl

    URL = 'https://duckduckgo.com/'

    # Locators

    SEARCH_INPUT = (By.ID, 'searchbox_input')


    # Initializer | now the initializer is within base_page.py 


    # def __init__(self, browser):
    #   self.browser = browser

    #Interaction methods

    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        search_input = self.browser.wait_visibility(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)
