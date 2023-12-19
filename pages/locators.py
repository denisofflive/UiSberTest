from selenium.webdriver.common.by import By

main_url = "http://www.sberbank.ru/"

class BasePageLocators():
    # Первый заголовок страницы Курсы валют
    FIRST_PAGE_TITLE_EXCHANGE_RATES = (By.XPATH, "(//h1)[1]")

class MainPageLocators(BasePageLocators):
    # Курсы валют
    EXCHANGE_RATES_LINK = (By.XPATH, "(//a[text()='Курсы валют'])[1]")
    # Все Курсы валют на странице
    EXCHANGE_RATES_LINK_ALL = (By.XPATH, "(//a[text()='Курсы валют'])")
    # Вкладка Сбербанк Онлайн
    SBERBANK_ONLINE_BUTTON = (By.XPATH, "//a[text()='СберБанк Онлайн']")
    # Заголовок Сбербанк России
    SBERBANK_TITLE = (By.XPATH, "//a[@aria-label='Официальный сайт Сбербанка России']")
    # Заголовок Сбербанк Онлайн
    SBERONLINE_TITLE = (By.XPATH, "//h1[text()='СберБанк']")
    # Заголовок Лучшие предложения
    THE_BEST_OFFERS_TITLE = "//span[text()='Лучшие предложения']"
    # Геопозиция
    GEOPOSITION_LINK = (By.XPATH, "//a[@title='Изменить регион']")
    # Поле выбора имени региона
    REGION_NAME_FIELD = (By.XPATH, "//input[@aria-label='Введите имя региона']")
    # Имя региона Ростовская область
    ROSTOV_REGION_FIELD = (By.XPATH, "//button[text()='Ростовская область']")
    # Имя региона Ленинградская область
    LENINGRAD_REGION_FIELD = (By.XPATH, "//button[text()='Ленинградская область']")
    # Вкладка Офисы
    OFFICES_BUTTON = (By.XPATH, "(//a[text()='Офисы'])[2]")
    # Заголовок Офисы
    OFFICES_PAGE_TITLE = (By.XPATH, "//span[text()='Офисы и банкоматы']")
    # Все Офисы на странице
    OFFICES_COUNT = (By.XPATH, "//a[text()='Офисы']")
    # Все Банкоматы на странице
    ATMS_COUNT = (By.XPATH, "//a[text()='Банкоматы']")
    # Вкладка Банкоматы
    ATMS_BUTTON = (By.XPATH, "(//a[text()='Банкоматы'])[2]")
    # Заголовок Офисы и банкоматы
    ATMS_BUTTON_PAGE_TITLE = (By.XPATH, "//span[text()='Офисы и банкоматы']")
    # Заголовок Правила безопасности
    SECURITY_REGULATIONS = (By.XPATH, "//h4[text()='Правила безопасности']")
    # Чтение геометки
    CONTEXT_GEO_BUTTON = (By.XPATH, "(//button[@type='submit'])[1]")
    # Английский язык
    ENG_LANGUAGE = (By.XPATH, "(//a[text()='ENG'])[1]")
    # Кнопка Поиск по сайту
    SEARCH_BUTTON = (By.XPATH, "//a[@aria-label='Открыть поиск по сайту']")
    # Поле поиска
    SEARCH_FIELD = (By.XPATH, "//input[@type='search']")
    # Кнопка подтверждения поиска
    BUTTON_SUBMIT = (By.XPATH, "//button[@class='kitt-header-search__submit']")
    # Кнопка поиска Что-нибудь поищем
    TEXT_SEARCH_FIELD = (By.XPATH, "//input[@placeholder='Что-нибудь поищем']")
    # Кнопка подтверждения Найти
    TEXT_BUTTON_SUBMIT = (By.XPATH, "//input[@value='Найти']")
    # Кнопка сброса
    RESET_BUTTON = (By.XPATH, "//button[@type='reset']")
    SEARCH_SUCCESS_REGION_BUTTON = (By.XPATH, "//button[@class='kitt-header-regiom__region']")

# CTRL + SHIFT + U - менять регистр с большой или маленькой буквы
