import pytest
from selenium import webdriver

from urls import MAINPAGE_URL


@pytest.fixture
def driver():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--window-size=1500,1000')
    driver = webdriver.Firefox(firefox_options)
    driver.get(MAINPAGE_URL)
    yield driver
    driver.quit()
