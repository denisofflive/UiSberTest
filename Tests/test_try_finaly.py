import time
import pytest
from Steps.assert_steps import AssertSteps
from conftest import browser
from pages.locators import main_url
from pages.main_page import MainPage


# Тест подсчета элементов на странице у курсов валют
def test_open_sber_main_page(browser):
    try:
        # Запуск браузера
        main_page = MainPage(browser, main_url)
        # Открываем страницу
        main_page.open()
        # Геометка
        main_page.geoposition()
        # Подсчет элементов на странице у курсов валют
        main_page.exchange_rates_count()
        time.sleep(3)
    finally:
        browser.quit()

# Тест - проверка корректного перехода по ссылкам меню
def test_moving_menu_links(browser):
    try:
        # Запуск браузера
        main_page = MainPage(browser, main_url)
        assert_steps = AssertSteps(browser)
        # Открываем страницу
        main_page.open()
        # Геометка
        main_page.geoposition()

        # Нажать на вкладку Курсы валют
        main_page.click_on_exchange_rates_link()
        # Переключение между вкладками
        browser.switch_to.window(browser.window_handles[1])
        time.sleep(3)
        # Проверка страницы Курсы валют
        assert_steps.assert_exchange_rates_title()
        time.sleep(3)
    finally:
        browser.quit()

# Тест - проверка корректного поиска и выбора геопозиции
@pytest.mark.smoke
@pytest.mark.full_regress
def test_check_geoposition(browser):
    try:
        # Запуск браузера
        main_page = MainPage(browser, main_url)
        assert_steps = AssertSteps(browser)
        # Открываем страницу
        main_page.open()
        # Геометка
        main_page.geoposition()
        # Нажать на геопозицию и вывести её на экран
        main_page.click_on_geoposition_link()
        # Ввести регион Ростовская область и кликнуть по нему
        main_page.fill_rostov_region_name()
        main_page.click_on_rostov_region_field()
        time.sleep(3)
        # Проверяем текст выбранный на странице (Ростовская область), что он там есть
        main_page.geoposition()
        assert_steps.assert_geopostion()
        time.sleep(3)
    finally:
        browser.quit()

def test_count_links(browser):
    try:
        # Запуск браузера
        main_page = MainPage(browser, main_url)
        assert_steps = AssertSteps(browser)
        # Открываем страницу
        main_page.open()
        # Геометка
        main_page.geoposition()

        # Подсчет элементов на странице у курсов валют
        main_page.exchange_rates_count()
        # Проверка количества элементов
        assert_steps.assert_exchange_rates_count()
        time.sleep(3)
    finally:
        browser.quit()

def test_color_links(browser):
    try:
        # Запуск браузера
        main_page = MainPage(browser, main_url)
        assert_steps = AssertSteps(browser)
        # Открываем страницу
        main_page.open()
        # Геометка
        main_page.geoposition()
        # Проверка, что цвет до и после наведения мыши на вкладку Сбербанк Онлайн не равны
        assert_steps.assert_colors_not_equal()
        time.sleep(3)
    finally:
        browser.quit()

# Негативный тест - проверка корректного перехода по ссылкам меню
def test_moving_menu_links_negative(browser):
    try:
        # Запуск браузера
        main_page = MainPage(browser, main_url)
        assert_steps = AssertSteps(browser)
        # Открываем страницу
        main_page.open()
        # Геометка
        main_page.geoposition()

        # Нажать на вкладку Курсы валют
        main_page.click_on_exchange_rates_link()
        # Переключение между вкладками
        browser.switch_to.window(browser.window_handles[1])
        time.sleep(3)
        # Проверка страницы Курсы валют
        assert_steps.assert_incorrect_exchange_rates_title()
        time.sleep(3)
    finally:
        browser.quit()

# Негативный тест - проверка некорректного поиска и выбора геопозиции
def test_check_geoposition_negative(browser):
    try:
        # Запуск браузера
        main_page = MainPage(browser, main_url)
        assert_steps = AssertSteps(browser)
        # Открываем страницу
        main_page.open()
        # Геометка
        main_page.geoposition()
        main_page.click_on_geoposition_link()
        # Ввести регион - Ростовская область
        main_page.fill_rostov_region_name()
        # Нажать на Ростовскую область
        main_page.click_on_rostov_region_field()
        time.sleep(3)
        # Проверяем текст выбранный на странице (Ростовская область), что он там есть
        assert_steps.assert_incorrect_rostov_geoposition()
        time.sleep(3)
    finally:
        browser.quit()
