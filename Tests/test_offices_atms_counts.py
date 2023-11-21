import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_offices_atms_counts():
    driver = webdriver.Chrome()
    webdriver.ChromeOptions().add_argument('ignore-certificate-errors')
    driver.implicitly_wait(10)
    driver.get("http://www.sberbank.ru/")
    driver.maximize_window()

    # Геометка
    driver.find_element(By.XPATH, "//a[@title='Изменить регион']")
    print("Геометка")
    # Подсчет элементов на странице у офисов
    offices_count = driver.find_elements(By.XPATH, "//a[text()='Офисы']")
    print("Сount Offices =", len(offices_count))
    time.sleep(3)
    # Подсчет элементов на странице у банкоматов
    atms_count = driver.find_elements(By.XPATH, "//a[text()='Банкоматы']")
    print("Count ATMs =", len(atms_count))
    time.sleep(3)
