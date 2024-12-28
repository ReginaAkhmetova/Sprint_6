import pytest
from selenium import webdriver

URL_INDEX = 'https://qa-scooter.praktikum-services.ru/'

@pytest.fixture
def driver():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--window-size=1500,1000')
    driver = webdriver.Firefox(firefox_options)
    driver.get(URL_INDEX)
    yield driver
    driver.quit()
