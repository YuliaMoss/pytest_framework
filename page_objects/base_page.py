from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_element_is_visible(self, locator: tuple, timeout=3) -> WebElement:
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    def wait_element_is_clickable(self, locator: tuple, timeout=3) -> WebElement:
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))

    def wait_element_is_present(self, locator: tuple, timeout=15) -> WebElement:
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))

    def send_key(self, locator: tuple, value):
        el = self.wait_element_is_visible(locator)
        el.send_keys(value)

    def click(self, locator: tuple):
        el = self.wait_element_is_clickable(locator)
        el.click()

    def is_displayed(self, locator: tuple):
        el = self.wait_element_is_visible(locator)
        return el.is_displayed()

    def get_element_count(self, locator: tuple):
        self.wait_element_is_present(locator)
        elements = self.driver.find_elements(*locator)
        return len(elements)

    def clear_input(self, locator: tuple):
        el = self.wait_element_is_visible(locator)
        el.click()
        # the clear() method doesn't remove information from the cell
        el.send_keys(Keys.BACKSPACE * 15)
        return self

    def get_text(self, locator: tuple):
        el = self.wait_element_is_visible(locator)
        return el.text

    def get_text_present(self, locator: tuple):
        el = self.wait_element_is_present(locator)
        return el.text

    def scroll_to_el(self, locator: tuple):
        el = self.wait_element_is_present(locator)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def click_radio_button(self, locator: tuple):
        el = self.wait_element_is_present(locator)
        return el.click()

    def save_screenshot(self):
        self.driver.get_screenshot_as_file('screen.png')

    def get_attribute(self, locator: tuple):
        self.wait_element_is_present(locator)
        el = self.driver.find_element(*locator)
        return el.get_attribute('value')
