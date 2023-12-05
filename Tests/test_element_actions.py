import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages import locators as locators

def test_change_language_page():
    driver = webdriver.Chrome()
    webdriver.ChromeOptions().add_argument('ignore-certificate-errors')
    driver.implicitly_wait(10)
    driver.get("https://www.sberbank.ru")
    driver.maximize_window()

    # Чтение геометки
    context_geo_button = driver.find_element(By.XPATH, locators.CONTEXT_GEO_BUTTON)
    context_geo_button.click()
    print("Геометка")
    time.sleep(3)

    # Смена языка
    eng_language = driver.find_element(By.XPATH, locators.ENG_LANGUAGE)
    eng_language.click()
    print("Eng language")
    time.sleep(3)


def test_search():
    driver = webdriver.Chrome()
    webdriver.ChromeOptions().add_argument('ignore-certificate-errors')
    driver.implicitly_wait(10)
    driver.get("https://www.sberbank.ru")
    driver.maximize_window()

    # Чтение геометки
    context_geo_button = driver.find_element(By.XPATH, locators.CONTEXT_GEO_BUTTON)
    context_geo_button.click()
    print("Геометка")
    time.sleep(3)
    # Поиск по сайту
    search_button = driver.find_element(By.XPATH, locators.SEARCH_BUTTON)
    search_button.click()
    print("Клик по кпопке поиска (лупа)")
    search_field = driver.find_element(By.XPATH, locators.SEARCH_FIELD)
    search_field.send_keys("Кредит")
    print("Ввели Кредит")
    button_submit = driver.find_element(By.XPATH, locators.BUTTON_SUBMIT)
    button_submit.click()
    print("Подтвердили поиск")
    time.sleep(5)

    # Негативный сценарий

    text_search_field = driver.find_element(By.XPATH, locators.TEXT_SEARCH_FIELD)
    # Очистить поисковое поле
    text_search_field.clear()
    # Ввести несуществующее значение
    text_search_field.send_keys("1234567890")
    print("Ввели 1234567890")
    # Нажать на кнопку поиск
    text_button_submit = driver.find_element(By.XPATH, locators.TEXT_BUTTON_SUBMIT)
    text_button_submit.click()
    print("Подтвердили поиск")
    time.sleep(5)

    # Закрытие строки поиска

    # Нажать на кнопку поиск
    search_field = driver.find_element(By.XPATH, locators.SEARCH_FIELD)
    search_field.click()
    print("Нажали на кнопку поиск по сайту")
    # Закрыть кнопку поиск
    reset_button = driver.find_element(By.XPATH, locators.RESET_BUTTON)
    reset_button.click()
    print("Нажали на кнопку закрыть поиск по сайту")

    time.sleep(5)

def test_actions_chains():
    driver = webdriver.Chrome()
    # webdriver.ChromeOptions().add_argument('ignore-certificate-errors')
    driver.implicitly_wait(10)
    driver.get("https://www.sberbank.ru")
    driver.maximize_window()
    time.sleep(3)


    # Чтение геометки
    context_geo_button = driver.find_element(By.XPATH, locators.CONTEXT_GEO_BUTTON)
    context_geo_button.click()
    print("Геометка")
    time.sleep(3)

    # Наведение курсора мыши на Курсы Валют
    exchange_rates_button = driver.find_element(By.XPATH, locators.CONTEXT_GEO_BUTTON)
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
