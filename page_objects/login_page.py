from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from page_objects.dashboard_page import DashboardPage


class LoginPage():
    def __init__(self, driver):
        self._page = BasePage(driver)

    __loc_username_input = (By.XPATH, "//input[@name= 'username']")
    __loc_password_input = (By.XPATH, "//input[@name='password']")
    __loc_login_button = (By.XPATH, "//button[@type='submit']")

    def set_login(self, login: str):
        self._page.send_key(self.__loc_username_input, value=login)
        return self

    def set_password(self, password: str):
        self._page.send_key(self.__loc_password_input, value=password)
        return self

    def click_login_button(self):
        self._page.click(self.__loc_login_button)
        return DashboardPage(self._page.driver)

    # STEPS
    def do_login(self, login: str, password: str):
        self.set_login(login)
        self.set_password(password)
        return self.click_login_button()
