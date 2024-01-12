from pages.locators import MainPageLocators
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Steps.assert_steps import Assert

class MainPage(Assert):
    # функция выполнения поиска
    def search_button_search(self, value):
        search_button = self.driver.find_element(*MainPageLocators.SEARCH_BUTTON)
        search_button.click()
        search = self.driver.find_element(*MainPageLocators.SEARCH_INPUT)
        search.send_keys(value)
        search.send_keys(Keys.ENTER)

    def geoposition(self):
        self.driver.find_element(*MainPageLocators.GEOPOSITION_BUTTON)
        print("Геометка")

    # Наведение на элементы и проверка, что цвет изменился
    def hover_elements(self, element):
        color_before_perform = element.value_of_css_property('color')
        ActionChains(self.driver).move_to_element(element).perform()
        color_after_perform = element.value_of_css_property('color')
        assert color_before_perform != color_after_perform

    # Переход с главной страницы на страницу авторизации
    def jump_to_authorization_page(self):
        return self.driver.find_element(*MainPageLocators.SBERONLINE_BUTTON).click()
