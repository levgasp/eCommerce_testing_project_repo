from selenium.webdriver.common.by import By

from six_pm_project.POM.library.assertions import assert_that
from six_pm_project.POM.library.helpers import Helpers


class BagsPage(Helpers):
    handbags_loc = (By.CSS_SELECTOR, '[data-eventvalue="B-TOPCAT-Handbags-42020"]')
    filter_bags_loc = (By.LINK_TEXT, 'Bags')
    filter_handbags_loc = (By.LINK_TEXT, 'Handbags')

    def click_on_handbags(self):
        self.find_and_click(self.handbags_loc)

    def asserting_filter_items(self):
        actual_result_bags = self.find(self.filter_bags_loc, get_text=True)
        expected_result_bags = "Bags"
        assert_that(actual_result_bags, expected_result_bags)
        actual_result_handbags = self.find(self.filter_handbags_loc, get_text=True)
        expected_result_handbags = "Handbags"
        assert_that(actual_result_handbags, expected_result_handbags)
