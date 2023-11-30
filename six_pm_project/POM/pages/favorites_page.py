from selenium.webdriver.common.by import By

from six_pm_project.POM.library.assertions import assert_that
from six_pm_project.POM.library.helpers import Helpers


class FavoritesPage(Helpers):
    title_of_favorites_loc = (By.LINK_TEXT, 'Favorites')
    added_item_loc = (By.CSS_SELECTOR, '[class="Y5-z"]')
    particular_added_item_loc = (By.CSS_SELECTOR, '[src="https://m.media-amazon.com/images/I/71QkS0bwurL._AC_SX400_.'
                                                  'jpg"]')
    selected_item_title_loc = (By.LINK_TEXT, 'Juicy Couture Cool Collar Bifold')

    def assertion_title_of_favorites(self):
        actual_result_favorites_title = self.find(self.title_of_favorites_loc, get_text=True)
        expected_result_favorites_title = "Favorites"
        assert_that(actual_result_favorites_title, expected_result_favorites_title)

    def click_on_added_item(self):
        self.find_and_click(self.added_item_loc)

    def click_on_particular_added_item(self):
        self.find_and_click(self.particular_added_item_loc)

    def assertion_selected_item_title(self):
        actual_result_wallet_title = self.find(self.selected_item_title_loc, get_text=True)
        expected_result_wallet_title = "Juicy Couture Cool Collar Bifold"
        assert_that(actual_result_wallet_title, expected_result_wallet_title)