import pytest


@pytest.mark.smoke
def test_main_menu(open_login_page, get_user):
    dashboard_page = open_login_page.do_login(*get_user)
    assert dashboard_page.main_menu()


@pytest.mark.regression
def test_count_cards(open_login_page, get_user):
    dashboard_page = open_login_page.do_login(*get_user)
    exc_count = 7
    assert dashboard_page.get_card_count() == exc_count


@pytest.mark.regression
def test_get_button_count(open_login_page, get_user):
    dashboard_page = open_login_page.do_login(*get_user)
    exc_count = 6
    assert dashboard_page.get_button_count() == exc_count


@pytest.mark.smoke
def test_titles_button(open_login_page, get_user):
    dashboard_page = open_login_page.do_login(*get_user)
    assert dashboard_page.button_on_card_quick_launch()


@pytest.mark.regression
def test_get_card_text(open_login_page, get_user):
    dashboard_page = open_login_page.do_login(*get_user)
    assert dashboard_page.get_card_text()
