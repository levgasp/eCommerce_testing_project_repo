import pytest


@pytest.mark.usefixtures("get_driver")
class BaseTest:
    def navigate_through_pages_and_perform_actions(self):
        self.homepage.click_on_how_did_christmas_start()
        self.howdidchristmasstartpage.how_did_christmas_start_header()
        self.homepage.back_to_previous_page()
        self.saturnaliaandchristmas.click_on_saturnalia_and_christmas()