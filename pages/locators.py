from selenium.webdriver.common.by import By

class BasePageLocators():
    TAG_H4 = (By.TAG_NAME, "h4")
    TAG_FIRST_H2 = (By.XPATH, "(//h2) [1]")
    TAG_B = (By.TAG_NAME, "b")

class MainPageLocators(BasePageLocators):
    SEARCH_BUTTON = (By.CLASS_NAME, "kitt-header-search")
    SEARCH_BUTTON_HOVER = (By.XPATH, "//a[@class='kitt-header-search']")
    SEARCH_INPUT = (By.CSS_SELECTOR, "[placeholder='Что ищете?']")
    SEARCH_INPUT_VAR = (By.XPATH, "//yass-span / b")
    EXCHANGE_RATES_BUTTON = (By.XPATH, "//a[text()='Курсы валют']")
    OFFICE_BUTTON = (By.XPATH, "(//a[text()='Офисы'])[2]")
    ATMS_BUTTON = (By.XPATH, "(//a[text()='Банкоматы'])[2]")
    GEOPOSITION_BUTTON = (By.XPATH, "//a[@title='Изменить регион']")
    CHANGE_LANGUAGE_BUTTON = (By.XPATH, "(//a[@data-cga_change_lang='en'])[1]")
    SBERONLINE_BUTTON = (By.XPATH, "//a[text()='СберБанк Онлайн']")
    OFFICE_LINK = (By.XPATH, "//a[text()='Офисы']")
    ATMS_LINK = (By.XPATH, "//a[text()='Банкоматы']")

# CTRL + SHIFT + U - менять регистр с большой или маленькой буквы
