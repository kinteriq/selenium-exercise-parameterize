# Добавьте в файл conftest.py обработчик, который считывает из командной строки параметр language.

# Реализуйте в файле conftest.py логику запуска браузера с указанным языком пользователя.
# Браузер должен объявляться в фикстуре browser и передаваться в тест как параметр.

# Тест должен запускаться с параметром language следующей командой:
#       pytest --language=es test_items.py
# и проходить успешно. Достаточно, чтобы код работал только для браузера Сhrome.

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# PATH_TO_CHROME = r'/Users/kinteriq/drivers/chromedriver'


def pytest_addoption(parser):
    parser.addoption('--language', action='store',
                     default='es', help='Choose language.')


@pytest.fixture(scope='function')
def browser(request):
    lang = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': lang})
    # browser = webdriver.Chrome(PATH_TO_CHROME, options=options)
    browser = webdriver.Chrome(options=options)
    print(f'Start browser: language={lang}.')
    yield browser
    print(f'Quit browser; language={lang}.')
    browser.quit()