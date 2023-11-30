import time

import pytest


@pytest.mark.usefixtures("get_driver")
class BaseTest:
    def pages_navigating(self):
        self.homepage.click_on_bugs_section()
        self.bagspage.click_on_handbags()
        self.bagspage.asserting_filter_items()

    def searching_navigating(self):
        self.homepage.click_on_login_button()
        self.homepage.click_on_email_field_and_input_email()
        self.homepage.click_on_password_field_and_input_password()
        self.homepage.click_on_submit_btn()
        time.sleep(3)
        self.homepage.click_on_search_field_and_input_word()
        self.searchresultpage.click_on_wallets_topic()
        self.searchresultpage.click_on_wallets_search_result_first_item_heart()
        self.searchresultpage.click_on_favorites_general()
        self.favoritespage.assertion_title_of_favorites()
        self.favoritespage.click_on_added_item()
        self.favoritespage.click_on_particular_added_item()

    def accessories_page_checking(self):
        self.homepage.click_on_accessories_section()
        self.accessoriespage.click_on_hats_topic()
