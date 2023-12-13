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

    # Проверка, что цвет до и после наведения мыши не равны
    def assert_colors_not_equal(self):
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

    # Проверка количества элементов у курсов валют
    def assert_exchange_rates_count(self):
        assert len(self.driver.find_elements(*MainPageLocators.EXCHANGE_RATES_LINK_ALL)) == 4
        print("Верно")

    # Проверка страницы Курсы валют
    def assert_exchange_rates_title(self):
        assert self.driver.find_element(
            *MainPageLocators.FIRST_PAGE_TITLE_EXCHANGE_RATES).text == "Курсы валют"

    # Проверка некорректного заголовка Курсы валют
    def assert_incorrect_title__exchange_rates_title(self):
        assert self.driver.find_element(
            *MainPageLocators.FIRST_PAGE_TITLE_EXCHANGE_RATES).text != "Курсы валют1"
        print("Негативный тест пройден")

    # Проверка имени региона
    def assert_region_name_in_geo_link(self, text):
        assert self.driver.find_element(*MainPageLocators.GEOPOSITION_LINK).text.__contains__(
            text.title()), "Регион в гео не найден"
        print(text)

    # Проверка несуществующего элемента (региона)
    def should_not_be_success_region_button(self):
        assert self.is_not_element_present(*MainPageLocators.SEARCH_SUCCESS_REGION_BUTTON)
