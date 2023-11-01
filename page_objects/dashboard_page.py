from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from page_objects.admin_user_management import AdminUserManagement
from page_objects.my_info_page import MyInfoPage


class DashboardPage:
    def __init__(self, driver):
        self._page = BasePage(driver)

    __loc_logo = (By.XPATH, "//a[@class='oxd-brand']")
    __loc_time_to_work = (By.XPATH, "//button[contains(@class, 'attendance-card-action')]")
    __loc_my_act = (By.XPATH, "(//button[contains(@class, 'report-icon')])[1]")
    __loc_my_info = (By.XPATH, "//*[contains(@href, 'viewMyDetails')]")
    __loc_cards = (By.XPATH, "//div[contains(@class, 'oxd-sheet--white orangehrm-dashboard-widget')]")
    __loc_main_menu = (By.XPATH, "//ul[contains(@class, 'oxd-main-menu')]")
    __loc_buttons_on_card_quick_launch = (By.XPATH, "//div[contains(@class, 'oxd-grid-3 orangehrm-quick-launch')]")
    __loc_admin = (By.XPATH, "//*[contains(@href, 'admin')]")
    __loc_buttons_on_card_buzz_posts = (By.XPATH, ("(//div[contains(@class, 'oxd-sheet oxd-sheet--rounded oxd-sheet--"
                                                   "white orangehrm-dashboard-widget')])[4]"))

    def is_logo_displayed(self):
        return self._page.is_displayed(self.__loc_logo)

    def main_menu(self):
        data = self._page.get_text(self.__loc_main_menu)
        return data

    def get_card_count(self):
        return self._page.get_element_count(self.__loc_cards)

    def get_button_count(self):
        return self._page.get_element_count(self.__loc_buttons_on_card_quick_launch)

    def button_on_card_quick_launch(self):
        data = self._page.get_text(self.__loc_buttons_on_card_quick_launch)
        return data

    def click_my_info(self):
        self._page.click(self.__loc_my_info)
        return MyInfoPage(self._page.driver)

    def click_admin(self):
        self._page.click(self.__loc_admin)
        return AdminUserManagement(self._page.driver)

    def get_card_text(self):
        data = self._page.get_text(self.__loc_buttons_on_card_buzz_posts)
        return data
