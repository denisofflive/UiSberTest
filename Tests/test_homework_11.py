import time
import pytest
from Steps.assert_steps import AssertSteps
from pages.locators import main_url
from pages.main_page import MainPage


# Тест с проверкой корректного перехода по ссылкам меню "Курсы валют, "Офисы", "Банкоматы"
@pytest.mark.full_regress
def test_moving_menu_links(browser):
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
        # Проверка страницы Курсы валют
        assert_steps.assert_exchange_rates_title()
        # Переключение между вкладками (главная страница)
        browser.switch_to.window(browser.window_handles[0])
        print("Переключение на вкладку Главная страница")
        time.sleep(3)

        # Нажать на вкладку Офисы
        main_page.click_on_offices_link()
        time.sleep(3)
        # Проверка страницы Офисы
        assert_steps.assert_offices_page_title()
        time.sleep(3)
        # Вернуться назад (на главную страницу)
        browser.back()

        # Нажать на вкладку Банкоматы
        main_page.click_on_atms_link()
        time.sleep(3)
        # Проверка страницы Банкоматы
        assert_steps.assert_atms_page_title()
        # Вернуться назад (на главную страницу)
        browser.back()
        time.sleep(3)
    finally:
        browser.quit()

# Тест с проверкой корректного перехода по ссылке меню "СберБанк Онлайн"
@pytest.mark.full_regress
def test_moving_menu_sberonline_link(browser):
    try:
        main_page = MainPage(browser, main_url)
        assert_steps = AssertSteps(browser)
        # Открываем страницу
        main_page.open()
        # Геометка (без неё не сработает тест)
        main_page.geoposition()

        # Нажать на вкладку СберБанк Онлайн
        main_page.click_on_sberonline_button()
        time.sleep(3)
        # Переключение между вкладками
        browser.switch_to.window(browser.window_handles[1])
        time.sleep(3)
        # Проверка страницы СберБанк (Правила безопасности)
        assert_steps.assert_security_regulations_title_on_sber_online()
        time.sleep(3)
    finally:
        browser.quit()

# Тест с проверкой корректной работы поиска
@pytest.mark.full_regress
def test_check_search(browser):
    try:
        main_page = MainPage(browser, main_url)
        assert_steps = AssertSteps(browser)
        # Открываем страницу
        main_page.open()
        # Геометка (без неё не сработает тест)
        main_page.geoposition()
        main_page.click_on_geoposition_link()

        # Ввести имя региона Ленинградская область
        main_page.fill_leningrad_region_name()
        # Нажать на кнопку поиска
        main_page.click_on_leningrad_region_field()
        time.sleep(3)
        # Проверяем, что выбранный текст на странице (Ленинградская область) есть
        assert_steps.assert_leningrad_geopostion()
        time.sleep(3)
    finally:
        browser.quit()

# Тест - проверка корректного количества элементов на странице для ссылок "Курсы валют, Офисы, Банкоматы,
# СберБанк Онлайн"
@pytest.mark.full_regress
def test_count_links(browser):
    try:
        main_page = MainPage(browser, main_url)
        assert_steps = AssertSteps(browser)
        # Открываем страницу
        main_page.open()
        # Геометка (без неё не сработает тест)
        main_page.geoposition()

        # Проверка и подсчет элементов на странице у Курсов валют
        assert_steps.assert_exchange_rates_count()

        # Подсчет элементов на странице у Офисов
        assert_steps.assert_offices_count()

        # Подсчет элементов на странице у Банкоматов
        assert_steps.assert_atms_count()

        # Подсчет элементов на странице у СберБанк Онлайн
        assert_steps.assert_sber_online_count()
        time.sleep(3)
    finally:
        browser.quit()

# Тест - проверка изменения цвета ссылок "Курсы валют", "Офисы", "Банкоматы", "СберБанк Онлайн"
@pytest.mark.smoke
def test_color_links(browser):
    try:
        main_page = MainPage(browser, main_url)
        assert_steps = AssertSteps(browser)
        # Открываем страницу
        main_page.open()
        # Геометка (без неё не сработает тест)
        main_page.geoposition()
        time.sleep(3)

        # Проверка, что цвет до и после наведения на вкладку Курсы валют мыши не равны
        assert_steps.assert_colors_not_equal_by_exchange_rates()
        time.sleep(3)

        # Находим вкладку Офисы
        assert_steps.assert_colors_not_equal_by_offices()
        time.sleep(3)

        # Находим вкладку Банкоматы
        assert_steps.assert_colors_not_equal_by_atms()
        time.sleep(3)

        # Находим вкладку СберБанк Онлайн
        assert_steps.assert_colors_not_equal_by_sber_online()
        time.sleep(3)
    finally:
        browser.quit()

# Тест с проверками корректности заголовков страниц для сценария
@pytest.mark.full_regress
def test_check_headers(browser):
    try:
        main_page = MainPage(browser, main_url)
        assert_steps = AssertSteps(browser)
        # Открываем страницу
        main_page.open()
        # Геометка (без неё не сработает тест)
        main_page.geoposition()

        # Нажать на вкладку СберБанк Онлайн
        main_page.click_on_sberonline_button()
        # Переключение между вкладками
        browser.switch_to.window(browser.window_handles[1])
        # Проверка страницы авторизации на странице СберБанк Онлайн (Правила безопасности)
        assert_steps.assert_security_regulations_title_on_sber_online()
        # Переключение между вкладками
        browser.switch_to.window(browser.window_handles[0])
        time.sleep(3)
        # Проверка заголовка Лучшие предложения для главной страницы Сбера
        assert_steps.assert_best_offers_title_on_sber()
        time.sleep(3)
    finally:
        browser.quit()
