"""
This module contains DuckDuckGoResultPage, the page object for the DuckDuckGo result page.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_page import BasePage
class DuckDuckGoResultPage(BasePage):


    #Locators
    
    RESULT_LINKS = (By.CSS_SELECTOR, '[data-testid="result-title-a"] span')
    SEARCH_INPUT = (By.ID,'search_form_input')

    #Initializer

    def __init__(self, browser):
        self.browser = browser

    #Interaction Methods

    def result_link_titles(self):
    
        #wait = WebDriverWait(self.browser, 10) deprecated this

        links = self.wait_multiple_visibility(self.RESULT_LINKS)

        titles = [link.text for link in links]

        return titles


    def search_input_value(self):
        search_input = self.wait_visibility(self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value
    
    
    def title(self):
        return self.browser.title
    
