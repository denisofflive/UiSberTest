import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Тест с проверкой корректного перехода по ссылкам меню "Курсы валют, "Офисы", "Банкоматы"
def test_moving_menu_links():
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
    assert first_page_title.text == "Курсы валют"
    print("Курсы валют")
    # Переключение между вкладками (главная страница)
    driver.switch_to.window(driver.window_handles[0])
    print("Переключение на вкладку Главная страница")
    time.sleep(3)

    # Нажать на вкладку Офисы
    offices_button = driver.find_element(By.XPATH, "(//a[text()='Офисы'])[2]")
    offices_button.click()
    print("Нажать на вкладку Офисы")
    time.sleep(5)
    # Проверка страницы Офисы
    offices_page_title = driver.find_element(By.XPATH, "//span[text()='Офисы и банкоматы']")
    assert offices_page_title.text == "Офисы и банкоматы"
    print("Офисы и банкоматы")
    time.sleep(5)
    # Вернуться назад (на главную страницу)
    driver.back()

    # Нажать на вкладку Банкоматы
    atms_button = driver.find_element(By.XPATH, "(//a[text()='Банкоматы'])[2]")
    atms_button.click()
    print("Нажать на вкладку Банкоматы")
    time.sleep(5)
    # Проверка страницы Банкоматы
    atms_button_page_title = driver.find_element(By.XPATH, "//span[text()='Офисы и банкоматы']")
    assert atms_button_page_title.text == "Офисы и банкоматы"
    print("Офисы и банкоматы")
    # Вернуться назад (на главную страницу)
    driver.back()
    time.sleep(5)

# Тест с проверкой корректного перехода по ссылке меню "СберБанк Онлайн"
def test_moving_menu_sberonline_link():
    driver = webdriver.Chrome()
    webdriver.ChromeOptions().add_argument('ignore-certificate-errors')
    driver.implicitly_wait(10)
    driver.get("http://www.sberbank.ru/")
    driver.maximize_window()

    # Геометка
    driver.find_element(By.XPATH, "//a[@title='Изменить регион']")
    print("Геометка")
    # Нажать на вкладку СберБанк Онлайн
    sberonline_button = driver.find_element(By.XPATH, "//a[text()='СберБанк Онлайн']")
    sberonline_button.click()
    print("Нажать на вкладку СберБанк Онлайн")
    time.sleep(3)
    # Переключение между вкладками
    driver.switch_to.window(driver.window_handles[1])
    print("Переключение на вкладку СберБанк Онлайн")
    time.sleep(3)
    # Проверка страницы СберБанк
    sberonline_title = driver.find_element(By.XPATH, "//h1[text()='СберБанк']")
    assert sberonline_title.text == "СберБанк"
    print("СберБанк")
    time.sleep(5)

# Тест с проверкой корректной работы поиска
def test_check_search():
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
    # Ввести имя региона Ленинградская область
    region_name_field = driver.find_element(By.XPATH, "//input[@aria-label='Введите имя региона']")
    region_name_field.send_keys("Ленинградская область")
    # Нажать на кнопку поиска
    region_name_button = driver.find_element(By.XPATH, "//button[text()='Ленинградская область']")
    region_name_button.click()
    time.sleep(3)
    # Проверяем текст выбранный на странице (Ростовская область), что он там есть
    geo_button = driver.find_element(By.XPATH, "//a[@title='Изменить регион']")
    assert geo_button.text == "Ленинградская область"
    print("Ленинградская область")
    time.sleep(3)

# Тест - проверка корректного количества элементов на странице для ссылок "Курсы валют, Офисы, Банкоматы,
# СберБанк Онлайн"
def test_count_links():
    driver = webdriver.Chrome()
    webdriver.ChromeOptions().add_argument('ignore-certificate-errors')
    driver.implicitly_wait(10)
    driver.get("http://www.sberbank.ru/")
    driver.maximize_window()

    # Геометка
    driver.find_element(By.XPATH, "//a[@title='Изменить регион']")
    print("Геометка")

    # Подсчет элементов на странице у Курсов валют
    exchange_rates_count = driver.find_elements(By.XPATH, "//a[text()='Курсы валют']")
    assert len(exchange_rates_count) == 4
    print("Количество элементов на странице у Курсы валют 4")

    # Подсчет элементов на странице у Офисов
    offices_count = driver.find_elements(By.XPATH, "//a[text()='Офисы']")
    assert len(offices_count) == 3
    print("Количество элементов на странице у Офисы 3")

    # Подсчет элементов на странице у Банкоматов
    offices_count = driver.find_elements(By.XPATH, "//a[text()='Банкоматы']")
    assert len(offices_count) == 3
    print("Количество элементов на странице у Бакоматы 3")
    # Подсчет элементов на странице у СберБанк Онлайн
    offices_count = driver.find_elements(By.XPATH, "//a[text()='СберБанк Онлайн']")
    assert len(offices_count) == 1
    print("Количество элементов на странице у СберБанк Онлайн 1")
    time.sleep(3)

