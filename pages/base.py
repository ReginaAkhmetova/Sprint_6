import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.all_locators import GeneralLocators


class BasePage:
    """
    Базовый класс всех страниц.

    Так как на сайте присутствуют элементы, которые имеются на всех страницах сайта, то
    методы работы с ними я вынесла в базовый класс, так как эти элементы могут понадобиться
    с любой страницы и имеют одни и те же локаторы.
    """

    """ `url` является сущностью страницы - каждая страница имеет свой однозначный URL, поэтому
    этот атрибут сделан атрибутом класса страницы. Переопределяется дочерним классом на
    фактическое значение. """
    url = ""  # URL будет переопределён классом соответствующей страницы

    """ `pageloc` так же является сущностью определенной страницы. В методе базового класса
    `wait_page_to_be_open` используется этот атрибут для ожидания успешной загрузки страницы
    (или переключения на страницы в случае SPA). Переопределяется дочерним классом на
    фактическое значение. """
    pageloc = None  # уникальный локатор конкретной страницы

    """ Локаторы для класса страницы. Локаторы являются синглтоном, единым для всех
    экземпляров классов, поэтому нет никакого смысла выносить присваивание этого
    синглтона в конструктор или инициализатор экземпляра класса и единственный смысл
    композиции заключается в класс-уровненном назначении (что несет и меньшие накладные
    ресурсные расходы) в этом месте (иными словами, выносить это здесь в __init__ будет 
    вредно). """
    locators = GeneralLocators

    def __init__(self, driver):
        self.driver = driver

    def switch_tab(self):
        """ Переключает вкладку браузера """
        return self.driver.switch_to.window(self.driver.window_handles[-1])

    def open_site(self, url):
        """ Открывает страницу по её адресу (URL) """
        self.driver.get(url)

    def find_element(self, locator):
        """ Ищет элемент на странице по предоставленному локатору """
        return self.driver.find_element(*locator)

    def click_element(self, locator):
        """ Нажимаем на элемент страницы по локатору """
        self.find_element(locator).click()

    def scroll_to_element(self, locator):
        """ Скроллит до переданного элемента на странице, полученного, например,
        через find_element.
        """
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait_for_visible(locator)

    def wait_for(self, locator):
        """ Ожидаем появления на странице указанного элемента """
        return WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(locator))

    def get_text(self, locator):
        """ Возвращает текст внутри элемента """
        return self.find_element(locator).text

    def wait_for_visible(self, locator):
        """ Ожидает, пока элемент станет видимым """
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        """ Ожидает, пока элемент станет кликабельным """
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(locator))

    def wait_for_url(self, url):
        """ Ожидает, пока адрем в строке браузера поменяется на ожидаемый """
        return WebDriverWait(self.driver, 3).until(EC.url_to_be(url))

    def send_keys(self, locator, text):
        """ Печатает текст в элемент страницы (как будто с клавиатуры) """
        self.find_element(locator).send_keys(text)

    def type_in_input(self, locator, text):
        """ Кликает по инпуту и после этого вводит указанный текст """
        self.click_element(locator)
        self.send_keys(locator, text)

    def combobox_select(self, locator_value, locator_select, option):
        """ Кликает на дропдаун с предвводом и выбирает указанную опцию из селекта """
        self.click_element(locator_value)
        self.send_keys(locator_value, option)
        self.click_element(locator_select)

    def selectbox_select(self, locator_base, locator_option, option):
        """ Кликает на дропдаун селекта и выбирает указанную опцию. `locator_base`
        указывает локатор, куда нажать для того, чтобы появился выпадающий список.
        А локатор `location_option` должен представлять собой шаблон с одним параметром
        строки `{}`, который будет заменён на текст опции (мы не ориентируемся на номер
        опции по очереди, потому что их расположение друг относительно друга может
        поменяться).
        """
        self.click_element(locator_base)
        by, loc = locator_option
        loc = loc.format(option)
        locator_option = by, loc
        self.click_element(locator_option)

    def wait_page_to_be_open(self):
        """ Этот метод ждет, пока браузер перейдет на эту страницу (поменяется URL в строке
        адреса и будет найден элемент TITLE на странице.
        """
        self.wait_for_url(self.url)
        return self.wait_for(self.pageloc)

    @allure.step("Кликаем лого Яндекс")
    def click_yandex_logo(self):
        self.find_element(self.locators.LOGO_YANDEX).click()

    @allure.step("Кликаем лого Самокат")
    def click_scooter_logo(self):
        self.find_element(self.locators.LOGO_SCOOTER).click()
