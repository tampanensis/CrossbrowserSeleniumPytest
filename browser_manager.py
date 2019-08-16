from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions


class BrowserManager:

    def get_chrome_browser(self):
        options = ChromeOptions()
        options.add_argument("no-sandbox")
        options.accept_untrusted_certs = True
        options.assume_untrusted_cert_issuer = True
        options.add_argument("--disable-infobars")
        options.add_argument("--headless")
        driver_ = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        return driver_

    def get_mozilla_browser(self):
        options = FirefoxOptions()
        options.add_argument("no-sandbox")
        options.accept_untrusted_certs = True
        options.assume_untrusted_cert_issuer = True
        options.add_argument("--disable-infobars")
        options.add_argument("--headless")
        driver_ = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
        return driver_
