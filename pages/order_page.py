import allure

from locators import OrderLocators
from pages.base import BasePage
from const import ORDERPAGE_URL


@allure.step('Заполняем Для кого самокат')
class OrderPage(OrderLocators, BasePage):
    """
    Страница заказа самоката

    Мы унаследовались от базового класса страниц для переиспользования методов, единых для
    всех страниц.
    Мы унаследовались от микс-ина локаторов страницы заказа, чтобы обращаться к ним как к
    части этого класса, потому что они актуальны только для этой страницы. Это позволяет
    с пользой использовать ООП в этом месте, обращаясь как к `self.LOCATOR_NAME` вместо
    `OrderLocators.LOCATOR_NAME`.
    """
    URL = ORDERPAGE_URL

    @allure.step('Открываем страницы заказа')
    def open(self):
        self.open_site(self.URL)
        self.wait_page_to_be_open()

    @allure.step('Заполняем первую форму "Для кого самокат"')
    def fill_first_form(self, name, surname, address, station, phone):
        self.type_in_input(self.FirstForm.FORM_NAME, name)
        self.type_in_input(self.FirstForm.FORM_SURNAME, surname)
        self.type_in_input(self.FirstForm.FORM_ADDRESS, address)
        self.type_in_input(self.FirstForm.FORM_PHONE, phone)
        self.combobox_select(
            self.FirstForm.FORM_STATION,
            self.FirstForm.FORM_STATION_CLICK,
            station,  # например, Лубянка
        )

    @allure.step('Нажмаем кнопку Далее')
    def submit_first_form(self):
        self.click_element(self.FirstForm.BUTTON_NEXT)

    @allure.step('Дожидаемя открытия второй формы для заполнения')
    def wait_for_second_form(self):
        self.wait_for(self.SecondForm.TITLE)

    @allure.step('Заполняем вторую форму "Про аренду"')
    def fill_second_form(self, date, period, color, comment):
        self.type_in_input(self.SecondForm.FORM_DATE, date)
        self.selectbox_select(
            self.SecondForm.FORM_PERIOD,
            self.SecondForm.FORM_PERIOD_OPTION,
            period,
        )
        by, loc = self.SecondForm.FORM_COLOR
        loc = loc.format(color)
        self.click_element((by, loc))
        self.type_in_input(self.SecondForm.FORM_COMMENT, comment)

    @allure.step('Нажимаем кнопку Заказать')
    def submit_second_form(self):
        self.click_element(self.SecondForm.BUTTON_NEXT)

    @allure.step('Ожидаем появления поп-ап окна')
    def wait_for_modal_popup(self):
        self.wait_for(self.PopupModal.TITLE)

    @allure.step('Нажимаем кнопку "Да"')
    def click_modal_yes(self):
        self.click_element(self.PopupModal.BUTTON_YES)

    @allure.step('ожидаем появления окна "Заказ оформлен"')
    def wait_for_ordered(self):
        self.wait_for(self.PopupModal.POPUP_STATUS)


