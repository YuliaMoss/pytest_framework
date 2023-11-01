import pytest


@pytest.mark.smoke
def test_admin_user_management_page(open_login_page, get_user):
    dashboard_page = open_login_page.do_login(*get_user)
    admin_page = dashboard_page.click_admin()
    assert admin_page.is_add_button_displayed(), "Test failed, button not displayed"


@pytest.mark.regression
def test_records_text(open_login_page, get_user):
    dashboard_page = open_login_page.do_login(*get_user)
    admin_page = dashboard_page.click_admin()
    text = admin_page.get_records_text()
    assert text


@pytest.mark.smoke
def test_el_count(open_login_page, get_user):
    dashboard_page = open_login_page.do_login(*get_user)
    admin_page = dashboard_page.click_admin()
    num = admin_page.count_records()
    assert num