# Тест - проверка изменения цвета ссылок "Курсы валют", "Офисы", "Банкоматы", "СберБанк Онлайн"
def test_color_links():
    driver = webdriver.Chrome()
    webdriver.ChromeOptions().add_argument('ignore-certificate-errors')
    driver.implicitly_wait(10)
    driver.get("http://www.sberbank.ru/")
    driver.maximize_window()

    # Геометка
    driver.find_element(By.XPATH, "//a[@title='Изменить регион']")
    print("Геометка")

    # Находим вкладку Курсы валют
    exchange_rates_button = driver.find_element(By.XPATH, "(//a[text()='Курсы валют'])[1]")
    # Цвет до наведения курсора мыши на Курсы валют
    color_before_perform_ex = exchange_rates_button.value_of_css_property('color')
    # Наведение курсора мыши на СберБанк Онлайн
    ActionChains(driver).move_to_element(exchange_rates_button).perform()
    # Цвет после наведения курсора мыши на Курсы валют
    color_after_perform_ex = exchange_rates_button.value_of_css_property('color')
    # Проверяем, что цвет до и после не равны
    assert color_before_perform_ex != color_after_perform_ex
    print("Верно Курсы валют")
    time.sleep(3)

    # Находим вкладку Офисы
    offices_button = driver.find_element(By.XPATH, "(//a[text()='Офисы'])[2]")
    # Цвет до наведения курсора мыши на Офисы
    color_before_perform_o = offices_button.value_of_css_property('color')
    # Наведение курсора мыши на Офисы
    ActionChains(driver).move_to_element(offices_button).perform()
    # Цвет после наведения курсора мыши на Офисы
    color_after_perform_o = offices_button.value_of_css_property('color')
    # Проверяем, что цвет до и после не равны
    assert color_before_perform_o != color_after_perform_o
    print("Верно Офисы")
    time.sleep(3)

    # Находим вкладку Банкоматы
    atms_button = driver.find_element(By.XPATH, "(//a[text()='Банкоматы'])[2]")
    # Цвет до наведения курсора мыши на Банкоматы
    color_before_perform_atms = atms_button.value_of_css_property('color')
    # Наведение курсора мыши на Офисы
    ActionChains(driver).move_to_element(offices_button).perform()
    # Цвет после наведения курсора мыши на Банкоматы
    color_after_perform_atms = offices_button.value_of_css_property('color')
    # Проверяем, что цвет до и после не равны
    assert color_before_perform_atms != color_after_perform_atms
    print("Верно Банкоматы")
    time.sleep(3)

    # Находим вкладку СберБанк Онлайн
    sberonline_button = driver.find_element(By.XPATH, "//a[text()='СберБанк Онлайн']")
    # Цвет до наведения курсора мыши на СберБанк Онлайн
    color_before_perform = sberonline_button.value_of_css_property('color')
    # Наведение курсора мыши на СберБанк Онлайн
    ActionChains(driver).move_to_element(sberonline_button).perform()
    # Цвет после наведения курсора мыши на СберБанк Онлайн
    color_after_perform = sberonline_button.value_of_css_property('color')
    # Проверяем, что цвет до и после не равны
    assert color_before_perform != color_after_perform
    print("Верно СберБанк Онлайн")
    time.sleep(3)

# Тест с проверками корректности заголовков страниц для сценария
def test_check_headers():
    driver = webdriver.Chrome()
    webdriver.ChromeOptions().add_argument('ignore-certificate-errors')
    driver.implicitly_wait(10)
    driver.get("http://www.sberbank.ru/")
    driver.maximize_window()

    # Геометка
    driver.find_element(By.XPATH, "//a[@title='Изменить регион']")
    print("Геометка")

    # Главная страница СберБанк
    sberbank_title = driver.find_element(By.XPATH, "//a[@aria-label='Официальный сайт Сбербанка России']")
    assert sberbank_title.text == ""
    print("Главная страница Сбербанк")
    time.sleep(3)

    # Нажать на вкладку СберБанк Онлайн
    sberonline_button = driver.find_element(By.XPATH, "//a[text()='СберБанк Онлайн']")
    sberonline_button.click()
    print("Нажать на вкладку СберБанк Онлайн")
    time.sleep(3)
    # Переключение между вкладками
    driver.switch_to.window(driver.window_handles[1])
    print("Переключение на вкладку СберБанк Онлайн")
    time.sleep(3)
    # Проверка страницы СберБанк
    sberonline_title = driver.find_element(By.XPATH, "//h1[text()='СберБанк']")
    assert sberonline_title.text == "СберБанк"
    print("СберБанк")
    # Переключение между вкладками
    driver.switch_to.window(driver.window_handles[0])
    print("Переключение на вкладку главная страница")
    time.sleep(3)

    # Главная страница СберБанк
    sberbank_title = driver.find_element(By.XPATH, "//a[@aria-label='Официальный сайт Сбербанка России']")
    assert sberbank_title.text == ""
    print("Главная страница Сбербанк")
    time.sleep(3)
