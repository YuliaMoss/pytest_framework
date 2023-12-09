import json
import pytest
from faker import Faker
from yaml import FullLoader
import yaml
from constants import ROOT_PATH
from page_objects.login_page import LoginPage
from utilities.driver_factory import DriverFactory
from utilities.json_to_dict import DictToClass
import allure


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)


def pytest_addoption(parser):
    parser.addoption('--env', action='store', default='dev', help='Choose your env')
    parser.addoption('--hub', action='store', default='True', help='Run test in container Selenoid')
    parser.addoption('--headless', action='store', default='False', help='Run test in headless mode')
    # parser.addoption('--browser', action='store', default='2', help='Choose yor browser (1- chrome, 2 -firefox)')


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "smoke: mark test smoke"
    )

    config.addinivalue_line(
        "markers", "sanity: mark test sanity"
    )


@pytest.fixture
def env(request):
    _env_name = request.config.getoption('--env')
    with open(f'{ROOT_PATH}/configs/conf.json') as f:
        conf_dict = json.loads(f.read())
        return DictToClass(**conf_dict)


@pytest.fixture
def env_yaml(request):
    _env_name = request.config.getoption('--env')
    with open(f'{ROOT_PATH}/configs/dev.yaml') as f:
        conf_dict = yaml.load(f.read(), Loader=FullLoader)
        return DictToClass(**conf_dict)


@pytest.fixture
def create_driver(env, request):
    driver = DriverFactory(
        browser_id=env.browser_id,
        hub=eval(request.config.getoption('--hub')),
        headless=eval(request.config.getoption('--headless'))
    ).get_driver()
    driver.maximize_window()
    driver.get(env.url)
    yield driver
    if request.node.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(),
                      name='Fail_screenshot',
                      attachment_type=allure.attachment_type.PNG)
    driver.quit()


@pytest.fixture
def open_login_page(create_driver):
    return LoginPage(create_driver)


@pytest.fixture
def get_user(env):
    return env.user_data.login, env.user_data.password


@pytest.fixture
def get_name(env):
    return (env.firstname,
            env.middle_name,
            env.lastname)


@pytest.fixture
def open_admin_user_management_page(open_login_page, get_user):
    dashboard_page = open_login_page.do_login(*get_user)
    return dashboard_page.click_admin()


@pytest.fixture
def open_my_info(open_login_page, get_user):
    my_info_page = open_login_page.do_login(*get_user)
    return my_info_page.click_my_info()


@pytest.fixture
def fake():
    fake = Faker()
    return fake
