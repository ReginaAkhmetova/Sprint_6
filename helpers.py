import datetime
import random


def get_ordering_test_data():
    random_date = datetime.date.today() + datetime.timedelta(days=random.randint(2, 59))
    return {
        'name': random.choice(["Регина", "Екатерина", "Юлия"]),
        'surname': random.choice(["Ахметова", "Иванова", "Петрова"]),
        'address': f"г.Екатеринбург, ул. Куйбышева {random.randint(1, 99)} кв.{random.randint(1, 200)}",
        'station': random.choice(["Динамо", "Лубянка", "Аэропорт"]),
        'phone': "+79" + "".join([str(random.randint(0, 9)) for _ in range(9)]),
        'date': "%02d.%02d.%04d" % (random_date.day, random_date.month, random_date.year),
        'period': random.choice([
            "сутки",
            "двое суток",
            "трое суток",
            "четверо суток",
            "пятеро суток",
            "шестеро суток",
            "семеро суток",
        ]),
        'color': random.choice(['black', 'grey']),
        'comment': "Какой-то комментарий",
    }
