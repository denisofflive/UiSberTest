import time
import pytest

from Steps.assert_steps import AssertSteps
from conftest import browser
from pages.locators import main_url
from pages.main_page import MainPage

# Тест - подсчет элементов на странице у курсов валют
@pytest.mark.full_regress
def test_open_sber_main_page(browser):
    main_page = MainPage(browser, main_url)
    # Открываем страницу
    main_page.open()
    # Геометка (без неё не сработает тест)
    main_page.geoposition()
    # Подсчет элементов на странице у курсов валют
    main_page.exchange_rates_count()
    time.sleep(3)


# Тест - проверка корректного перехода по ссылкам меню
@pytest.mark.full_regress
def test_moving_menu_links(browser):
    main_page = MainPage(browser, main_url)
    assert_steps = AssertSteps(browser)
    # Открываем страницу
    main_page.open()
    # Проверяем, что ссылка с курсами валют присутствует
    assert_steps.should_be_exchange_rates_link()
    # Находим ссылку курсов валют и нажимаем на неё
    main_page.click_on_exchange_rates_link()
    # Переключение между вкладками (без переключения не сработает тест)
    browser.switch_to.window(browser.window_handles[1])
    print("Переключение между вкладками")
    time.sleep(3)
    # Проверка страницы Курсы валют (считываем заголовок)
    assert_steps.assert_exchange_rates_title()
    time.sleep(3)


# Тест - проверка корректного поиска и выбора геопозиции
@pytest.mark.smoke
@pytest.mark.full_regress
@pytest.mark.parametrize('text',
                         [
                             "Санкт-Петербург",
                             "Ростовская",
                             "Республика Са",
                             "Адыгея",
                             "Сахалин",
                             "кРасНоДар"
                         ],
                         ids=["City",
                              "Region",
                              "Part of region",
                              "Region name",
                              "Low letters",
                              "Crazy letters"]
                         )
def test_check_geoposition(browser, text):
    main_page = MainPage(browser, main_url)
    assert_steps = AssertSteps(browser)
    # Открываем страницу
    main_page.open()
    # Геометка (без неё сработает тест)
    main_page.geoposition()
    # Нажать на геопозицию
    main_page.click_on_geoposition_link()
    # Заполняем регион(ы) текстом
    main_page.fill_text_region_name_field(text)
    # Нажимаем на регион(ы)
    main_page.click_on_region_name_link(text)
    # Проверяем текст выбранный на странице (регионы), что он там есть
    assert_steps.assert_region_name_in_geo_link(text)
    time.sleep(3)

@pytest.mark.full_regress
def test_incorrect_geoposition(browser):
    main_page = MainPage(browser, main_url)
    assert_steps = AssertSteps(browser)
    # Открываем страницу
    main_page.open()
    # Геометка (без неё не сработает тест)
    main_page.geoposition()
    # Нажать на геопозицию
    main_page.click_on_geoposition_link()
    # Ввести рандомный (некорректный) регион
    main_page.fill_incorrect_region_name_field()
    # Проверка несуществующего элемента (региона)
    assert_steps.should_not_be_success_region_button()
    time.sleep(3)


# Тест - проверка корректного количества элементов на странице
@pytest.mark.full_regress
def test_count_exchange_count(browser):
    main_page = MainPage(browser, main_url)
    assert_steps = AssertSteps(browser)
    # Открываем страницу
    main_page.open()
    # Геометка (без неё не сработает тест)
    main_page.geoposition()
    # Подсчет элементов на странице у курсов валют
    main_page.exchange_rates_count()
    # Проверка количества элементов у курсов валют
    assert_steps.assert_exchange_rates_count()
    time.sleep(3)


# Тест - проверка изменения цвета ссылки
@pytest.mark.full_regress
def test_color_links(browser):
    main_page = MainPage(browser, main_url)
    assert_steps = AssertSteps(browser)
    # Открываем страницу
    main_page.open()
    # Геометка (без неё не сработает тест)
    main_page.geoposition()

    # Находим вкладку СберБанк Онлайн
    main_page.sberonline_button()
    # Проверяем, что цвет до и после наведения мыши не равны
    assert_steps.assert_colors_not_equal()
    time.sleep(3)

# Негативный тест - проверка корректного перехода по ссылкам меню
@pytest.mark.full_regress
def test_moving_menu_links_negative(browser):
    try:
        main_page = MainPage(browser, main_url)
        assert_steps = AssertSteps(browser)
        # Открываем страницу
        main_page.open()
        # Геометка (без неё не сработает тест)
        main_page.geoposition()

        # Нажать на вкладку Курсы валют
        main_page.click_on_exchange_rates_link()
        # Переключение между вкладками
        browser.switch_to.window(browser.window_handles[1])
        time.sleep(3)
        # Заголовок на странице Курсы валют
        main_page.first_page_title_exchange_rates()
        # Проверка некорректного заголовка Курсы валют
        assert_steps.assert_incorrect_title__exchange_rates_title()
        time.sleep(3)
    finally:
        browser.quit()

@pytest.mark.full_regress
def test_check_incorrect_geoposition(browser):
    main_page = MainPage(browser, main_url)
    # Открываем страницу
    main_page.open()
    # Геометка (без неё не сработает тест)
    main_page.geoposition()

    # Нажать на геопозицию
    main_page.click_on_geoposition_link()
    # Заполняем регион рандомным (некорректным) текстом
    main_page.fill_incorrect_region_name_field()
    time.sleep(3)
