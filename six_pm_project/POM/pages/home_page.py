from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from six_pm_project.POM.library.helpers import Helpers


class HomePage(Helpers):
    def __init__(self, driver):
        super().__init__(driver)

    bugs_section_loc = (By.CSS_SELECTOR, '[href="/c/bags"]')
    search_field_loc = (By.CSS_SELECTOR, '[id="searchAll"]')
    accessories_section_loc = (By.CSS_SELECTOR, '[href="/accessories"]')

    def click_on_bugs_section(self):
        self.find_and_click(self.bugs_section_loc)

    def click_on_search_field_and_input_word(self):
        self.find_and_send_keys(self.search_field_loc, "bags")
        self.find_and_send_keys(self.search_field_loc, Keys.ENTER)

    def click_on_accessories_section(self):
        self.find_and_click(self.accessories_section_loc)


