from selenium.webdriver.common.by import By

from six_pm_project.POM.library.helpers import Helpers


class SearchPage(Helpers):
    wallets_topic_loc = (By.CSS_SELECTOR, '[data-eventvalue="B-TOPCAT-Wallets-42020"]')
    wallets_search_result_first_item_heart_loc = (By.CSS_SELECTOR, '[class="gga-z kga-z lga-z"]')
    favorites_general_loc = (By.LINK_TEXT, 'Favorites')

    def click_on_wallets_topic(self):
        self.find_and_click(self.wallets_topic_loc)

    def click_on_wallets_search_result_first_item_heart(self):
        self.find_and_click(self.wallets_search_result_first_item_heart_loc)

    def click_on_favorites_general(self):
        self.find_and_click(self.favorites_general_loc)
