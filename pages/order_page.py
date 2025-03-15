import allure

from locators import OrderLocators
from pages.base import BasePage
from urls import ORDERPAGE_URL


class OrderPage(BasePage):
    """
    Страница заказа самоката
    """
    url = ORDERPAGE_URL
    locators = OrderLocators
    pageloc = locators.TITLE

    @allure.step('Открываем страницы заказа')
    def open(self):
        self.open_site(self.url)
        self.wait_page_to_be_open()

    @allure.step('Заполняем первую форму "Для кого самокат"')
    def fill_first_form(self, **testdata):
        self.type_in_input(self.locators.FirstForm.FORM_NAME, testdata.get("name"))
        self.type_in_input(self.locators.FirstForm.FORM_SURNAME, testdata.get("surname"))
        self.type_in_input(self.locators.FirstForm.FORM_ADDRESS, testdata.get("address"))
        self.type_in_input(self.locators.FirstForm.FORM_PHONE, testdata.get("phone"))
        self.combobox_select(
            self.locators.FirstForm.FORM_STATION,
            self.locators.FirstForm.FORM_STATION_CLICK,
            testdata.get("station"),  # например, Лубянка
        )

    @allure.step('Нажмаем кнопку Далее')
    def submit_first_form(self):
        self.click_element(self.locators.FirstForm.BUTTON_NEXT)

    @allure.step('Дожидаемя открытия второй формы для заполнения')
    def wait_for_second_form(self):
        self.wait_for(self.locators.SecondForm.TITLE)

    @allure.step('Заполняем вторую форму "Про аренду"')
    def fill_second_form(self, **testdata):
        self.type_in_input(self.locators.SecondForm.FORM_DATE, testdata.get("date"))
        self.selectbox_select(
            self.locators.SecondForm.FORM_PERIOD,
            self.locators.SecondForm.FORM_PERIOD_OPTION,
            testdata.get("period"),
        )
        by, loc = self.locators.SecondForm.FORM_COLOR
        loc = loc.format(testdata.get("color"))
        self.click_element((by, loc))
        self.type_in_input(self.locators.SecondForm.FORM_COMMENT, testdata.get("comment"))

    @allure.step('Нажимаем кнопку Заказать')
    def submit_second_form(self):
        self.click_element(self.locators.SecondForm.BUTTON_NEXT)

    @allure.step('Ожидаем появления поп-ап окна')
    def wait_for_modal_popup(self):
        self.wait_for(self.locators.PopupModal.TITLE)

    @allure.step('Нажимаем кнопку "Да"')
    def click_modal_yes(self):
        self.click_element(self.locators.PopupModal.BUTTON_YES)

    @allure.step('Ожидаем появления окна "Заказ оформлен"')
    def wait_for_ordered(self):
        return self.wait_for(self.locators.PopupModal.POPUP_STATUS)

    @allure.step('Выполняем процедуру заказа')
    def order(self, test_data):
        self.wait_page_to_be_open()

        # заполняем первую форму
        self.fill_first_form(**test_data)
        self.submit_first_form()

        # ожидаем, пока сменится раздел на второй
        self.wait_for_second_form()

        # заполняем вторую форму
        self.fill_second_form(**test_data)
        self.submit_second_form()

        # ожидаем модальное окно подтверждения
        self.wait_for_modal_popup()

        # нажимаем "да"
        self.click_modal_yes()

        # ждем, что появится информация об оформленном заказе
        return self.wait_for_ordered()
