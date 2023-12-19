import time
import pytest
from pages.locators import main_url
from pages.main_page import MainPage

# Выбор английского языка
@pytest.mark.smoke
def test_change_language_page(browser):
    # Запуск браузера
    main_page = MainPage(browser, main_url)
    # Открываем страницу
    main_page.open()
    # Геометка
    main_page.geoposition()
    # Выбрать английский язык
    main_page.click_on_eng_language()
    time.sleep(3)

@pytest.mark.full_regress
def test_search(browser):
    # Запуск браузера
    main_page = MainPage(browser, main_url)
    # Открываем страницу
    main_page.open()
    # Геометка
    main_page.geoposition()
    time.sleep(3)
    # Клик и поиск по сайту
    main_page.click_on_search_button()
    # Заполнить поле поиска и ввести кредит
    main_page.fill_search_field()
    # Нажать и подтвердить кнопку поиска
    main_page.click_on_button_submit()
    time.sleep(3)

    # Негативный сценарий

    # Очистить поисковое поле
    main_page.clear_text_search_field()
    # Ввести несуществующее значение
    main_page.fill_random_text_search_field()
    # Нажать на кнопку поиск
    main_page.text_button_submit()
    time.sleep(3)

    # Закрытие строки поиска

    # Нажать на кнопку поиск
    main_page.click_on_search_button()
    # Закрыть кнопку поиск
    main_page.click_on_reset_button()
    time.sleep(5)

@pytest.mark.smoke
def test_actions_chains(browser):
    # Запуск браузера
    main_page = MainPage(browser, main_url)
    # Открываем страницу
    main_page.open()
    # Геометка
    main_page.geoposition()
    time.sleep(1)

    # Наведение курсора мыши на Курсы Валют
    main_page.actionChains_exchange_rates_button()
    time.sleep(1)

    # Наведение курсора мыши на Офисы
    main_page.actionChains_offices_button()
    time.sleep(1)

    # Наведение курсора мыши на Банкоматы
    main_page.actionChains_atms_button()
    time.sleep(1)

    # Наведение курсора мыши на Геопозиция
    main_page.actionChains_geoposition_button()
    time.sleep(1)

    # Наведение курсора мыши на Смена языка
    main_page.actionChains_change_language_button()
    time.sleep(1)

    # Наведение курсора мыши на Поиск
    main_page.actionChains_search_button()
    time.sleep(3)

