import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_open_sber_main_page():
    driver = webdriver.Chrome()
    webdriver.ChromeOptions().add_argument('ignore-certificate-errors')
    driver.implicitly_wait(10)
    driver.get("http://www.sberbank.ru/")
    driver.maximize_window()

    # Геометка
    driver.find_element(By.XPATH, "//a[@title='Изменить регион']")
    print("Геометка")
    # Переключение языка "ENG"
    driver.find_element(By.XPATH, "(//a[text()='ENG'])[1]")
    print("ENG")
    # Меню "поиск-лупа"
    driver.find_element(By.XPATH, "//a[@aria-label='Открыть поиск по сайту']")
    print("поиск-лупа")
    time.sleep(3)
