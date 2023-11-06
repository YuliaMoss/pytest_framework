import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_my_info(open_login_page, get_user):
    my_info_page = open_login_page.do_login(*get_user)
    assert my_info_page.click_my_info(), "Test failed, my info page is not opened"


@pytest.mark.smoke
def test_full_name(open_my_info, get_name):
    assert open_my_info.set_full_name(*get_name), "Test failed, full name is not set"


@pytest.mark.smoke
def test_scroll_and_get_text(open_my_info):
    assert open_my_info.get_text_with_scroll(), "Test failed, button is not appeared"


@pytest.mark.smoke
def test_click_radio_button_gender(open_my_info):
    assert open_my_info.click_radio_button_gender(), "Test failed, gender is not set"


@pytest.mark.regression
def test_get_name_text(open_my_info):
    assert open_my_info.get_name_text(), "Test failed, name is not displayed"
