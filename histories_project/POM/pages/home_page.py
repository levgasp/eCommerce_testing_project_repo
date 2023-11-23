from selenium.webdriver.common.by import By

from histories_project.POM.library.helpers import Helpers


class HomePage(Helpers):
    def __init__(self, driver):
        super().__init__(driver)

    how_did_christmas_start_loc = (By.CSS_SELECTOR, '[class="block-table-of-contents__link"]')
    saturnalia_and_christmas_loc = (By.LINK_TEXT, 'Saturnalia and Christmas ')

    def click_on_how_did_christmas_start(self):
        self.find_and_click(self.how_did_christmas_start_loc)

    def click_on_saturnalia_and_christmas(self):
        self.find_and_click(self.how_did_christmas_start_loc)

    def back_to_previous_page(self):
        self.driver.back()
