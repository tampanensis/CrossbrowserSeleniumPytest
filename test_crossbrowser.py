import pytest


@pytest.mark.usefixtures('driver')
class TestCrossBrowser:

    def test_sample(self, driver):
        driver.get('https://www.google.com.ua/')
        print(driver.title)