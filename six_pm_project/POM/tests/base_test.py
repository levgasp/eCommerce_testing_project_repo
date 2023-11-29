import pytest


@pytest.mark.usefixtures("get_driver")
class BaseTest:
    def pages_navigating(self):
        self.homepage.click_on_bugs_section()
        self.bagspage.click_on_handbags()
        self.bagspage.asserting_filter_items()
        self.favoritespage.assertion_title_of_favorites()

