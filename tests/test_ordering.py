import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage
from helpers import get_ordering_test_data


class TestOrdering:
    @allure.title('Тестируем заказ самоката через верхнюю кнопку Заказать и первым набором данных')
    def test_order_upper_button(self, driver):
        test_data = get_ordering_test_data()
        main_page = MainPage(driver)
        main_page.click_order_header()
        order_page = OrderPage(driver)
        assert order_page.order(test_data)

    @allure.title('Тестируем заказ самоката через нижнюю кнопку Заказать и вторым набором данных')
    def test_order_below_button(self, driver):
        test_data = get_ordering_test_data()
        main_page = MainPage(driver)
        main_page.click_order_below()
        order_page = OrderPage(driver)
        assert order_page.order(test_data)
