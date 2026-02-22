import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: en, ru, fr, de, es, ja")


@pytest.fixture(scope="function")
def browser(request):
    supported_languages = ['en', 'ru', 'fr', 'de', 'es', 'ja']
    user_language = request.config.getoption("language")
    browser = None
    if user_language in supported_languages:
        print(f"\nstart chrome browser for test in {user_language} language")
        options = Options()

        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)

    else:
        raise pytest.UsageError("--language should be en, ru, fr, de, es, ja")
    yield browser
    print("\nquit browser..")
    browser.quit()