import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


# Негативный тест - проверка корректного перехода по ссылкам меню
def test_moving_menu_links_negative():
    try:
        driver = webdriver.Chrome()
        webdriver.ChromeOptions().add_argument('ignore-certificate-errors')
        driver.implicitly_wait(10)
        driver.get("http://www.sberbank.ru/")
        driver.maximize_window()

        # Геометка
        driver.find_element(By.XPATH, "//a[@title='Изменить регион']")
        print("Геометка")
        # Нажать на вкладку Курсы валют
        exchange_rates_button = driver.find_element(By.XPATH, "(//a[text()='Курсы валют'])[1]")
        exchange_rates_button.click()
        print("Нажать на вкладку Курсы валют")
        # Переключение между вкладками
        driver.switch_to.window(driver.window_handles[1])
        print("Переключение между вкладками")
        time.sleep(3)
        # Проверка страницы Курсы валют
        first_page_title = driver.find_element(By.XPATH, "(//h1)[1]")
        assert first_page_title.text == "Курсы валют1"
        print("Курсы валют")
        time.sleep(3)
    finally:
        driver.quit()


# Негативный тест - проверка корректного поиска и выбора геопозиции
def test_check_geoposition_negative():
    try:
        driver = webdriver.Chrome()
        webdriver.ChromeOptions().add_argument('ignore-certificate-errors')
        driver.implicitly_wait(10)
        driver.get("http://www.sberbank.ru/")
        driver.maximize_window()

        # Геометка
        driver.find_element(By.XPATH, "//a[@title='Изменить регион']")
        print("Геометка")
        geo_button = driver.find_element(By.XPATH, "//a[@title='Изменить регион']")
        print("geo_button_text", geo_button.text)
        geo_button.click()
        region_name_field = driver.find_element(By.XPATH, "//input[@aria-label='Введите имя региона']")
        region_name_field.send_keys("Ростовская область")
        region_name_button = driver.find_element(By.XPATH, "//button[text()='Ростовская область']")
        region_name_button.click()
        time.sleep(3)
        # Проверяем текст выбранный на странице (Ростовская область), что он там есть
        geo_button = driver.find_element(By.XPATH, "//a[@title='Изменить регион']")
        assert geo_button.text == "Ростовская область1"
        print("Ростовская область")
        time.sleep(3)
    finally:
        driver.quit()
