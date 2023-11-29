import pytest


@pytest.mark.usefixtures("get_driver")
class BaseTest:
    def pages_navigating(self):
        self.homepage.click_on_bugs_section()
        self.bagspage.click_on_handbags()
        self.bagspage.asserting_filter_items()

    def searching_navigating(self):
        self.homepage.click_on_search_field_and_input_word()
        self.searchresultpage.click_on_wallets_topic()
        self.searchresultpage.click_on_wallets_search_result_first_item_heart()
        self.searchresultpage.click_on_favorites_general()

    def accessories_page_checking(self):
        self.homepage.click_on_accessories_section()
        self.accessoriespage.click_on_hats_topic()
