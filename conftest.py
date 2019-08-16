from browser_manager import BrowserManager
import pytest
from selenium import webdriver

browser = BrowserManager()
# ch = browser.get_chrome_browser()
# ff = browser.get_mozilla_browser()
#
# chrome = [ch]
# firefox = [ff]


# all_browsers = chrome + firefox

def pytest_addoption(parser):
    parser.addoption("--chrome", action="store_true",
                     help="chrome")
    parser.addoption("--firefox", action="store_true"),
    parser.addoption("--allbrowsers", action="store_true"),


def pytest_generate_tests(metafunc):
    if 'param1' in metafunc.fixturenames:
        if metafunc.config.getoption('chrome'):
            metafunc.parametrize("param1", [browser.get_chrome_browser()])
        elif metafunc.config.getoption('firefox'):
            metafunc.parametrize("param1", [browser.get_mozilla_browser()])
        elif metafunc.config.getoption('allbrowsers'):
            metafunc.parametrize("param1", [browser.get_chrome_browser(),
                                            browser.get_mozilla_browser()])

@pytest.fixture
def driver(param1):
    """Create driver object"""
    driver = param1
    yield driver
    driver.quit()




