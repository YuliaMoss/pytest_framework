import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_my_info(open_login_page, get_user):
    my_info_page = open_login_page.do_login(*get_user)
    assert my_info_page.click_my_info()


@pytest.mark.smoke
def test_full_name(open_login_page, get_user, get_name):
    my_info_page = open_login_page.do_login(*get_user)
    set_my_info = my_info_page.click_my_info()
    new_name = set_my_info.set_full_name(*get_name)
    assert new_name


@pytest.mark.smoke
def test_scroll_and_get_text(open_login_page, get_user):
    my_info_page = open_login_page.do_login(*get_user)
    set_my_info = my_info_page.click_my_info()
    text = set_my_info.get_text_with_scroll()
    assert text


@pytest.mark.smoke
def test_click_radio_button_gender(open_login_page, get_user):
    my_info_page = open_login_page.do_login(*get_user)
    set_my_info = my_info_page.click_my_info()
    new_result = set_my_info.click_radio_button_gender()
    my_info_page._page.save_screenshot()
    assert new_result


@pytest.mark.regression
def test_get_name_text(open_login_page, get_user):
    my_info_page = open_login_page.do_login(*get_user)
    set_my_info = my_info_page.click_my_info()
    my_name = set_my_info.get_name_text()
    assert my_name
