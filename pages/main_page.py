import allure

from locators.all_locators import MainPageLocators
from pages.base import BasePage
from const import MAINPAGE_URL


class MainPage(MainPageLocators, BasePage):
    """
    Главная страница.

    Мы унаследовались от базового класса страниц для переиспользования методов, единых для
    всех страниц.
    Мы унаследовались от микс-ина локаторов главной страницы, чтобы обращаться к ним как к
    части этого класса, потому что они актуальны только для этой страницы. Это позволяет
    с пользой использовать ООП в этом месте, обращаясь как к `self.LOCATOR_NAME` вместо
    `MainPageLocators.LOCATOR_NAME`.
    """
    URL = MAINPAGE_URL

    @allure.step('Открываем Яндекс Самокат')
    def open(self):
        self.open_site(self.URL)
        self.wait_page_to_be_open()

    @allure.step('Скролим до "Вопросы о важном"')
    def scroll_to_questions_list(self):
        self.scroll_to_element(self.QUESTIONS)
        self.wait_for_visible(self.QUESTIONS)

    @allure.step('Находим вопрос и нажимаем на него')
    def find_question_and_click(self, index):
        q_locator = self.question_locator(index)
        a_locator = self.answer_locator(index)
        self.scroll_to_element(q_locator)
        self.wait_for_visible(q_locator)
        self.click_element(q_locator)
        self.wait_for_visible(a_locator)

    @allure.step('Получаем текст вопроса')
    def get_question_text(self, index):
        q_locator = self.question_locator(index)
        return self.get_text(q_locator)

    @allure.step('Получаем текст ответа')
    def get_answer_text(self, index):
        a_locator = self.answer_locator(index)
        return self.get_text(a_locator)

    @allure.step('Нажимаем кнопку Заказать сверху')
    def click_order_header(self):
        self.click_element(self.ORDER_BUTTON_HEADER)

    @allure.step('Нажимаем кнопку Заказать снизу')
    def click_order_below(self):
        self.scroll_to_element(self.ORDER_BUTTON_BELOW)
        self.click_element(self.ORDER_BUTTON_BELOW)
