### Тесты для сайта https://qa-scooter.praktikum-services.ru/
=====

#### Тестовые сценарии

#### Выпадающий список в разделе «Вопросы о важном». 
````
    1. Когда нажимаешь на стрелочку, открывается соответствующий текст. 
    2. Заказ самоката. Нужно проверить весь флоу позитивного сценария с двумя наборами данных.
        - Проверить точки входа в сценарий, их две: кнопка «Заказать» вверху страницы и внизу.
    3. Заполнить форму заказа.
        - Проверить, что появилось всплывающее окно с сообщением об успешном создании заказа.
        - Проверить: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».
        - Проверить: если нажать на логотип Яндекса, в новом окне через редирект откроется главная 
          страница Дзена.

````

#### Для работы необходимо:
````
1. Установи зависимости из requirements.txt
````
pip3 install -r requirements.txt
````
2. Запусти тесты из корневого каталога проекта:
````
pytest tests --alluredir=allure_results
````
3. Посмотри отчет Allure:
````
allure serve allure_results 
````
#### Запуск тестов
````
pytest -v tests
````