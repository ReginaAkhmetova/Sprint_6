import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage
from const import DZEN_URL

class TestLogo:

    @allure.title('Тест нажатия на логотип самокат')
    def test_logo_scooter(self, driver):
        order_page = OrderPage(driver)
        order_page.open()
        order_page.click_scooter_logo()
        main_page = MainPage(driver)
        main_page.wait_page_to_be_open()

    @allure.title('Тест нажатия на логотип Яндекса')
    def test_logo_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_yandex_logo()
        main_page.switch_tab()
        main_page.wait_for_url(DZEN_URL)
