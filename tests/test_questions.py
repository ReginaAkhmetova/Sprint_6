import allure
import pytest

from pages.main_page import MainPage
from testdata import CHECK_QUESTIONS_LIST_TESTDATA


class TestQuestions:
    @allure.title('Проверка выпадающего списка "Вопросы о важном"')
    @allure.description('Когда нажимаешь на вопрос, открывается соответствующий текст с ответом')
    @pytest.mark.parametrize('question, answer, index', CHECK_QUESTIONS_LIST_TESTDATA)
    def test_check_questions_list(self, driver, question, answer, index):
        main_page = MainPage(driver)
        main_page.scroll_to_questions_list()
        main_page.find_question_and_click(index)
        q_text = main_page.get_question_text(index)
        a_text = main_page.get_answer_text(index)
        assert q_text == question
        assert a_text == answer
