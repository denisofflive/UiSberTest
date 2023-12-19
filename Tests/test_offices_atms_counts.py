import time
from conftest import browser
from pages.locators import main_url
from pages.main_page import MainPage

def test_offices_atms_counts(browser):
    main_page = MainPage(browser, main_url)
    # Открываем страницу
    main_page.open()
    # Геометка
    main_page.geoposition()
    time.sleep(2)

    # Подсчет элементов на странице у офисов
    main_page.offices_count()
    time.sleep(1)

    # Подсчет элементов на странице у банкоматов
    main_page.atms_count()
    time.sleep(3)
