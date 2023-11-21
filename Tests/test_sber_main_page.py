import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def test_open_sber_main_page():
    driver = webdriver.Chrome()
    webdriver.ChromeOptions().add_argument('ignore-certificate-errors')
    driver.implicitly_wait(10)
    driver.get("http://www.sberbank.ru/")
    driver.maximize_window()

    # Геометка
    driver.find_element(By.XPATH, "//a[@title='Изменить регион']")
    print("Геометка")

    # Подсчет элементов на странице у курсов валют
    exchange_rates_count = driver.find_elements(By.XPATH, "//a[text()='Курсы валют']")
    print("count exchange =", len(exchange_rates_count))


    # # Переключение языка "ENG"
    # driver.find_element(By.XPATH, "(//a[text()='ENG'])[1]")
    # print("ENG")
    # # Меню "поиск-лупа"
    # driver.find_element(By.XPATH, "//a[@aria-label='Открыть поиск по сайту']")
    # print("поиск-лупа")
    # # Кнопка Сбербанк-онлайн
    # sberonline_button = driver.find_element(By.XPATH, "//a[text()='СберБанк Онлайн']")
    # sberonline_button.click()
    # print("СберБанк Онлайн")
    # time.sleep(3)
    #
    # # Переключение между вкладками
    # driver.switch_to.window(driver.window_handles[0])
    # print("Главная страница Сбера")

    # # Наведение курсора мыши на СберБанк Онлайн
    # sberonline_button = driver.find_element(By.XPATH, "//a[text()='СберБанк Онлайн']")
    # ActionChains(driver).move_to_element(sberonline_button).perform()
    # print("Цвет кнопки изменился")

    # geo_buton = driver.find_element(By.XPATH, "//a[@title='Изменить регион']")
    # print("geo_button_text", geo_buton.text)
    # geo_buton.click()
    # region_name_field = driver.find_element(By.XPATH, "//input[@aria-label='Введите имя региона']")
    # region_name_field.send_keys("Какая-то область")
    # region_name_field.clear()
    # time.sleep(3)
    # region_name_field.send_keys("Ростовская область")
    # region_name_button = driver.find_element(By.XPATH, "//button[text()='Ростовская область']")
    # region_name_button.click()

    # # Скролл вниз
    # driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)

    time.sleep(3)
