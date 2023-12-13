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


# # Фикстура для запуска браузера Mozilla Firefox
# @pytest.fixture(scope="session")
# def browser():
#     try:
#         # Инициализируем браузер
#         driver = webdriver.Firefox()
#         yield driver
#     finally:
# # Закрытие браузера
#         driver.quit()

# # Фикстура для запуска браузера Microsoft Egde
# @pytest.fixture(scope="session")
# def browser():
#     try:
#         # Инициализируем браузер
#         driver = webdriver.Edge()
#         yield driver
#     finally:
# # Закрытие браузера
#         driver.quit()
