import pytest


@pytest.mark.smoke
def test_main_menu(open_login_page, get_user):
    dashboard_page = open_login_page.do_login(*get_user)
    assert dashboard_page.main_menu(), "Test failed, there is no main menu"


@pytest.mark.regression
def test_count_cards(open_login_page, get_user):
    dashboard_page = open_login_page.do_login(*get_user)
    exc_count = 7
    assert dashboard_page.get_card_count() == exc_count, "Test failed, the number of cards is not equal to 7"


@pytest.mark.regression
def test_get_button_count(open_login_page, get_user):
    dashboard_page = open_login_page.do_login(*get_user)
    exc_count = 6
    assert dashboard_page.get_button_count() == exc_count, "Test failed, the number of cards is not equal to 6"


@pytest.mark.smoke
def test_titles_button(open_login_page, get_user):
    dashboard_page = open_login_page.do_login(*get_user)
    assert dashboard_page.button_on_card_quick_launch(), "Test failed, the text is not equal to 'Assign Leave'"


@pytest.mark.regression
def test_get_card_text(open_login_page, get_user):
    dashboard_page = open_login_page.do_login(*get_user)
    assert dashboard_page.get_card_text(), "Test failed, the text is not equal to 'Buzz Latest Posts'"
