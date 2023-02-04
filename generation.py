# генерация списка новых объектов класса Train

import datetime
import random

types = ['скорый', 'пассажирский', 'товарный']


def generate_date():
    d = datetime.date(random.randrange(2000, 2023), random.randrange(1, 13), random.randrange(1, 28))
    return d.strftime("%m/%d/%Y")


def generate_time():
    h = random.randrange(0, 24)
    h = f'0{h}' if h < 10 else str(h)

    m = random.randrange(0, 60)
    m = f'0{m}' if m < 10 else str(m)

    return f'{h}:{m}'


def generate(n):
    final_dict = {}
    dates = []
    dep_time = []
    trav_time = []
    num = []
    type_ = []
    for i in range(n):
        dates.append(generate_date())
        dep_time.append(generate_time())
        trav_time.append(round(random.uniform(1, 48), 2))
        num.append(random.randrange(1, 1000))
        type_.append(types[random.randrange(0, 3)])
    final_dict['Дата отправления'] = dates
    final_dict['Время отправления'] = dep_time
    final_dict['Время в пути'] = trav_time
    final_dict['Номер поезда'] = num
    final_dict['Тип поезда'] = type_
    return final_dict
