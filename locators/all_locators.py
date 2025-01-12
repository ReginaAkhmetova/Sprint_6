from selenium.webdriver.common.by import By


class GeneralLocators:
    """ Локаторы элементов, которые присутствуют на всех страницах сайта. На сайте есть элементы, которые
    присутствуют на всех страницах и лоцируются одним и тем же локатором - я их выделила в отдельный
    класс локаторов, который можно использовать генерализировано путем наследования от него остальных
    классов локаторов.
    """
    LOGO_YANDEX = (By.XPATH, ".//*[@alt='Yandex']")  # логотип Яндекса
    LOGO_SCOOTER = (By.XPATH, ".//*[@alt='Scooter']")  # логотип Самокат


class MainPageLocators(GeneralLocators):
    """ Локаторы заглавной страницы """
    TITLE = (By.XPATH, "//div[starts-with(@class, 'Home_Header__')]")
    BUTTON_COOCKIE = (By.XPATH, "//button[text()='да все привыкли']")
    QUESTIONS = (By.CLASS_NAME, "accordion")  #  Вопросы о важном
    QUESTION = (
        By.XPATH,
        "//div[starts-with(@class, 'Home_FAQ__')]//div[@class='accordion__item'][{}]//div[@class='accordion__button']"
    )
    ANSWER = (
        By.XPATH,
        "//div[starts-with(@class, 'Home_FAQ__')]//div[@class='accordion__item'][{}]//div[@class='accordion__panel']"
    )

    ORDER_BUTTON_HEADER = (By.XPATH, "(//button[text()='Заказать'])[1]")  # кнопка заказать вверху главной страницы
    ORDER_BUTTON_BELOW = (By.XPATH, "(//button[text()='Заказать'])[2]")  # кнопка заказать в блоке Как это работает
    SCROLL_MIDDLE_BUTTON = (By.CLASS_NAME, 'Home_FinishButton__1cWm')

    @classmethod
    def question_locator(cls, index):
        """ Эта функция принимает на вход индекс вопроса - от 1 до 8, и возвращает
        локатор, который берется из шаблона QUESTION, где вместо {} метод .format()
        подставит переданный индекс.
        """
        by, loc = cls.QUESTION
        return by, loc.format(index)

    @classmethod
    def answer_locator(cls, index):
        """ Эта функция принимает на вход индекс ответа - от 1 до 8, и возвращает
        локатор, который берется из шаблона ANSWER, где вместо {} метод .format()
        подставит переданный индекс.
        """
        by, loc = cls.ANSWER
        return by, loc.format(index)


class OrderLocators(GeneralLocators):
    """ Локаторы страницы заказа самоката. Так как данная страница имеет две формы, вторая из которых
    недоступна, пока не пройдена первая форма - локаторы каждой из них я выделила в отдельный
    подкласс.
    """

    # этот атрибут оставляет на уровне этого класса, так как в классах страниц есть метод,
    # который проверяет, что страница открылась, ища элемент по именно этому локатору
    TITLE = (By.XPATH, "//div[text()='Для кого самокат']")

    class FirstForm:
        """ Локаторы первой формы """
        # локаторы первого раздела "для кого самокат"
        TITLE = (By.XPATH, "//div[text()='Для кого самокат']")
        BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']")
        # форма первого раздела
        FORM_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
        FORM_SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
        FORM_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
        FORM_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")
        FORM_STATION_CLICK = (By.CLASS_NAME, "select-search__select")
        FORM_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

    class SecondForm:
        """ Локаторы второй формы """
        # локаторы второго раздела после нажатия "далее"
        TITLE = (By.XPATH, "//div[text()='Про аренду']")
        BUTTON_NEXT = (By.XPATH, "//div[starts-with(@class, 'Order_Buttons__')]/button[text()='Заказать']")
        # форма второго раздела
        FORM_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
        FORM_PERIOD = (
            By.XPATH,
            "//div[@class='Dropdown-placeholder' and text()='* Срок аренды']/parent::*//span[@class='Dropdown-arrow']"
        )
        FORM_PERIOD_OPTION = (
            By.XPATH,
            "//div[@class='Dropdown-placeholder' and text()='* Срок аренды']/parent::*"
            "/parent::*//div[@class='Dropdown-option' and text()='{}']"
        )
        FORM_COLOR = (By.XPATH, "//label[@for='{}']")
        FORM_COLOR_BLACK = (By.XPATH, "//label[@for='black']")
        FORM_COLOR_GREY = (By.XPATH, "//label[@for='grey']")
        FORM_COMMENT = (By.XPATH, ".//*[@placeholder='Комментарий для курьера']")

    class PopupModal:
        """ Локаторы элементов модального окна подтверждения заказа """
        # локаторы модального поп-апа
        TITLE = (By.XPATH, "//div[starts-with(@class, 'Order_ModalHeader__') and text()='Хотите оформить заказ?']")
        POPUP_STATUS = (By.XPATH, "//div[text()='Заказ оформлен']")
        BUTTON_YES = (By.XPATH, "//button[text()='Да']")
        BUTTON_STATUS = (By.XPATH, "//button[text()='Посмотреть статус']")
