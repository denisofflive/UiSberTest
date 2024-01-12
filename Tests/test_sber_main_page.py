import pytest

from Steps import support_steps as support_steps
from pages.main_page import MainPage
from pages.locators import MainPageLocators
from pages.locators import BasePageLocators


# Тест успешного выполнения поиска
@pytest.mark.full_regress
@pytest.mark.smoke
def test_search_on_the_main_page(browser):
    main_page = MainPage(browser, "http://www.sberbank.ru")
    main_page.open()
    main_page.geoposition()
    main_page.search_button_search("кредит")
    main_page.assert_check_search("кредит", MainPageLocators.SEARCH_INPUT_VAR)


# Негативный тест выполнения поиска
@pytest.mark.full_regress
def test_negative_search(browser):
    main_page = MainPage(browser, "http://www.sberbank.ru")
    main_page.open()
    main_page.geoposition()
    main_page.search_button_search(support_steps.generate_random_letter_strings(30))
    main_page.assert_check_search("Искомая комбинация слов нигде не встречается", MainPageLocators.TAG_B)


# Тест на проверку изменения цвета ссылок при hover
@pytest.mark.full_regress
@pytest.mark.smoke
@pytest.mark.parametrize("element",
                         [
                             MainPageLocators.EXCHANGE_RATES_BUTTON,
                             MainPageLocators.OFFICE_BUTTON,
                             MainPageLocators.ATMS_BUTTON,
                             MainPageLocators.GEOPOSITION_BUTTON,
                             MainPageLocators.CHANGE_LANGUAGE_BUTTON,
                             MainPageLocators.SEARCH_BUTTON_HOVER,
                             MainPageLocators.SBERONLINE_BUTTON
                         ], ids=["exchange_rates_button", "office_button", "atms_button", "geoposition_button",
                                 "change_language_button", "search_button", "sberonline_button"]
                         )
def test_hover_elements(browser, element):
    main_page = MainPage(browser, "http://www.sberbank.ru")
    main_page.open()
    main_page.geoposition()
    main_page.hover_elements(main_page.driver.find_element(*element))


# Тест на проверку, что ссылки имеют href отличный от главной страницы
@pytest.mark.full_regress
@pytest.mark.smoke
@pytest.mark.parametrize("element",
                         [
                             MainPageLocators.EXCHANGE_RATES_BUTTON,
                             MainPageLocators.OFFICE_BUTTON,
                             MainPageLocators.ATMS_BUTTON,
                             MainPageLocators.SBERONLINE_BUTTON
                         ], ids=["exchange_rates_button",
                                 "office_button",
                                 "atms_button",
                                 "sberonline_button"]
                         )
def test_open_new_tab(browser, element):
    main_page = MainPage(browser, "http://www.sberbank.ru")
    main_page.open()
    main_page.geoposition()
    main_url = main_page.get_link()
    main_page.assert_correct_link(main_url, main_page.driver.find_element(*element))


# Тест на проверку корректности заголовков страниц
@pytest.mark.full_regress
@pytest.mark.smoke
def test_correct_open_new_tab(browser):
    main_page = MainPage(browser, "http://www.sberbank.ru")
    main_page.open()
    main_page.geoposition()
    main_page.jump_to_authorization_page()
    main_page.assert_correct_text("Правила безопасности", 1, BasePageLocators.TAG_H4)
    main_page.assert_correct_text("Лучшие предложения", 0, BasePageLocators.TAG_FIRST_H2)


# Тест подсчета ссылок на странице
@pytest.mark.full_regress
@pytest.mark.smoke
@pytest.mark.parametrize("element, count",
                         [
                             (MainPageLocators.OFFICE_LINK, 3),
                             (MainPageLocators.ATMS_LINK, 3),
                             (MainPageLocators.EXCHANGE_RATES_BUTTON, 4),
                             (MainPageLocators.SBERONLINE_BUTTON, 2)
                         ], ids=["ссылок Офисы - 3", "ссылок Банкоматы - 3", "ссылок Курсы валют - 4",
                                 "ссылок СберБанк Онлайн - 2"]
                         )
def test_count(browser, element, count):
    main_page = MainPage(browser, "http://www.sberbank.ru")
    main_page.open()
    main_page.geoposition()
    main_page.assert_number_links(main_page.driver.find_elements(*element), count)
