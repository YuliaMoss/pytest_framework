import json
import pytest
import yaml
from yaml import FullLoader

from constants import ROOT_PATH
from page_objects.login_page import LoginPage
from utilities.config_reader import AppConfig
from utilities.driver_factory import DriverFactory
from utilities.json_to_dict import DictToClass


# def pytest_addoption(parser):
#     parser.addoption('--env', action='store', default='dev', help='Choose your env')


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "smoke: mark test smoke"
    )

    config.addinivalue_line(
        "markers", "sanity: mark test sanity"
    )


@pytest.fixture
def env():
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
def create_driver(env):
    driver = DriverFactory(env.browser_id).get_driver()
    driver.maximize_window()
    driver.get(env.url)
    yield driver
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
