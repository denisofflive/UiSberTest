from pages.base_page import BasePage
from pages.locators import MainPageLocators
from selenium.webdriver.common.by import By
from Steps import support_steps as support_steps
from selenium.webdriver.common.action_chains import ActionChains


class MainPage(BasePage):

    # Нажать на Курсы валют
    def click_on_exchange_rates_link(self):
        button = self.driver.find_element(*MainPageLocators.EXCHANGE_RATES_LINK)
        button.click()
        print("Нажать на вкладку Курсы валют")

    # Подсчет всех элементов (поэтому find_elementS) на странице у курсов валют
    def exchange_rates_count(self):
        exchange_rates_count = self.driver.find_elements(*MainPageLocators.EXCHANGE_RATES_LINK_ALL)
        print("count exchange =", len(exchange_rates_count))

    def geoposition(self):
        self.driver.find_element(*MainPageLocators.GEOPOSITION_LINK)
        print("Геометка")

    # Нажать на геопозицию
    def click_on_geoposition_link(self):
        geo_button = self.driver.find_element(*MainPageLocators.GEOPOSITION_LINK)
        print("Регион:", geo_button.text)
        geo_button.click()

    # Выбрать регион(ы) из text и кликнуть по региону(ам)
    def click_on_region_name_link(self, text):
        link = self.driver.find_element(By.XPATH, "//button[text()[contains(.,'" + text.title() + "')]]")
        link.click()

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
