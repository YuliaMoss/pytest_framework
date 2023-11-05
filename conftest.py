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


@pytest.fixture
def open_admin_user_management_page(open_login_page, get_user):
    dashboard_page = open_login_page.do_login(*get_user)
    return dashboard_page.click_admin()


@pytest.fixture
def open_my_info(open_login_page, get_user):
    my_info_page = open_login_page.do_login(*get_user)
    return my_info_page.click_my_info()
