from selenium.webdriver import Chrome, Firefox

_CHROME_ID = 1
_FIREFOX_ID = 2


class DriverFactory:
    def __init__(self, browser_id: int):
        self.browser_id = browser_id

    def get_driver(self):
        if int(self.browser_id) == _CHROME_ID:
            return self.__get_chrome_driver()
        elif int(self.browser_id) == _FIREFOX_ID:
            return self.__get_firefox_driver()
        else:
            return self.__get_chrome_driver()

    @staticmethod
    def __get_chrome_driver():
        driver = Chrome()
        return driver

    @staticmethod
    def __get_firefox_driver():
        driver = Firefox()
        return driver
