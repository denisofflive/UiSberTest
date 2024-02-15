import pytest
from selenium import webdriver


# Описываем дополнительные опции командой строки
# --bro - браузер, на котором будет выполняться тестирование

def pytest_addoption(parser):
    parser.addoption("--bro",
                     action="store",
                     default="Chtome",
                     help="available browsers: Edge, Firefox, Chrome",
                     choices=("Edge", "Firefox", "Chrome")
                     )

# Фикстура браузера
@pytest.fixture(autouse=True, scope="session")
def bro(pytestconfig):
    bro = pytestconfig.getoption("bro")
    yield bro

# Фикстура для запуска браузера Google Chrome
@pytest.fixture(scope="session")
def browser(bro):
    try:
        # Инициализируем браузер
        if bro == "Chrome":
            driver = webdriver.Chrome()
        elif bro == "Firefox":
            driver = webdriver.Firefox()
        elif bro == "Edge":
            driver = webdriver.Edge()
        else:
            raise ValueError("Invalid browser name")
        yield driver
    finally:
        # Закрытие браузера
        driver.quit()
