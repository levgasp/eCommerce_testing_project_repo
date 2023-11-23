from selenium.webdriver.common.by import By

from histories_project.POM.library.assertions import assert_that
from histories_project.POM.library.helpers import Helpers


class HowDidChristmasStart(Helpers):
    how_did_christmas_start_header_loc = (By.LINK_TEXT, 'How Did Christmas Start?')

    def how_did_christmas_start_header(self):
        actual_result = self.find(self.how_did_christmas_start_header_loc, get_text=True)
        expected_result = "How Did Christmas Start?"
        assert_that(actual_result, expected_result)