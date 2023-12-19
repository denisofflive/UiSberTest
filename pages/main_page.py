from pages.base_page import BasePage
from pages.locators import MainPageLocators
from selenium.webdriver.common.by import By
from Steps import support_steps as support_steps
from selenium.webdriver.common.action_chains import ActionChains


class MainPage(BasePage):

    # Нажать на вкладку Курсы валют
    def click_on_exchange_rates_link(self):
        button = self.driver.find_element(*MainPageLocators.EXCHANGE_RATES_LINK)
        button.click()
        print("Нажать на вкладку Курсы валют")

    # Нажать на вкладку Офисы
    def click_on_offices_link(self):
        button = self.driver.find_element(*MainPageLocators.OFFICES_BUTTON)
        button.click()
        print("Нажать на вкладку Офисы")

    # Нажать на вкладку Банкоматы
    def click_on_atms_link(self):
        button = self.driver.find_element(*MainPageLocators.ATMS_BUTTON)
        button.click()
        print("Нажать на вкладку Банкоматы")

    # Подсчет всех элементов (поэтому find_elementS) на странице - Курсы валют
    def exchange_rates_count(self):
        exchange_rates_count = self.driver.find_elements(*MainPageLocators.EXCHANGE_RATES_LINK_ALL)
        print("Количество элементов Курсы валют =", len(exchange_rates_count))

    # Подсчет всех элементов (поэтому find_elementS) на странице - Офисы
    def offices_count(self):
        offices_count = self.driver.find_elements(*MainPageLocators.OFFICES_COUNT)
        print("Количество элементов Офисы =", len(offices_count))

    # Подсчет всех элементов (поэтому find_elementS) на странице - Банкоматы
    def atms_count(self):
        atms_count = self.driver.find_elements(*MainPageLocators.ATMS_COUNT)
        print("Количество элементов Банкоматы =", len(atms_count))

    def geoposition(self):
        self.driver.find_element(*MainPageLocators.GEOPOSITION_LINK)
        print("Геометка")

    # Нажать на геопозицию
    def click_on_geoposition_link(self):
        geo_button = self.driver.find_element(*MainPageLocators.GEOPOSITION_LINK)
        print("Регион:", geo_button.text)
        geo_button.click()

    # Ввести регион Ростовская область
    def fill_rostov_region_name(self):
        region_name_field = self.driver.find_element(*MainPageLocators.REGION_NAME_FIELD)
        region_name_field.send_keys("Ростовская область")

        # Ввести регион Ленинградская область
    def fill_leningrad_region_name(self):
        region_name_field = self.driver.find_element(*MainPageLocators.REGION_NAME_FIELD)
        region_name_field.send_keys("Ленинградская область")

    # Выбрать регион(ы) из text и кликнуть по региону(ам)
    def click_on_region_names_link(self, text):
        link = self.driver.find_element(By.XPATH, "//button[text()[contains(.,'" + text.title() + "')]]")
        link.click()

    # Нажать на Ростовскую область
    def click_on_rostov_region_field(self):
        rostov_region_field = self.driver.find_element(*MainPageLocators.ROSTOV_REGION_FIELD)
        rostov_region_field.click()
        print("Ростовская область")

    # Нажать на Ленинградскую область
    def click_on_leningrad_region_field(self):
        leningrad_region_field = self.driver.find_element(*MainPageLocators.LENINGRAD_REGION_FIELD)
        leningrad_region_field.click()
        print("Ростовская область")

    # Выбрать английский язык
    def click_on_eng_language(self):
        eng_language = self.driver.find_element(*MainPageLocators.ENG_LANGUAGE)
        eng_language.click()
        print("Eng language")

    # Нажать на кнопку поиска
    def click_on_search_button(self):
        search_button = self.driver.find_element(*MainPageLocators.SEARCH_BUTTON)
        search_button.click()
        print("Клик по кпопке поиска (лупа)")

    # Заполнить поле поиска и ввести кредит
    def fill_search_field(self):
        search_field = self.driver.find_element(*MainPageLocators.SEARCH_FIELD)
        search_field.send_keys("Кредит")
        print("Ввели Кредит")

    # Нажать и подтвердить кнопку поиска
    def click_on_button_submit(self):
        button_submit = self.driver.find_element(*MainPageLocators.BUTTON_SUBMIT)
        button_submit.click()
        print("Подтвердили поиск")

    # Очистить поисковое поле
    def clear_text_search_field(self):
        text_search_field = self.driver.find_element(*MainPageLocators.TEXT_SEARCH_FIELD)
        text_search_field.clear()

    # Заполнить поле поиска рандомными буквами
    def fill_random_text_search_field(self):
        fill_random_text_search_field = self.driver.find_element(*MainPageLocators.TEXT_SEARCH_FIELD).send_keys(
            support_steps.generate_random_letter_strings(5))
        print(fill_random_text_search_field)

    # Нажать на поле поиск по сайту
    def click_on_search_field(self):
        search_field = self.driver.find_element(*MainPageLocators.SEARCH_FIELD)
        search_field.click()
        print("Нажали на кнопку поиск по сайту")

    # Нажать и закрыть кнопку поиск
    def click_on_reset_button(self):
        reset_button = self.driver.find_element(*MainPageLocators.RESET_BUTTON)
        reset_button.click()
        print("Нажали на кнопку закрыть поиск по сайту")

    # Нажать на кнопку поиск и подтвердить
    def text_button_submit(self):
        text_button_submit = self.driver.find_element(*MainPageLocators.TEXT_BUTTON_SUBMIT)
        text_button_submit.click()
        print("Подтвердили поиск")

    # Заполняем регион(ы) текстом
    def fill_text_region_name_field(self, text):
        self.driver.find_element(*MainPageLocators.REGION_NAME_FIELD).send_keys(text)
        print(text)

    # Заполняем регион рандомным (некорректным) текстом
    def fill_incorrect_region_name_field(self):
        self.driver.find_element(*MainPageLocators.REGION_NAME_FIELD).send_keys(
            support_steps.generate_random_letter_strings(5))

    # Вкладка Сбербанк Онлайн
    def sberonline_button(self):
        self.driver.find_element(*MainPageLocators.SBERBANK_ONLINE_BUTTON)

    # Нажать на Сбербанк Онлайн
    def click_on_sberonline_button(self):
        sberonline_button = self.driver.find_element(*MainPageLocators.SBERBANK_ONLINE_BUTTON)
        sberonline_button.click()
        print("СберБанк Онлайн")

    # Заголовок Курсы валют
    def first_page_title_exchange_rates(self):
        self.driver.find_elements(*MainPageLocators.FIRST_PAGE_TITLE_EXCHANGE_RATES)
        print("Курсы валют")

    # Наведение курсора мыши на Курсы Валют
    def actionChains_exchange_rates_button(self):
        exchange_rates_button = self.driver.find_element(*MainPageLocators.EXCHANGE_RATES_LINK)
        ActionChains(self.driver).move_to_element(exchange_rates_button).perform()
        print("Цвет кнопки Курсы Валют изменился")

    # Наведение курсора мыши на Офисы
    def actionChains_offices_button(self):
        offices_button = self.driver.find_element(*MainPageLocators.OFFICES_BUTTON)
        ActionChains(self.driver).move_to_element(offices_button).perform()
        print("Цвет кнопки Офисы изменился")

    # Наведение курсора мыши на Банкоматы
    def actionChains_atms_button(self):
        atms_button = self.driver.find_element(*MainPageLocators.ATMS_BUTTON)
        ActionChains(self.driver).move_to_element(atms_button).perform()
        print("Цвет кнопки Банкоматы изменился")

    # Наведение курсора мыши на Геопозиция
    def actionChains_geoposition_button(self):
        geoposition_button = self.driver.find_element(*MainPageLocators.GEOPOSITION_LINK)
        ActionChains(self.driver).move_to_element(geoposition_button).perform()
        print("Цвет кнопки Геопозиция изменился")

    # Наведение курсора мыши на Смена языка
    def actionChains_change_language_button(self):
        change_language_button = self.driver.find_element(*MainPageLocators.ENG_LANGUAGE)
        ActionChains(self.driver).move_to_element(change_language_button).perform()
        print("Цвет кнопки Смена языка изменился")

    # Наведение курсора мыши на Поиск
    def actionChains_search_button(self):
        search_button = self.driver.find_element(*MainPageLocators.SEARCH_BUTTON)
        ActionChains(self.driver).move_to_element(search_button).perform()
        print("Цвет кнопки Смена языка изменился")
