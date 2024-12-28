import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage
from testdata import get_ordering_test_data


class TestOrdering:

    @classmethod
    def order(cls, driver, test_data):
        order_page = OrderPage(driver)
        order_page.wait_page_to_be_open()

        # заполняем первую форму
        order_page.fill_first_form(
            name=test_data['name'],
            surname=test_data['surname'],
            address=test_data['address'],
            station=test_data['station'],
            phone=test_data['phone']
        )
        order_page.submit_first_form()

        # ожидаем, пока сменится раздел на второй
        order_page.wait_for_second_form()

        # заполняем вторую форму
        order_page.fill_second_form(
            date=test_data['date'],
            period=test_data['period'],
            color=test_data['color'],
            comment=test_data['comment']
        )
        order_page.submit_second_form()

        # ожидаем модальное окно подтверждения
        order_page.wait_for_modal_popup()

        # нажимаем "да"
        order_page.click_modal_yes()

        # ждем, что появится информация об оформленном заказе
        order_page.wait_for_ordered()

    @allure.title('Тестируем заказ самоката через верхнюю кнопку Заказать и первым набором данных')
    def test_order_upper_button(self, driver):
        test_data = get_ordering_test_data()
        main_page = MainPage(driver)
        main_page.click_order_header()
        self.order(driver, test_data)

    @allure.title('Тестируем заказ самоката через нижнюю кнопку Заказать и вторым набором данных')
    def test_order_below_button(self, driver):
        test_data = get_ordering_test_data()
        main_page = MainPage(driver)
        main_page.click_order_below()
        self.order(driver, test_data)
