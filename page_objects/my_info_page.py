from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class MyInfoPage:
    def __init__(self, driver):
        self._page = BasePage(driver)

    __loc_firstname_input = (By.XPATH, "//*[contains(@class, 'firstname')]")
    __loc_middle_name_input = (By.XPATH, "//*[contains(@class, 'middlename')]")
    __loc_lastname_input = (By.XPATH, "//*[contains(@class, 'lastname')]")
    __loc_submit_button = (By.XPATH, "//*[contains(@type, 'submit')]")
    __loc_add_button = (By.XPATH, "//*[contains(@class, 'oxd-button--text')]")
    __loc_radio_button = (By.XPATH, "(//*[contains(@class, 'oxd-radio-input')])[2]")
    __loc_marital_status = (By.XPATH, "(//*[contains(@class, ' oxd-select-text--active')])[2]")
    __loc_name = (By.XPATH, "//*[contains(@class, 'oxd-input oxd-input--active orangehrm-firstname')]")

    def clean_input_firstname(self):
        self._page.clear_input(self.__loc_firstname_input)
        return self

    def clean_input_middle_name(self):
        self._page.clear_input(self.__loc_middle_name_input)
        return self

    def clean_input_lastname(self):
        self._page.clear_input(self.__loc_lastname_input)
        return self

    def set_firstname(self, firstname: str):
        self._page.send_key(self.__loc_firstname_input, value=firstname)
        return self

    def set_middle_name(self, middle_name: str):
        self._page.send_key(self.__loc_middle_name_input, value=middle_name)
        return self

    def set_lastname(self, lastname: str):
        self._page.send_key(self.__loc_lastname_input, value=lastname)
        return self

    def click_submit_button(self):
        self._page.click(self.__loc_submit_button)
        return self

    # STEPS
    def set_full_name(self, firstname: str, middle_name: str, lastname: str):
        self.clean_input_firstname()
        self.set_firstname(firstname)
        self.clean_input_middle_name()
        self.set_middle_name(middle_name)
        self.clean_input_lastname()
        self.set_lastname(lastname)
        return self.click_submit_button()

    def get_text_with_scroll(self):
        self._page.scroll_to_el(self.__loc_add_button)
        data = self._page.get_text_present(self.__loc_add_button)
        return data

    def click_radio_button_gender(self):
        self._page.wait_element_is_visible(self.__loc_radio_button)
        self._page.click_radio_button(self.__loc_radio_button)
        return self.click_submit_button()

    def get_name_text(self):
        first_name = self._page.get_attribute(self.__loc_firstname_input)
        middle_name = self._page.get_attribute(self.__loc_middle_name_input)
        lastname = self._page.get_attribute(self.__loc_lastname_input)
        return f"{first_name} {middle_name} {lastname}"
