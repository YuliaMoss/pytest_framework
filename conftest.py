import pytest
from page_objects.login_page import LoginPage
from utilities.config_reader import AppConfig
from utilities.driver_factory import DriverFactory


@pytest.fixture
def create_driver():
    driver = DriverFactory(AppConfig.browser_id).get_driver()
    driver.maximize_window()
    driver.get(AppConfig.app_url)
    yield driver
    driver.quit()


@pytest.fixture
def open_login_page(create_driver):
    return LoginPage(create_driver)


@pytest.fixture
def get_user():
    return AppConfig.login, AppConfig.password


@pytest.fixture
def get_name():
    return AppConfig.firstname, AppConfig.middle_name, AppConfig.lastname
