import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages import locators as locators

# Тест - скролл по странице
def test_scroll_page():
    driver = webdriver.Chrome()
    webdriver.ChromeOptions().add_argument('ignore-certificate-errors')
    driver.implicitly_wait(10)
    driver.get("http://www.sberbank.ru/")
    driver.maximize_window()

    # Геометка
    driver.find_element(By.XPATH, locators.GEOPOSITION_LINK)
    print("Геометка")
    # Скролл на один экран вниз
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(3)
    # Скролл прокрутка до футера
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(3)
    # Скролл на один экран вверх
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_UP)
    time.sleep(3)
    # Скролл на вверх к хедеру
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.HOME)
    time.sleep(3)


# Тест - переключение между вкладками
def test_switch_page():
    driver = webdriver.Chrome()
    webdriver.ChromeOptions().add_argument('ignore-certificate-errors')
    driver.implicitly_wait(10)
    driver.get("http://www.sberbank.ru/")
    driver.maximize_window()

    # Геометка
    driver.find_element(By.XPATH, locators.GEOPOSITION_LINK)
    print("Геометка")

    # Кнопка Сбербанк-онлайн
    sberonline_button = driver.find_element(By.XPATH, locators.SBERBANK_ONLINE_BUTTON)
    sberonline_button.click()
    print("СберБанк Онлайн")
    time.sleep(3)

    # Переключение между вкладками (переход на главную страницу Сбера)
    driver.switch_to.window(driver.window_handles[0])
    print("Главная страница Сбера")
    time.sleep(3)

    exchange_rates_button = driver.find_element(By.XPATH, locators.EXCHANGE_RATES_LINK)
    exchange_rates_button.click()
    print("Курсы валют")
    time.sleep(3)

    # Переключение между вкладками (переход на страницу СберБанк Онлайн)
    driver.switch_to.window(driver.window_handles[1])
    print("Страница СберБанк Онлайн")
    time.sleep(3)
