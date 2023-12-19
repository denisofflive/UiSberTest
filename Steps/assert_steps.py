from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.locators import MainPageLocators
from selenium.webdriver.common.action_chains import ActionChains

class AssertSteps():
    def __init__(self, driver):
        self.driver = driver

    # Функция выставляет параметры для проверки существования объекта
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    # Функция отображает параметры для ситуации, когда объект не должен отображаться
    def is_not_element_present(self, how, what, timeout=3):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def should_be_exchange_rates_link(self):
        assert self.is_element_present(*MainPageLocators.EXCHANGE_RATES_LINK), "Ссылка 'Курсы валют' отсутствует"

    # Проверка, что цвет до и после наведения мыши на вкладку Сбербанк Онлайн не равны
    def assert_colors_not_equal_by_sber_online(self):
        color_before_perform = self.driver.find_element(
            *MainPageLocators.SBERBANK_ONLINE_BUTTON).value_of_css_property(
            'color')
        ActionChains(self.driver).move_to_element(
            self.driver.find_element(*MainPageLocators.SBERBANK_ONLINE_BUTTON)).perform()
        color_after_perform = self.driver.find_element(
            *MainPageLocators.SBERBANK_ONLINE_BUTTON).value_of_css_property(
            'color')
        assert color_before_perform != color_after_perform
        print("Верно")

    # Проверка, что цвет до и после наведения мыши на вкладку Курсы валют не равны
    def assert_colors_not_equal_by_exchange_rates(self):
        color_before_perform = self.driver.find_element(
            *MainPageLocators.EXCHANGE_RATES_LINK).value_of_css_property(
            'color')
        ActionChains(self.driver).move_to_element(
            self.driver.find_element(*MainPageLocators.EXCHANGE_RATES_LINK)).perform()
        color_after_perform = self.driver.find_element(
            *MainPageLocators.EXCHANGE_RATES_LINK).value_of_css_property(
            'color')
        assert color_before_perform != color_after_perform
        print("Верно")

    # Проверка, что цвет до и после наведения мыши на вкладку Офисы не равны
    def assert_colors_not_equal_by_offices(self):
        color_before_perform = self.driver.find_element(
            *MainPageLocators.OFFICES_BUTTON).value_of_css_property(
            'color')
        ActionChains(self.driver).move_to_element(
            self.driver.find_element(*MainPageLocators.OFFICES_BUTTON)).perform()
        color_after_perform = self.driver.find_element(
            *MainPageLocators.OFFICES_BUTTON).value_of_css_property(
            'color')
        assert color_before_perform != color_after_perform
        print("Верно")

    # Проверка, что цвет до и после наведения мыши на вкладку Офисы валют не равны
    def assert_colors_not_equal_by_atms(self):
        color_before_perform = self.driver.find_element(
            *MainPageLocators.ATMS_BUTTON).value_of_css_property(
            'color')
        ActionChains(self.driver).move_to_element(
            self.driver.find_element(*MainPageLocators.ATMS_BUTTON)).perform()
        color_after_perform = self.driver.find_element(
            *MainPageLocators.ATMS_BUTTON).value_of_css_property(
            'color')
        assert color_before_perform != color_after_perform
        print("Верно")

    # Проверка количества элементов у курсов валют
    def assert_exchange_rates_count(self):
        assert len(self.driver.find_elements(*MainPageLocators.EXCHANGE_RATES_LINK_ALL)) == 4
        print("Количество элементов на странице у Курсы Валют 4")

    # Проверка количества элементов у курсов офисов
    def assert_offices_count(self):
        assert len(self.driver.find_elements(*MainPageLocators.OFFICES_COUNT)) == 3
        print("Количество элементов на странице у Офисы 3")

    # Проверка количества элементов у банкоматов
    def assert_atms_count(self):
        assert len(self.driver.find_elements(*MainPageLocators.ATMS_COUNT)) == 3
        print("Количество элементов на странице у Банкоматы 3")

    # Проверка количества элементов у СберБанк Онлайн
    def assert_sber_online_count(self):
        assert len(self.driver.find_elements(*MainPageLocators.SBERBANK_ONLINE_BUTTON)) == 1
        print("Количество элементов на странице у СберБанк Онлайн 1")

    # Проверка заголовка на странице Курсы валют
    def assert_exchange_rates_title(self):
        assert self.driver.find_element(
            *MainPageLocators.FIRST_PAGE_TITLE_EXCHANGE_RATES).text == "Курсы валют"
        print("Заголовок Курсы Валют")

    # Проверка заголовка на странице Офисы
    def assert_offices_page_title(self):
        assert self.driver.find_element(
            *MainPageLocators.OFFICES_PAGE_TITLE).text == "Офисы и банкоматы"
        print("Офисы и банкоматы")

    # Проверка заголовка на странице Банкоматы
    def assert_atms_page_title(self):
        assert self.driver.find_element(
            *MainPageLocators.ATMS_BUTTON_PAGE_TITLE).text == "Офисы и банкоматы"
        print("Офисы и банкоматы")

    # Проверка страницы СберБанк Онлайн (Правила безопасности)
    def assert_security_regulations_title_on_sber_online(self):
        assert self.driver.find_element(
            *MainPageLocators.SECURITY_REGULATIONS).text == "Правила безопасности"
        print("Правила безопасности")

    # Проверка страницы СберБанк (Лучшие предложения)
    def assert_best_offers_title_on_sber(self):
        assert self.driver.find_element(
            *MainPageLocators.THE_BEST_OFFERS_TITLE).text == "Лучшие предложения"
        print("Лучшие предложения")

    # Проверка геопозиции Ростовская область
    def assert_rostov_geopostion(self):
        assert self.driver.find_element(
            *MainPageLocators.GEOPOSITION_LINK).text == "Ростовская область"
        print("Ростовская область")

    # Проверка геопозиции Ленинградская область
    def assert_leningrad_geopostion(self):
        assert self.driver.find_element(
            *MainPageLocators.GEOPOSITION_LINK).text == "Ленинградская область"
        print("Ленинградская область")

    # Проверка некорректного заголовка Курсы валют
    def assert_incorrect_exchange_rates_title(self):
        assert self.driver.find_element(
            *MainPageLocators.FIRST_PAGE_TITLE_EXCHANGE_RATES).text != "Курсы валют1"
        print("Негативный тест пройден")

    def assert_incorrect_rostov_geoposition(self):
        assert self.driver.find_element(
            *MainPageLocators.ROSTOV_REGION_FIELD).text != "Ростовская область1"
        print("Негативный тест пройден")

    # Проверка имени региона
    def assert_region_name_in_geo_link(self, text):
        assert self.driver.find_element(*MainPageLocators.GEOPOSITION_LINK).text.__contains__(
            text.title()), "Регион в гео не найден"
        print(text)

    # Проверка несуществующего элемента (региона)
    def should_not_be_success_region_button(self):
        assert self.is_not_element_present(*MainPageLocators.SEARCH_SUCCESS_REGION_BUTTON)






