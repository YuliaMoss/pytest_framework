import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_login(open_login_page, get_user):
    dashboard_page = open_login_page.do_login(*get_user)
    assert dashboard_page.is_logo_displayed(), "login failed,logo not displayed"
