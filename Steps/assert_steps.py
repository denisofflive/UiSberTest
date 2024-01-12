from pages.base_page import BasePage

class Assert(BasePage):
    # Проверка выполнения поиска
    def assert_check_search(self, value, element):
        assert self.driver.find_element(*element).text == value

    # Проверка, что ссылки имеют href отличный от главной страницы
    def assert_correct_link(self, main_url, element):
        assert element.get_attribute('href') != main_url

    # Проверка корректности текста
    def assert_correct_text(self, check_text, number_page, element):
        self.driver.switch_to.window(self.driver.window_handles[number_page])
        assert self.driver.find_element(*element).text == check_text

    # Проверка, что количество ссылок у элемента равно заданному значению
    def assert_number_links(self, element, count):
        assert len(element) == count
