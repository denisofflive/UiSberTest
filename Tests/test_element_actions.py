import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages import locators as locators
from pages.locators import main_url
from pages.main_page import MainPage

# Выбор английского языка
@pytest.mark.smoke
def test_change_language_page(browser):
    main_page = MainPage(browser, main_url)
    # Открываем страницу
    main_page.open()
    # Геометка (без неё не сработает тест)
    main_page.geoposition()
    # Выбрать английский язык
    main_page.click_on_eng_language()
    time.sleep(3)

def test_search(browser):
    main_page = MainPage(browser, main_url)
    # Открываем страницу
    main_page.open()
    # Геометка (без неё не сработает тест)
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

def test_actions_chains(browser):
    main_page = MainPage(browser, main_url)
    # Открываем страницу
    main_page.open()
    # Геометка (без неё не сработает тест)
    main_page.geoposition()
    # Нажать на геопозицию
    main_page.click_on_geoposition_link()
    time.sleep(3)

    # Наведение курсора мыши на Курсы Валют
    exchange_rates_button = driver.find_element(By.XPATH, locators.EXCHANGE_RATES_LINK)
    ActionChains(driver).move_to_element(exchange_rates_button).perform()
    print("Цвет кнопки Курсы Валют изменился")
    time.sleep(3)

    # Наведение курсора мыши на Офисы
    offices_button = driver.find_element(By.XPATH, locators.OFFICES_BUTTON)
    ActionChains(driver).move_to_element(offices_button).perform()
    print("Цвет кнопки Офисы изменился")
    time.sleep(3)

    # Наведение курсора мыши на Банкоматы
    atms_button = driver.find_element(By.XPATH, locators.ATMS_BUTTON)
    ActionChains(driver).move_to_element(atms_button).perform()
    print("Цвет кнопки Банкоматы изменился")
    time.sleep(3)

    # Наведение курсора мыши на Геопозиция
    geoposition_button = driver.find_element(By.XPATH, locators.GEOPOSITION_LINK)
    ActionChains(driver).move_to_element(geoposition_button).perform()
    print("Цвет кнопки Геопозиция изменился")
    time.sleep(3)

    # Наведение курсора мыши на Смена языка
    change_language_button = driver.find_element(By.XPATH, locators.ENG_LANGUAGE)
    ActionChains(driver).move_to_element(change_language_button).perform()
    print("Цвет кнопки Смена языка изменился")
    time.sleep(3)

    # Наведение курсора мыши на Поиск
    search_button = driver.find_element(By.XPATH, locators.SEARCH_BUTTON)
    ActionChains(driver).move_to_element(search_button).perform()
    print("Цвет кнопки Поиск изменился")
    time.sleep(3)
