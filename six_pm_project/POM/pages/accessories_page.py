from selenium.webdriver.common.by import By

from six_pm_project.POM.library.helpers import Helpers


class AccessoriesPage(Helpers):
    hats_topic_loc = (By.CSS_SELECTOR, '[data-eventvalue="A-TOPCAT-WomensHats"]')

    def click_on_hats_topic(self):
        self.find_and_click(self.hats_topic_loc)