from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from utilities.waiter import wait_until


class AdminUserManagement:
    def __init__(self, driver):
        self._page = BasePage(driver)

    __loc_add_button = (By.XPATH, "(//button[contains(@class, 'oxd-button--secondary')])[2]")
    __loc_records = (By.XPATH, "//div[@class='orangehrm-container']")
    __loc_username_input = (By.XPATH, "(//input[contains(@class, 'oxd-input oxd-input--active')])[2]")
    __loc_help = (By.XPATH, "//*[contains(@title, 'Help')]")
    __loc_title = (By.XPATH, "//div[contains(@class, 'oxd-table-body')]")
    __loc_items = (By.XPATH, "//div[contains(@class, 'oxd-table-row oxd-table-row--with-border')]")

    def is_add_button_displayed(self):
        return self._page.is_displayed(self.__loc_add_button)

    def get_records_text(self):
        if wait_until(lambda: len(self._page.get_text(self.__loc_records)) > 0):
            return self._page.get_text(self.__loc_records)

    def count_records(self):
        return self._page.get_element_count(self.__loc_items)


