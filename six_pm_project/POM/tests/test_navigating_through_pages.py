from six_pm_project.POM.tests.base_test import BaseTest


class TestNavigatingPages(BaseTest):
    def test_navigating_bags(self):
        self.pages_navigating()

    def test_searching(self):
        self.searching_navigating()

    def test_accessories(self):
        self.accessories_page_checking()