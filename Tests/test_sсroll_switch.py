import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from conftest import browser
from pages.locators import main_url
from pages.main_page import MainPage


# Тест - скролл по странице
@pytest.mark.smoke
def test_scroll_page(browser):
    main_page = MainPage(browser, main_url)
    # Открываем страницу
    main_page.open()
    # Геометка (без неё сработает тест)
    main_page.geoposition()

    # Скролл на один экран вниз
    browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(3)
    # Скролл прокрутка до футера
    browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(3)
    # Скролл на один экран вверх
    browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_UP)
    time.sleep(3)
    # Скролл на вверх к хедеру
    browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.HOME)
    time.sleep(3)


# Тест - переключение между вкладками
@pytest.mark.smoke
def test_switch_page(browser):
    main_page = MainPage(browser, main_url)
    # Открываем страницу
    main_page.open()
    # Геометка (без неё сработает тест)
    main_page.geoposition()
    # Нажать на Сбербанк Онлайн
    main_page.click_on_sberonline_button()
    # Переключение между вкладками (переход на главную страницу Сбера)
    browser.switch_to.window(browser.window_handles[0])
    print("Главная страница Сбера")
    time.sleep(3)
    # Нажать на Сбербанк Онлайн
    main_page.click_on_exchange_rates_link()
    time.sleep(3)
    # Переключение между вкладками (переход на страницу СберБанк Онлайн)
    browser.switch_to.window(browser.window_handles[1])
    print("Страница СберБанк Онлайн")
    time.sleep(3)
