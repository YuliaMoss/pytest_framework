import pytest


@pytest.mark.smoke
def test_admin_user_management_page(open_admin_user_management_page):
    assert open_admin_user_management_page.is_add_button_displayed(), "Test failed, button not displayed"


@pytest.mark.regression
def test_records_text(open_admin_user_management_page):
    assert open_admin_user_management_page.get_records_text(), "Test failed, there are no text on records"


@pytest.mark.smoke
def test_el_count(open_admin_user_management_page):
    assert open_admin_user_management_page.count_records(), "Test failed, there are no records"
