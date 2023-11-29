from selenium.webdriver.common.by import By

from six_pm_project.POM.library.assertions import assert_that
from six_pm_project.POM.library.helpers import Helpers


class SearchPage(Helpers):
    search_results_first_item_loc = (By.CSS_SELECTOR, '[alt="Handbags"]')
    title_of_search_result = (By.LINK_TEXT, 'Handbags')
    wallets_topic_loc = (By.CSS_SELECTOR, '[data-eventvalue="B-TOPCAT-Wallets-42020"]')
    wallets_search_result_first_item_heart_loc = (By.XPATH, '(//*[@data-test-id="heartButton"])[1]')
    favorites_general_loc = (By.LINK_TEXT, 'Favorites')

    def click_on_search_results_first_item(self):
        self.find_and_click(self.search_results_first_item_loc)

    def asserting_title_of_search_result(self):
        actual_result_handbags = self.find(self.title_of_search_result, get_text=True)
        expected_result_handbags = "Handbags"
        assert_that(actual_result_handbags, expected_result_handbags)

    def click_on_wallets_topic(self):
        self.find_and_click(self.wallets_topic_loc)

    def click_on_wallets_search_result_first_item_heart(self):
        self.find_and_click(self.wallets_search_result_first_item_heart_loc)

    def click_on_favorites_general(self):
        self.find_and_click(self.favorites_general_loc)