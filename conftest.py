import pytest
from selenium import webdriver


# Фикстура для запуска браузера Google Chrome
@pytest.fixture(scope="session")
def browser():
    try:
        # Инициализируем браузер
        driver = webdriver.Chrome()
        yield driver
    finally:
        # Закрытие браузера
        driver.quit()
