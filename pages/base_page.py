from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Класс базовой страницы
class BasePage():
    # driver - текущий драйвер браузера
    # url - передаваемый url
    # timeout - таймаут ожидания элемента, по умолчанию 10 секунд
    def __init__(self, driver, url, timeout=15):
        self.driver = driver
        self.url = url
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(timeout)

        # всегда разворачиваем окно на полный экран
        self.driver.maximize_window()

    # Открыть ссылку
    def open(self):
        self.driver.get(self.url)
        print("Открыть главную страницу")



    # Функция выставляет параметры для проверки существования объекта
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    # Получение ссыпки страницы, на которой находимся
    def get_link(self):
        return self.driver.current_url
