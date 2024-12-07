import pytest
from selenium import webdriver

# Фикстура для создания и настройки браузера
# Данная фикстура будет запускаться один раз для каждого класса
@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")  # Сообщение перед запуском браузера
    browser = webdriver.Chrome()  # Запускаем браузер Chrome
    yield browser  # Передаем объект браузера тестам
    print("\nquit browser..")  # Сообщение перед закрытием браузера
    browser.quit()  # Закрываем браузер после выполнения тестов

# Функция для добавления пользовательской опции командной строки
# Эта функция добавляет возможность выбора языка через параметр командной строки
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",  # Параметр командной строки для выбора языка
                     help="Choose language: ru, hu")  # Описание параметра

# Фикстура для получения выбранного языка из командной строки
# Данная фикстура выполняется для каждого теста
@pytest.fixture(scope="function")
def language(request):
    language = request.config.getoption("--language")  # Получаем значение параметра 'language' из командной строки
    yield language  # Передаем выбранный язык тестам
import pytest
