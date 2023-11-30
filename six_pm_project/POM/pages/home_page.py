from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from six_pm_project.POM.library.helpers import Helpers


class HomePage(Helpers):
    def __init__(self, driver):
        super().__init__(driver)

    login_button_loc = (By.CSS_SELECTOR, '[class="qa-z"]')
    email_field_loc = (By.CSS_SELECTOR, '[name="email"]')
    password_field_loc = (By.CSS_SELECTOR, '[name="password"]')
    submit_btn_loc = (By.CSS_SELECTOR, '[id="signInSubmit"]')

    bugs_section_loc = (By.CSS_SELECTOR, '[href="/c/bags"]')

    search_field_loc = (By.CSS_SELECTOR, '[id="searchAll"]')
    search_btn_loc = (By.LINK_TEXT, 'Submit Search')

    accessories_section_loc = (By.CSS_SELECTOR, '[href="/accessories"]')

    def click_on_login_button(self):
        self.find_and_click(self.login_button_loc)

    def click_on_email_field_and_input_email(self):
        self.find_and_send_keys(self.email_field_loc, "gasparyan.levon177@gmail.com")

    def click_on_password_field_and_input_password(self):
        self.find_and_send_keys(self.password_field_loc, "12chuchundrA")

    def click_on_submit_btn(self):
        self.find_and_click(self.submit_btn_loc)

    def click_on_bugs_section(self):
        self.find_and_click(self.bugs_section_loc)

    def click_on_search_field_and_input_word(self):
        self.find_and_send_keys(self.search_field_loc, "bags")
        self.find_and_send_keys(self.search_field_loc, Keys.ENTER)

    def click_on_accessories_section(self):
        self.find_and_click(self.accessories_section_loc)
